"""Ekstraksi fitur klasik yang dapat diaudit langkah demi langkah."""
from __future__ import annotations

import numpy as np
from skimage import measure
from skimage.filters import threshold_otsu, sobel
from skimage.morphology import opening, disk

FITUR_TABLET = (
    "rasio_luas", "sirkularitas", "soliditas", "eksentrisitas",
    "rata_intensitas", "simpangan_intensitas", "densitas_tepi",
)
FITUR_WARNA = ("R", "G", "B", "r", "g", "b")


def fitur_tablet(image: np.ndarray) -> np.ndarray:
    """Ekstraksi geometrik, intensitas, dan gradien dari 1 citra grayscale."""
    img = np.asarray(image)
    if img.ndim != 2 or img.size == 0:
        raise ValueError("Masukan harus citra grayscale 2-D")
    threshold = threshold_otsu(img)
    mask = opening(img > threshold, disk(1))
    labeled = measure.label(mask)
    props = measure.regionprops(labeled)
    if not props:
        return np.zeros(len(FITUR_TABLET), dtype=float)
    obj = max(props, key=lambda p: p.area)
    main = labeled == obj.label
    y, x = np.nonzero(main)
    inner_intensity = img[y, x].astype(float) / 255.0
    perim = max(obj.perimeter, 1.0)
    circularity = min(4 * np.pi * obj.area / perim**2, 2.0)
    edge_density = float(np.mean(sobel(img.astype(float) / 255.0)[main]))
    return np.array([
        obj.area / img.size,
        circularity,
        obj.solidity,
        obj.eccentricity,
        inner_intensity.mean(),
        inner_intensity.std(),
        edge_density,
    ], dtype=float)


def fitur_kolorimetri(image: np.ndarray, koreksi_referensi: bool = True) -> np.ndarray:
    """Fitur RGB dan chromaticity dari objek; koreksi diagonal via patch abu-abu.

    Patch objek: [6:58, 5:62]; referensi: [12:52, 72:90]. Koreksi sederhana
    hanya cocok sebagai ilustrasi white balance, BUKAN color calibration penuh.
    """
    img = np.asarray(image, dtype=float)
    if img.shape != (64, 96, 3):
        raise ValueError("Citra yang diharapkan berukuran (64, 96, 3)")
    obj = img[6:58, 5:62].mean(axis=(0, 1))
    if koreksi_referensi:
        ref = img[12:52, 72:90].mean(axis=(0, 1))
        obj = obj * (128.0 / np.maximum(ref, 1.0))
    s = max(obj.sum(), 1.0)
    chroma = obj / s
    return np.r_[obj / 255.0, chroma]
