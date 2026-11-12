# Pengolahan Citra untuk Pengukuran dan Inspeksi Sistem Fisik
Versi umum, terapan, dan berbasis Teknik Fisika

Repository ini berfokus pada pengolahan citra sebagai alat untuk pengukuran, karakterisasi, dan inspeksi sistem fisik. Bukan hanya sekadar klasifikasi gambar, tetapi juga:
- deteksi cacat material,
- analisis deformasi dan regangan,
- inspeksi termal,
- pengukuran intensitas dan geometri,
- interpretasi citra dari sistem optik, termal, dan material.

Materi ini dirancang untuk mahasiswa, peneliti, dan praktisi yang ingin memahami bagaimana citra dapat digunakan untuk menganalisis fenomena fisik secara kuantitatif, dapat diulang, dan dapat dipertanggungjawabkan secara ilmiah.

---

## Tujuan Repository

Repository ini menghubungkan:
- fisika pembentukan citra,
- sensor dan kalibrasi,
- noise, blur, dan distorsi,
- ekstraksi fitur dan segmentasi,
- machine learning untuk inspeksi,
- validasi eksperimen dan interpretasi ilmiah.

Dengan kata lain, repository ini menekankan bahwa pengolahan citra bukan hanya sekadar teknik komputasi, tetapi juga alat pengukuran yang harus dipahami secara fisika, statistika, dan evaluasi eksperimen.

---

## Studi kasus utama

Repository ini menggunakan beberapa studi kasus yang relevan dengan Teknik Fisika dan rekayasa:

1. Thermography untuk inspeksi material
   - deteksi cacat internal dan permukaan
   - analisis suhu dan distribusi termal
   - pemetaan anomali termal

2. Digital Image Correlation (DIC)
   - pengukuran deformasi dan regangan
   - analisis bidang perpindahan pada benda uji
   - aplikasi pada mekanika dan struktur

3. Electroluminescence (EL) pada sel surya
   - identifikasi microcrack dan defect sel
   - evaluasi kualitas modul fotovoltaik
   - pemetaan distribusi respons listrik

4. Karakterisasi mikrostruktur material
   - citra mikroskopi dan permukaan
   - analisis tekstur, porositas, dan retakan
   - struktur material dan kualitas produksi

5. Metrologi optik sederhana
   - perubahan bentuk, dimensi, dan geometri
   - kalibrasi kamera dan estimasi ukuran
   - ketidakpastian pengukuran

---

## Prinsip utama materi

Semua studi kasus mengikuti prinsip berikut:
- citra adalah representasi data fisik, bukan hanya array angka;
- noise dan blur harus dipahami sebagai bagian dari sistem pengukuran;
- validasi harus memisahkan data train/test dengan hati-hati;
- hasil model tidak boleh dipandang sebagai kebenaran absolut tanpa interpretasi fisik;
- metode harus dibahas bersama dengan asumsi, keterbatasan, dan ketidakpastian.

---

## Struktur kurikulum

### Modul inti (00–13)

| Sesi | Notebook | Topik utama | Fokus pembelajaran |
|---|---|---|---|
| 00 | 00_orientasi.ipynb | Pengenalan citra dan sensor | Memahami citra sebagai data fisik |
| 01 | 01_representasi.ipynb | Representasi piksel, kanal, resolusi | Bit depth, sampling, dan ruang warna |
| 02 | 02_histogram.ipynb | Histogram, kontras, normalisasi | Menganalisis distribusi intensitas |
| 03 | 03_filter.ipynb | Filter spatial dan denoising | Mengurangi noise dan mempertahankan fitur |
| 04 | 04_tepi.ipynb | Edge detection dan morfologi | Mendeteksi batas objek dan cacat |
| 05 | 05_segmentasi.ipynb | Thresholding, Otsu, label, ROI | Memisahkan objek dari background |
| 06 | 06_frekuensi.ipynb | FFT, blur, filter frekuensi | Menganalisis domain frekuensi |
| 07 | 07_warna.ipynb | RGB, HSV, grayscale, pencahayaan | Memahami pengaruh iluminasi dan kalibrasi |
| 08 | 08_fitur.ipynb | Tekstur, bentuk, HOG, feature extraction | Mengubah citra menjadi informasi kuantitatif |
| 09 | 09_ml_dasar.ipynb | Machine learning dasar | Klasifikasi dan regresi pada data citra |
| 10 | 10_termografi.ipynb | Studi kasus thermography | Deteksi cacat termal dan analisis suhu |
| 11 | 11_dik.ipynb | Studi kasus DIC | Deformasi, regangan, dan tracking |
| 12 | 12_proyek_akhir.ipynb | Proyek akhir | Pipeline lengkap dan evaluasi ilmiah |
| 13 | 13_cnn_opsional.ipynb | CNN dasar (opsional) | Membandingkan model klasik dan deep learning |

---

## Materi lanjutan (setelah modul inti)

Repository ini juga menyediakan seri materi lanjutan yang lebih umum dan aplikatif:

### 1. Pembentukan citra dan masalah invers
- model sensor,
- blur dan point spread function (PSF),
- noise sensor,
- dekonvolusi,
- regularisasi,
- trade-off antara resolusi dan stabilitas.

### 2. Optimisasi untuk pemrosesan citra
- fungsi objektif,
- gradien dan descent,
- sparsity,
- regularization,
- trade-off kualitas–kompleksitas.

### 3. Bayesian imaging dan ketidakpastian
- posterior distribution,
- estimasi parameter fisik,
- kalibrasi instrument,
- saat prediksi model tidak dapat dipercaya.

### 4. Segmentasi dan pengukuran ilmiah
- variasi anotasi,
- metrik yang sesuai untuk objek dan wilayah,
- evaluasi pada tingkat objek,
- hubungan antara segmentasi dan pengukuran kuantitatif.

### 5. Deep learning sebagai alat riset
- ablation study,
- pembandingan model secara adil,
- robustness terhadap noise dan domain shift,
- efisiensi komputasi dan interpretabilitas.

### 6. Domain shift dan generalisasi
- perbedaan kamera,
- batch dan kondisi eksperimen,
- variasi pencahayaan,
- perbedaan lokasi dan protokol akuisisi.

### 7. Desain eksperimen dan inferensi statistik
- interval kepercayaan,
- ukuran efek,
- pengujian berulang,
- pencegahan data leakage,
- evaluasi yang dapat direproduksi.

### 8. Reproducibility dan tata kelola data
- provenance data,
- metadata eksperimen,
- lisensi dan batas penggunaan,
- dokumentasi lingkungan,
- aspek etika dan pelaporan batas klaim.

---

## Dataset yang digunakan

Repository ini memanfaatkan dataset yang umum dan dapat diakses secara ilmiah, terutama untuk domain teknik fisika:
- dataset termografi untuk inspeksi material
- benchmark DIC untuk deformasi
- dataset EL sel surya
- citra mikroskopi atau microstructure untuk karakterisasi material

Semua dataset harus digunakan dengan memperhatikan:
- sumber data,
- lisensi,
- metode akuisisi,
- prosedur kalibrasi,
- batas penggunaan,
- dan interpretasi hasil.

---

## Lingkungan kerja

Direkomendasikan:
- Python 3.10+
- JupyterLab atau VS Code
- NumPy, SciPy, scikit-image, scikit-learn, matplotlib, pandas
- PyTorch untuk notebook opsional
- Git untuk repositori dan dokumentasi

---

## Cara menjalankan

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[belajar,test]"
jupyter lab
```

Untuk menjalankan model utama:
```bash
python scripts/latih_model.py --kasus digit
python scripts/latih_model.py --kasus tablet
python scripts/latih_model.py --kasus warna
```

Untuk validasi:
```bash
python -m pytest -q
python scripts/validasi_notebook.py
python scripts/uji_eksekusi_notebook.py
```

---

## Etika dan interpretasi ilmiah

Repository ini menekankan pentingnya:
- tidak mengklaim hasil yang melebihi data yang tersedia,
- membedakan simulasi dengan eksperimen nyata,
- menggunakan data real untuk validasi final,
- memperhatikan ketidakpastian pengukuran,
- membahas keterbatasan model dan domain aplikasi.

---

## Kontribusi

Kontributor diharapkan:
- menambahkan dataset yang relevan dan terdokumentasi,
- menjaga struktur notebook yang konsisten,
- menuliskan asumsi eksperimen dan kalibrasi,
- menjelaskan sumber data dan batas interpretasi,
- menjaga reproduksibilitas hasil.

---

## Lisensi

Repository ini menggunakan lisensi MIT, kecuali untuk dataset pihak ketiga yang memiliki lisensi sendiri. Pengguna harus mematuhi syarat lisensi masing-masing dataset.

---

## Kesimpulan

Repository ini bukan hanya tempat belajar pengolahan citra secara umum, tetapi juga pengolahan citra untuk pengukuran, inspeksi, dan karakterisasi sistem fisik. Dengan pendekatan ini, materi menjadi lebih relevan bagi mahasiswa Teknik Fisika, rekayasa material, optik, dan eksperimen sains.

Tujuan utamanya adalah membangun kemampuan:
- membaca citra sebagai data fisik,
- menilai kualitas dan ketidakpastian sistem pengukuran,
- memodelkan fenomena fisik dari citra,
- dan memvalidasi hasil dengan pendekatan ilmiah yang benar.
