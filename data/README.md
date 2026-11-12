# Sumber Data dan Etika

Tidak ada dataset eksternal yang didistribusikan ulang di repository ini.

1. Modul dasar memakai citra contoh `skimage.data` yang tersedia lewat instalasi scikit-image: `camera`, `coins`, `astronaut`, `coffee`.
2. Praktikum pengenalan angka menggunakan `sklearn.datasets.load_digits` (1.797 citra 8×8; angka 0–9).
3. Praktikum inspeksi tablet dan kolorimetri memakai citra **sintetis** yang dibuat oleh kode di `src/pengolahan_citra_id/datasets.py`. Tidak ada label, akurasi, maupun data lapangan yang diklaim nyata.

**Larangan interpretasi:** dataset sintetis tidak boleh dipakai untuk membuat klaim kinerja industri, pangan, atau klinis. Untuk riset asli, dokumentasikan asal data, izin, kondisi pencahayaan, pembagian kelompok, dan pemeriksaan data leakage.

Dokumentasi sumber: https://scikit-image.org/docs/stable/api/skimage.data.html dan https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html
