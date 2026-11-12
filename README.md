"""Dataset sintetis untuk praktikum pengolahan citra terapan pada Teknik Fisika.

Tujuan:
- merepresentasikan citra termal, pola speckle, dan defect material
- mencontohkan data sintetis yang dapat dipakai untuk eksplorasi metodologis
- bukan mewakili data eksperimen industri maupun hasil pengukuran yang valid secara ilmiah
"""

from __future__ import annotations

import numpy as np
from skimage.draw import disk, line, polygon
from skimage.filters import gaussian


def thermography_sintetis(
    n_batch: int = 12,
    per_batch: int = 16,
    seed: int = 42,
    size: int = 128,
):
    """Membuat citra termal sintetis dengan defect berukuran lokal.

    Return:
        images: array (n_samples, H, W)
        labels: 0 = tanpa defect, 1 = defect
        groups: batch ID
    """
    if n_batch < 2 or per_batch < 4:
        raise ValueError("n_batch >= 2 dan per_batch >= 4 diperlukan")

    rng = np.random.default_rng(seed)
    images, labels, groups = [], [], []

    for batch in range(n_batch):
        base_temp = 30.0 + 5.0 * batch
        noise_level = 0.6 + 0.15 * batch

        for i in range(per_batch):
            img = np.full((size, size), base_temp, dtype=float)

            # background pola tidak homogen
            x = np.linspace(0, 1, size)
            y = np.linspace(0, 1, size)
            yy, xx = np.meshgrid(y, x, indexing="ij")
            gradient = 2.5 * (xx + 0.5 * yy)
            img += gradient * 12.0

            # defect termal berbentuk bulat atau elips
            defect = int(i % 2 == 1)
            cy = int(size / 2 + rng.integers(-10, 11))
            cx = int(size / 2 + rng.integers(-10, 11))
            radius = int(rng.integers(10, 18))
            rr, cc = disk((cy, cx), radius, shape=img.shape)

            if defect:
                img[rr, cc] -= 12.0 + rng.uniform(0.0, 6.0)
                rr2, cc2 = disk((cy + 2, cx + 2), max(3, radius // 3), shape=img.shape)
                img[rr2, cc2] -= 8.0
            else:
                img[rr, cc] += 1.0 + rng.uniform(0.0, 2.0)

            img += rng.normal(0.0, noise_level, size=img.shape)
            img = gaussian(img, sigma=1.0, preserve_range=True)

            images.append(np.clip(img, 0, 100).astype(np.float32))
            labels.append(defect)
            groups.append(batch)

    return np.stack(images), np.asarray(labels), np.asarray(groups)


def dic_sintetis(
    n_batch: int = 12,
    per_batch: int = 20,
    seed: int = 42,
    size: int = 128,
):
    """Membuat pola speckle sintetis untuk simulasi DIC.

    Return:
        images: array (n_samples, H, W)
        labels: 0 = deformasi kecil, 1 = deformasi sedang
        groups: batch ID
    """
    rng = np.random.default_rng(seed)
    images, labels, groups = [], [], []

    for batch in range(n_batch):
        for i in range(per_batch):
            img = np.zeros((size, size), dtype=float)

            n_points = 1800
            ys = rng.integers(0, size, n_points)
            xs = rng.integers(0, size, n_points)
            img[ys, xs] = rng.uniform(0.2, 1.0)

            shift = 1 + batch // 2
            if i % 2 == 0:
                displacement = 2.0
            else:
                displacement = 5.0

            shifted = np.roll(img, shift=int(displacement), axis=0)
            shifted = np.roll(shifted, shift=int(displacement * 0.7), axis=1)

            img = img * 0.7 + shifted * 0.3
            img += rng.normal(0.0, 0.03, size=img.shape)

            images.append(np.clip(img, 0, 1.0).astype(np.float32))
            labels.append(int(i % 2))
            groups.append(batch)

    return np.stack(images), np.asarray(labels), np.asarray(groups)


def tablet_sintetis(n_batch: int = 24, per_batch: int = 16, seed: int = 42):
    """Bangun citra tablet utuh/cacat. Kembalikan (images, label, kelompok).
    Versi ini tetap dipertahankan untuk kompatibilitas dengan modul existing.
    """
    if n_batch < 2 or per_batch < 4:
        raise ValueError("n_batch >= 2 dan per_batch >= 4 diperlukan")
    rng = np.random.default_rng(seed)
    size = 96
    images, labels, groups = [], [], []
    for batch in range(n_batch):
        shift = rng.uniform(-18, 18)
        base_bg = 36 + shift / 3
        base_fg = 182 + shift
        for i in range(per_batch):
            is_defect = int((i % 2) == 1)
            cy, cx = 48 + int(rng.integers(-4, 5)), 48 + int(rng.integers(-4, 5))
            radius = int(rng.integers(25, 30))
            arr = rng.normal(base_bg, 3.0, (size, size))
            rr, cc = disk((cy, cx), radius, shape=arr.shape)
            arr[rr, cc] = rng.normal(base_fg, 5.5, len(rr))
            if is_defect:
                if i % 4 == 1:
                    a = rng.uniform(0, np.pi)
                    length = radius * 0.7
                    y0, x0 = int(cy - length * np.sin(a)), int(cx - length * np.cos(a))
                    y1, x1 = int(cy + length * np.sin(a)), int(cx + length * np.cos(a))
                    lr, lc = line(y0, x0, y1, x1)
                    for r, c in zip(lr, lc):
                        ylow, yhigh = max(0, r - 2), min(size, r + 3)
                        xlow, xhigh = max(0, c - 2), min(size, c + 3)
                        arr[ylow:yhigh, xlow:xhigh] = base_bg + 8
                else:
                    angle = rng.uniform(-np.pi, np.pi)
                    vx, vy = np.cos(angle), np.sin(angle)
                    tx, ty = -vy, vx
                    center_x, center_y = cx + radius * vx, cy + radius * vy
                    p = np.array([
                        [center_y - vy * 13 + ty * 12, center_x - vx * 13 + tx * 12],
                        [center_y + vy * 13 + ty * 17, center_x + vx * 13 + tx * 17],
                        [center_y + vy * 13 - ty * 17, center_x + vx * 13 - tx * 17],
                    ])
                    pr, pc = polygon(p[:, 0], p[:, 1], shape=arr.shape)
                    arr[pr, pc] = base_bg
            arr = gaussian(arr, sigma=0.65, preserve_range=True)
            arr += rng.normal(0, 2.2, (size, size))
            images.append(np.clip(arr, 0, 255).astype(np.uint8))
            labels.append(is_defect)
            groups.append(batch)
    return np.stack(images), np.asarray(labels), np.asarray(groups)


def kolorimetri_sintetis(n_batch: int = 24, per_batch: int = 18, seed: int = 42):
    """Citra patch warna + patch referensi abu-abu, per-batch pencahayaan berbeda."""
    if n_batch < 2 or per_batch < 4:
        raise ValueError("n_batch >= 2 dan per_batch >= 4 diperlukan")
    rng = np.random.default_rng(seed)
    images, labels, groups = [], [], []
    colors = np.asarray([[111, 156, 104], [149, 119, 77]], dtype=float)
    for batch in range(n_batch):
        gain = rng.uniform(0.85, 1.15) * rng.uniform(0.70, 1.30, size=3)
        for i in range(per_batch):
            label = i % 2
            img = np.full((64, 96, 3), 20.0)
            obj = colors[label] + rng.normal(0, 6, 3)
            ref = np.array([128., 128., 128.])
            img[6:58, 5:62, :] = obj
            img[12:52, 72:90, :] = ref
            img = img * gain[None, None, :] + rng.normal(0, 2.5, img.shape)
            images.append(np.clip(img, 0, 255).astype(np.uint8))
            labels.append(label)
            groups.append(batch)
    return np.stack(images), np.asarray(labels), np.asarray(groups)


__all__ = [
    "thermography_sintetis",
    "dic_sintetis",
    "tablet_sintetis",
    "kolorimetri_sintetis",
]


if __name__ == "__main__":
    # demo kecil agar file tetap eksploratif dan dapat di-debug
    imgs, labels, groups = thermography_sintetis(n_batch=2, per_batch=4, seed=7)
    print("thermography_sintetis:", imgs.shape, labels.shape, groups.shape)
    imgs2, labels2, groups2 = dic_sintetis(n_batch=2, per_batch=4, seed=7)
    print("dic_sintetis:", imgs2.shape, labels2.shape, groups2.shape)
