# Panduan Dosen — Pengolahan Citra Digital Berbasis Eksperimen

**Sasaran:** mahasiswa S1 Teknik Fisika/Elektro/Informatika semester awal yang telah belajar Python dasar dan pengukuran. Pembelajaran menggunakan pendekatan fenomena fisik → model matematis → eksperimen terkendali → interpretasi → validitas eksternal.

## Capaian pembelajaran

Setelah selesai, mahasiswa mampu: (1) menjelaskan representasi, sampling, kuantisasi, dan noise pada sistem pencitraan; (2) menggunakan filter, segmentasi, Fourier, ekstraksi fitur, dan koreksi warna; (3) merancang pipeline machine learning dengan pembagian data yang benar; (4) membaca confusion matrix dan F1, mengkritisi klaim model, serta menjelaskan keterbatasan dataset; (5) menulis mini technical report berbasis hasil yang dapat direproduksi.

## Model sesi 100 menit

| Waktu | Aktivitas | Bukti |
|---|---|---|
| 0–10 menit | Pemantik: kegagalan citra pada fenomena nyata | Dugaan awal setiap mahasiswa |
| 10–25 menit | Penjelasan intuisi, diagram, persamaan, satuan | Sketsa sebab-akibat |
| 25–55 menit | Praktikum notebook | Notebook yang berjalan |
| 55–80 menit | Variasi parameter dan mini eksperimen | Dua grafik/perbandingan kuantitatif |
| 80–95 menit | Diskusi kegagalan dan generalisasi | Jawaban kritis berbukti |
| 95–100 menit | Exit ticket | Satu klaim, satu bukti, satu batasan |

## Pemantik dan miskonsepsi per topik

- **Sampling:** piksel lebih banyak tidak otomatis meningkatkan resolusi optik, karena PSF dan sistem lensa turut membatasi.
- **Kuantisasi:** jumlah bit memperhalus intensitas; tidak menambah informasi spasial yang hilang.
- **Denoising:** filter yang agresif juga dapat merusak tepi/tekstur penting bagi inspeksi.
- **Segmentasi:** area dalam piksel tidak otomatis menjadi ukuran fisik tanpa kalibrasi skala.
- **Fourier:** spektrum tidak boleh diperlakukan sebagai foto objek yang langsung ditafsirkan spasial.
- **Warna:** auto white balance, sensor spectral response, exposure, dan reference illuminant memengaruhi warna; perbedaan RGB mentah bukan bukti perbedaan bahan.
- **ML:** skor test yang tinggi pada data sintetis tidak bisa diekstrapolasi ke alat nyata; jangan membandingkan model yang memakai setup split berbeda.

## Penguatan ilmiah untuk sesi 10–14

- **Sesi 10:** baseline sederhana dan HOG+SVM pada `digits`. Catat variance antar seed sebagai diskusi lanjutan; `digits` kecil dan bukan dataset tulisan tangan dari semua populasi.
- **Sesi 11:** lab QC tablet sintetis. Ajukan *false negative* sebagai risiko mutu, serta konsekuensi threshold.
- **Sesi 12:** eksperimen iluminasi dan patch referensi. Diskusikan kenapa *white balance* belum dapat menggantikan kalibrasi kolorimetri dengan target standar.
- **Sesi 13:** *GroupKFold* untuk pemilihan fitur pada train. Sisihkan test untuk evaluasi akhir, bukan trial-and-error berulang.
- **Sesi 14:** CNN opsional, **butuh PyTorch tambahan**. Jangan mewajibkan pada komputer mahasiswa tanpa cukup RAM/CPU.

## Proyek 1–2 minggu

**Judul:** Analisis robustitas algoritma pengolahan citra terhadap variasi akuisisi. Kelompok 2–3 orang; setiap kelompok memilih satu dari kasus digit, tablet, atau warna. Wajib minimal dua kondisi gangguan, tiga rancangan/variasi model, dan satu baseline. Deliverables: notebook bersih + laporan 6–8 halaman + reproducibility table (versi Python, package, seed, split).

**Kriteria selesai:** semua kode berjalan dari kernel baru; tabel metrik jujur; confusion matrix sesuai label; train/test tanpa group overlap bila berbasis batch; ada analisis kegagalan; keterbatasan data dan validasi nyata tertulis.

## Catatan sebelum menggunakan di kelas

Jalankan `python -m pytest -q` dan `python scripts/validasi_notebook.py`. Untuk mengecek hasil notebook secara penuh, jalankan ulang pada environment Python yang sudah terinstal. Jangan mengklaim eksperimen fisik hanya karena generator sintetis berhasil. Jika mengganti data, selalu audit sumber data, izin, anotasi, duplikasi, grouping, dan prosedur pengukuran.
