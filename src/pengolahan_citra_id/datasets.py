"""Dataset sintetis untuk praktikum; tidak mewakili data industri/medis asli."""
from __future__ import annotations

import numpy as np
from skimage.draw import disk, line, polygon
from skimage.filters import gaussian


def tablet_sintetis(n_batch: int = 24, per_batch: int = 16, seed: int = 42):
    """Bangun citra tablet utuh/cacat. Kembalikan (images, label, kelompok).

    0 = utuh; 1 = cacat (retak/terkelupas). Setiap batch = variasi pencahayaan.
    Seluruh citra merupakan simulasi, bukan pengukuran tablet farmasi sesungguhnya.
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
                if i % 4 == 1:  # retak: pita gelap melintasi permukaan
                    a = rng.uniform(0, np.pi)
                    length = radius * 0.7
                    y0, x0 = int(cy - length * np.sin(a)), int(cx - length * np.cos(a))
                    y1, x1 = int(cy + length * np.sin(a)), int(cx + length * np.cos(a))
                    lr, lc = line(y0, x0, y1, x1)
                    for r, c in zip(lr, lc):
                        ylow, yhigh = max(0, r - 2), min(size, r + 3)
                        xlow, xhigh = max(0, c - 2), min(size, c + 3)
                        arr[ylow:yhigh, xlow:xhigh] = base_bg + 8
                else:  # bagian tepi hilang
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
    """Citra patch warna + patch referensi abu-abu, per-batch pencahayaan berbeda.

    0=kelas A dan 1=kelas B. Untuk pembelajaran klasifikasi, bukan alat penilai
    kesegaran makanan, diagnosis, atau kalibrasi kolorimetri sesungguhnya.
    """
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
