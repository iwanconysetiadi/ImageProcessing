<div align="center">

# Pengolahan Citra Digital & Machine Learning

### Dari pembentukan citra, pemodelan matematis, dan pengukuran ilmiah hingga pembelajaran mesin

**Materi terbuka berbahasa Indonesia · Jupyter Notebook · Python · Google Colab**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Colab](https://img.shields.io/badge/Run-Google%20Colab-F9AB00?logo=googlecolab&logoColor=black)](https://colab.research.google.com/github/iwanconysetiadi/ImageProcessing/blob/main/notebooks/00_orientasi.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**[Mulai belajar](#-jalur-pembelajaran) · [Buka di Colab](#-daftar-notebook-dan-google-colab) · [Instalasi](#-menjalankan-secara-lokal) · [Studi kasus](#-studi-kasus-dan-evaluasi) · [Kontribusi](#-kontribusi)**

</div>

---

## Tentang repository ini

**ImageProcessing** adalah repository pembelajaran **pengolahan citra digital (*digital image processing*) dan machine learning berbasis citra**, disusun dalam Bahasa Indonesia dan menggabungkan penjelasan ilmiah, derivasi matematis, pemrograman, serta evaluasi eksperimen.

Citra digital bukan sekadar matriks piksel. Nilainya dipengaruhi pembentukan bayangan, respons sensor, pencahayaan, sistem optik, sampling, kuantisasi, noise, dan keputusan pemrosesan. Karena itu, setiap notebook berusaha menghubungkan **model fisik → representasi matematis → algoritma → hasil numerik → interpretasi dan batas klaim**.

Repository ini ditujukan bagi mahasiswa, dosen, peneliti pemula, dan pembelajar mandiri. Pengguna dapat mempelajari konsep tanpa langsung membangun model besar atau memerlukan GPU, dan melanjutkan ke analisis berbasis data ketika siap.

> [!IMPORTANT]
> **Status materi:** notebook **00–13** merupakan bagian pembelajaran yang telah disusun; pembahasan lanjutan **14–24** ada dalam rencana pengembangan dan **belum boleh dianggap telah tersedia**. Periksa daftar file pada branch `main` untuk melihat revisi mana yang sudah di-*commit*. Hasil pengujian di lingkungan pengembangan tidak otomatis berarti setiap versi di GitHub sudah diuji di semua konfigurasi Colab atau perangkat.

### Orientasi pembelajaran

- **Dari prinsip, bukan resep:** memahami mengapa transformasi bekerja, asumsi yang dipakai, dan kondisi ketika gagal.
- **Matematika yang bisa diuji:** derivasi ditemani eksperimen numerik dan visualisasi.
- **Bermakna secara fisik:** intensitas, satuan, resolusi, kalibrasi, PSF/MTF, dan ketidakpastian diperlakukan serius.
- **Machine learning yang akuntabel:** baseline, pemisahan data, metrik, *data leakage*, kalibrasi, dan *domain shift*.
- **Terbuka dan reproducible:** kode Python, dataset bawaan pustaka atau simulasi terdokumentasi, serta instruksi pengulangan eksperimen.

## 🚀 Mulai cepat: tanpa instalasi melalui Google Colab

1. Pilih notebook pada [tabel materi](#-daftar-notebook-dan-google-colab).
2. Klik tombol **Open in Colab** pada baris notebook yang ingin dipelajari.
3. Hubungkan runtime Colab dan jalankan sel berurutan, atau pilih **Runtime → Run all**.
4. Untuk menyimpan pekerjaan pribadi, gunakan **File → Save a copy in Drive**. Perubahan dalam Colab **tidak otomatis memperbarui** repository GitHub.

Untuk notebook yang memerlukan modul lokal (`src/`) atau berkas dari folder repository, jalankan sel persiapan ini di awal sesi Colab:

```python
# Dijalankan pada Google Colab, satu kali setiap runtime baru.
import os
import subprocess

REPO = "/content/ImageProcessing"
if not os.path.isdir(REPO):
    subprocess.run(
        ["git", "clone", "https://github.com/iwanconysetiadi/ImageProcessing.git", REPO],
        check=True,
    )
os.chdir(REPO)
```

Lalu dalam **sel kode terpisah**:

```python
%pip install -q -e ".[belajar]"
```

> [!NOTE]
> Banyak notebook menggunakan pustaka yang telah tersedia pada runtime Colab, tetapi versi pustaka dapat berubah. Jika notebook membutuhkan PyTorch, periksa terlebih dahulu apakah `import torch` berhasil. Runtime Colab bersifat sementara; instalasi tambahan dan file yang dibuat di `/content` tidak selalu bertahan setelah sesi berakhir. Bila notebook sedang terbuka dari GitHub, periksa direktori kerja sebelum membaca berkas relatif.

## 🧭 Jalur pembelajaran

```text
00  Orientasi dan cara bekerja secara ilmiah
 │
 ├── 01  Representasi citra, sampling, dan sensor
 ├── 02  Histogram, transformasi intensitas, dan kalibrasi
 ├── 03  Filtering spasial, konvolusi, dan PSF
 ├── 04  Tepi, gradien, dan ketelitian lokalisasi
 ├── 05  Segmentasi, morfologi, dan pengukuran objek
 ├── 06  Fourier 2D, frekuensi spasial, dan OTF/MTF
 ├── 07  Warna, kolorimetri, dan iluminasi
 └── 08  Fitur citra, HOG, dan tekstur
       │
       ├── 09  Klasifikasi citra dengan machine learning
       ├── 10  Inspeksi tablet: fitur klasik vs. CNN
       ├── 11  Machine learning untuk kolorimetri
       ├── 12  Proyek integratif pengolahan citra
       └── 13  CNN, interpretabilitas, dan eksperimen kritis
```

Pembaca dapat mengikuti urutan 00–13, atau menggunakan urutan tematik: **imaging dan metrologi (01–07)**, **fitur dan machine learning (08–11)**, serta **riset terintegrasi (12–13)**. Notebook awal bukan syarat mutlak untuk membuka notebook berikutnya, tetapi pemahaman prasyarat sangat dianjurkan.

## 📚 Daftar notebook dan Google Colab

Tautan di bawah ditujukan ke branch `main` repository ini. Jika file belum diunggah atau namanya berubah, perbarui tautannya sesuai struktur aktual.

| No. | Materi | Fokus dan kemampuan yang dibangun | Notebook | Jalankan |
|:--:|---|---|:--:|:--:|
| 00 | **Orientasi** | Alur komputasi ilmiah, citra sebagai array, eksperimen yang terdokumentasi | [GitHub](notebooks/00_orientasi.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwanconysetiadi/ImageProcessing/blob/main/notebooks/00_orientasi.ipynb) |
| 01 | **Representasi Citra Digital** | Pembentukan sinyal, sensor, sampling, kuantisasi, aliasing, noise dan ketidakpastian | [GitHub](notebooks/01_representasi.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwanconysetiadi/ImageProcessing/blob/main/notebooks/01_representasi.ipynb) |
| 02 | **Histogram, Kontras, dan Normalisasi** | Histogram/CDF, HE, CLAHE, transformasi intensitas, dark–flat field | [GitHub](notebooks/02_histogram.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwanconysetiadi/ImageProcessing/blob/main/notebooks/02_histogram.ipynb) |
| 03 | **Filtering Spasial dan Konvolusi** | Konvolusi 2D, linearitas, noise, Gaussian/median/bilateral, PSF, bias–variance | [GitHub](notebooks/03_filter.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwanconysetiadi/ImageProcessing/blob/main/notebooks/03_filter.ipynb) |
| 04 | **Deteksi Tepi dan Gradien** | Sobel/Scharr, Canny, scale-space, ESF/LSF, ketelitian subpiksel | [GitHub](notebooks/04_tepi.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwanconysetiadi/ImageProcessing/blob/main/notebooks/04_tepi.ipynb) |
| 05 | **Segmentasi dan Morfologi** | Otsu, ambang lokal, opening/closing, watershed, evaluasi piksel–objek | [GitHub](notebooks/05_segmentasi.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwanconysetiadi/ImageProcessing/blob/main/notebooks/05_segmentasi.ipynb) |
| 06 | **Transformasi Fourier 2D** | Spektrum amplitudo/fase, Parseval, aliasing, notch filter, PSF/OTF/MTF | [GitHub](notebooks/06_frekuensi.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwanconysetiadi/ImageProcessing/blob/main/notebooks/06_frekuensi.ipynb) |
| 07 | **Ruang Warna dan Kolorimetri** | RGB linear, sRGB, XYZ/Lab, ΔE00, white balance, matriks kalibrasi warna | [GitHub](notebooks/07_warna.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwanconysetiadi/ImageProcessing/blob/main/notebooks/07_warna.ipynb) |
| 08 | **Ekstraksi Fitur dan Tekstur** | HOG, LBP, GLCM, filter Gabor, stabilitas fitur, pergeseran domain | [GitHub](notebooks/08_fitur.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwanconysetiadi/ImageProcessing/blob/main/notebooks/08_fitur.ipynb) |
| 09 | **Machine Learning untuk Klasifikasi Citra** | Digits, k-NN, regresi logistik, SVM, HOG, kalibrasi, robustness | [GitHub](notebooks/09_ml_digits.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwanconysetiadi/ImageProcessing/blob/main/notebooks/09_ml_digits.ipynb) |
| 10 | **Inspeksi Tablet: ML dan CNN** | Fitur geometri, CNN PyTorch, ablation, robustness, evaluasi berbasis batch | [GitHub](notebooks/10_ml_tablet.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwanconysetiadi/ImageProcessing/blob/main/notebooks/10_ml_tablet.ipynb) |
| 11 | **Machine Learning untuk Kolorimetri** | White balance, CCM, ΔE00, klasifikasi warna, ketidakpastian, domain shift | [GitHub](notebooks/11_ml_kolorimetri.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwanconysetiadi/ImageProcessing/blob/main/notebooks/11_ml_kolorimetri.ipynb) |
| 12 | **Proyek Integratif** | Model sensor → koreksi → segmentasi → fitur → ML → metrik → laporan ilmiah | [GitHub](notebooks/12_proyek_akhir.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwanconysetiadi/ImageProcessing/blob/main/notebooks/12_proyek_akhir.ipynb) |
| 13 | **Convolutional Neural Networks** | CNN, backpropagation, regularisasi, interpretabilitas, ablation, efisiensi | [GitHub](notebooks/13_cnn_opsional.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwanconysetiadi/ImageProcessing/blob/main/notebooks/13_cnn_opsional.ipynb) |

### Cara menggunakan setiap notebook

Sebagian besar notebook hasil pendalaman dirancang dengan alur berikut:

**Pertanyaan ilmiah → pengantar fisik → asumsi/model → derivasi → kode Python → eksperimen parameter → interpretasi → keterbatasan → latihan analitis/HOTS → koneksi ke materi berikutnya.**

Notasi matematika pada sel Markdown mengikuti format yang umumnya kompatibel dengan GitHub dan Colab: `$...$` untuk persamaan dalam kalimat dan `$$...$$` untuk persamaan terpisah.

## 🔬 Studi kasus dan evaluasi

| Studi kasus | Sumber data | Pertanyaan utama | Evaluasi yang relevan |
|---|---|---|---|
| **Restorasi sinyal citra** (01–03) | Citra referensi dan degradasi terkontrol | Apakah filter mengurangi noise tanpa merusak informasi? | PSNR, SSIM, profil tepi, galat pengukuran |
| **Pengukuran batas/objek** (04–05) | Citra sensor sintetis dengan ground truth | Seberapa tepat posisi, luas, dan jumlah objek? | MAE posisi/luas, Dice, IoU, F1 tingkat objek |
| **Periodisitas permukaan** (06) | Pola sintetis dengan perioda diketahui | Apakah kualitas citra yang membaik meningkatkan akurasi ukuran? | Galat perioda, PSNR/SSIM, uji gangguan |
| **Koreksi warna** (07) | Target warna sintetis dan referensi sRGB | Bagaimana pencahayaan dan respons sensor mengubah warna? | ΔE00, analisis residual dan domain shift |
| **Klasifikasi tekstur** (08) | Spesimen tekstur sintetis | Apakah HOG, LBP, dan GLCM tetap stabil saat domain berubah? | Macro-F1, ablasi, grouped split |
| **Pengenalan digit** (09, 13) | `sklearn.datasets.load_digits` | Bagaimana model klasik dibandingkan dengan CNN secara adil? | Macro-F1, confusion matrix, calibration, robustness |
| **Inspeksi tablet** (10, 12) | Data tablet sintetis dengan variasi batch | Apa pengaruh sensor, preprocessing, fitur, dan model? | Macro-F1, kesalahan segmentasi, bootstrap per batch |
| **Klasifikasi warna** (11) | Target/akuisisi warna sintetis | Apakah koreksi kolorimetri memperbaiki prediksi lintas perangkat? | ΔE00, macro-F1, evaluasi perubahan iluminasi |

> [!WARNING]
> **Jangan menyamakan simulasi dengan validasi eksperimen fisik.** Hasil pada data sintetis berguna untuk menguji algoritma, asumsi, dan protokol; hasil tersebut **bukan bukti** bahwa metode siap dipakai pada kamera nyata, inspeksi farmasi, atau pengukuran kolorimetri terkalibrasi. Skor tinggi pada test normal tidak menghilangkan risiko *domain shift*.

### Prinsip evaluasi yang wajib dijaga

1. Pisahkan **train, validation, dan test** sebelum memilih model atau parameter.
2. Pastikan spesimen atau batch yang saling terkait tidak bocor antar-split; gunakan pemisahan berbasis kelompok bila relevan.
3. Latih scaler, PCA, seleksi fitur, dan koreksi yang mempelajari parameter **hanya pada data yang diizinkan untuk pelatihan/kalibrasi**.
4. Bandingkan dengan baseline yang masuk akal, bukan hanya dengan hasil sebelumnya.
5. Laporkan lebih dari satu metrik: kualitas citra, kinerja tugas, dan biaya komputasi dapat bergerak ke arah berbeda.
6. Bedakan variabilitas karena seed, spesimen, perangkat, dan protokol pengukuran.
7. Sertakan *error analysis*, keterbatasan data, serta kondisi ketika kesimpulan tidak dapat digeneralisasi.

## 💻 Menjalankan secara lokal

### Prasyarat

- Python **3.10 atau lebih baru**; Python 3.11 disarankan.
- Git (untuk `clone`), atau unduh repository sebagai ZIP dari GitHub.
- RAM yang mencukupi untuk notebook standar; GPU **tidak wajib** untuk materi dasar.
- Koneksi internet diperlukan untuk mengunduh pustaka; sebagian besar dataset contoh dapat digunakan tanpa internet setelah lingkungan siap.

### Windows (PowerShell)

```powershell
git clone https://github.com/iwanconysetiadi/ImageProcessing.git
cd ImageProcessing
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[belajar,test]"
jupyter lab
```

Apabila `py -3.11` tidak tersedia, sesuaikan dengan Python yang terpasang. Jika aktivasi PowerShell diblokir, jalankan `cmd` dan gunakan `.venv\Scripts\activate.bat` tanpa mengubah pengaturan keamanan sistem secara global.

### Linux / macOS

```bash
git clone https://github.com/iwanconysetiadi/ImageProcessing.git
cd ImageProcessing
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[belajar,test]'
jupyter lab
```

Buka file `notebooks/00_orientasi.ipynb` untuk memulai. Pengguna VS Code dapat memilih kernel Python dari `.venv`.

### PyTorch (untuk notebook 10 dan 13)

Notebook CNN membutuhkan PyTorch. Gunakan [panduan instalasi resmi PyTorch](https://pytorch.org/get-started/locally/) untuk memilih paket CPU atau CUDA sesuai perangkat. Jangan mengasumsikan GPU tersedia; hasil waktu komputasi dapat berbeda antarperangkat.

### Menguji repository

Jika struktur awal `scripts/`, `tests/`, dan `pyproject.toml` tetap dipertahankan, jalankan:

```bash
python -m pytest -q
python scripts/validasi_notebook.py
python scripts/uji_eksekusi_notebook.py
```

> [!NOTE]
> Skrip eksekusi bawaan awal mungkin hanya menguji cakupan yang ditetapkan dalam skrip tersebut. Notebook revisi, dependency tambahan, dan pipeline PyTorch perlu diaudit secara terpisah. Status "lulus" hanya boleh dicantumkan setelah pengujian dijalankan untuk versi commit dan lingkungan yang dilaporkan.

## 📁 Struktur repository

Struktur berikut menunjukkan folder inti dari paket repository awal. **Berkas dataset dan laporan validasi tambahan mungkin berbeda** sesuai revisi yang telah diunggah.

```text
ImageProcessing/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── pyproject.toml
├── requirements.txt
├── notebooks/
│   ├── 00_orientasi.ipynb
│   ├── 01_representasi.ipynb
│   ├── 02_histogram.ipynb
│   ├── 03_filter.ipynb
│   ├── 04_tepi.ipynb
│   ├── 05_segmentasi.ipynb
│   ├── 06_frekuensi.ipynb
│   ├── 07_warna.ipynb
│   ├── 08_fitur.ipynb
│   ├── 09_ml_digits.ipynb
│   ├── 10_ml_tablet.ipynb
│   ├── 11_ml_kolorimetri.ipynb
│   ├── 12_proyek_akhir.ipynb
│   └── 13_cnn_opsional.ipynb
├── src/pengolahan_citra_id/       # Modul reusable versi awal
├── scripts/                       # Pelatihan dan validasi versi awal
├── tests/                         # Pengujian Python versi awal
├── data/                          # Dokumentasi dan data jika disertakan
├── docs/                          # Teori, panduan, rubrik, referensi
└── .github/workflows/            # CI jika diaktifkan
```

## 🧪 Reproducibility, dataset, dan batas klaim

**Asal-usul data.** Setiap studi kasus sebaiknya mencatat sumber, lisensi, jumlah sampel, ukuran citra, unit independen, label/ground truth, seed, skenario degradasi, dan protokol train–validation–test. Untuk dataset sintetis, sertakan generator dan asumsi model. Untuk data bawaan pustaka, rujuk dokumentasi dan lisensi sumber tersebut.

**Pemisahan dan kalibrasi.** Citra dari objek yang sama, batch yang sama, atau perangkat yang sama dapat saling berkorelasi. Kesalahan membagi data sebelum memahami unit independennya dapat menghasilkan kinerja yang terlalu optimistis. Koreksi berbasis patch referensi harus dibedakan dari penggunaan label test untuk penalaan model.

**Lingkungan.** Dokumentasikan versi Python, NumPy, SciPy, scikit-image, scikit-learn, PyTorch, dan seed yang dipakai. Untuk merekam lingkungan lokal:

```bash
python --version
python -m pip freeze > environment-used.txt
```

**Pelaporan.** Nyatakan metrik, interval ketidakpastian bila relevan, jumlah pengulangan, rincian split, keterbatasan perangkat dan akuisisi, serta kegagalan model. *Confidence* model yang tinggi belum tentu berarti probabilitas terkalibrasi atau keputusan yang dapat dipercaya.

**Hak data.** Jangan mengunggah citra berhak cipta, rekam medis, data personal, atau hasil industri rahasia tanpa hak dan izin yang sesuai. Lisensi kode repository tidak otomatis mengalihkan lisensi dataset pihak ketiga.

## 👩‍🏫 Untuk dosen dan mahasiswa

Repository ini dapat digunakan sebagai bahan ajar, praktikum, atau referensi awal mini-riset. Usulan alur setiap sesi:

1. **Sebelum kelas:** baca motivasi, prasyarat, dan pertanyaan diagnostik notebook.
2. **Dalam kelas:** bahas model dan asumsi, jalankan demonstrasi, lalu ubah satu parameter dengan hipotesis yang jelas.
3. **Sesudah kelas:** lakukan eksperimen pembanding, plot hasil, jelaskan bias dan ketidakpastian, serta tuliskan kesimpulan dengan batas klaim.

**Contoh keluaran tugas:** laporan teknis singkat yang memuat rumusan masalah, model, metode, data, rancangan evaluasi, hasil dengan visualisasi, diskusi kegagalan, dan reproducibility statement.

Rubrik yang disarankan (dapat diubah oleh pengampu): **ketepatan konsep 25%**, **kualitas eksperimen 25%**, **validitas evaluasi 20%**, **interpretasi kritis 20%**, dan **reproducibility serta dokumentasi 10%**.

Dokumen pendukung dari struktur awal:

- [Modul teori dan derivasi](docs/MODUL_TEORI.md)
- [Panduan dosen](docs/PANDUAN_DOSEN.md)
- [Tugas dan rubrik](docs/TUGAS_DAN_RUBRIK.md)
- [Glosarium](docs/GLOSARIUM.md)
- [Referensi](docs/REFERENSI.md)
- [Panduan kontribusi](CONTRIBUTING.md)

Dokumen khusus per notebook (misalnya *dataset card*, pembahasan latihan, dan laporan validasi) tersedia pada paket revisi masing-masing dan perlu diunggah secara terpisah jika ingin ditampilkan pada GitHub.

## 🗺️ Rencana pengembangan (belum dirilis)

Materi lanjutan berikut merupakan **roadmap**, bukan tautan notebook yang telah tersedia.

| Nomor | Rencana topik | Pertanyaan kunci |
|:--:|---|---|
| 14 | Pembentukan Citra dan *Inverse Problems* | Bagaimana merekonstruksi sinyal dari blur, noise, dan informasi tidak lengkap? |
| 15 | Optimisasi untuk Pengolahan Citra | Bagaimana memilih fungsi objektif, regularisasi, dan trade-off komputasi? |
| 16 | Bayesian Imaging dan Ketidakpastian | Kapan posterior/prediksi layak dipercaya dan bagaimana mengecek kalibrasinya? |
| 17 | Segmentasi dan Pengukuran Ilmiah | Bagaimana anotasi, matching objek, dan ketidakpastian memengaruhi hasil? |
| 18 | Deep Learning sebagai Objek Riset | Bagaimana menjalankan ablation dan perbandingan yang adil? |
| 19 | Domain Shift dan Generalisasi | Apa yang terjadi jika sensor, lokasi, batch, atau cahaya berubah? |
| 20 | Desain Eksperimen dan Inferensi Statistik | Bagaimana menguji perbedaan model tanpa leakage atau klaim berlebihan? |
| 21 | Reproducibility dan Tata Kelola Data | Bagaimana mempertahankan provenance, lisensi, dan versi eksperimen? |
| 22 | Studi Kasus Restorasi dan Dekonvolusi | Bagaimana membandingkan kualitas rekonstruksi dan ketahanan pada noise? |
| 23 | Studi Kasus Segmentasi dan Metrologi | Bagaimana mengevaluasi area, jumlah, dan ketidakpastian objek? |
| 24 | Studi Kasus Robustness Machine Learning | Bagaimana mendesain evaluasi pergeseran domain dan inferensi statistik? |

## 📖 Bacaan dan dokumentasi utama

- [NumPy](https://numpy.org/doc/stable/) — array dan operasi numerik.
- [SciPy](https://docs.scipy.org/doc/scipy/) — filtering, optimisasi, dan komputasi ilmiah.
- [scikit-image](https://scikit-image.org/docs/stable/) — algoritma pengolahan citra dan metrik.
- [scikit-learn](https://scikit-learn.org/stable/) — model ML, pipeline, split, dan evaluasi.
- [PyTorch](https://pytorch.org/docs/stable/) — pembelajaran mendalam dan autodifferentiation.
- [Matplotlib](https://matplotlib.org/stable/) — visualisasi ilmiah.
- [Google Colab](https://colab.research.google.com/) — eksekusi notebook di browser.

Literatur yang relevan antara lain *Digital Image Processing* (Gonzalez & Woods), *Computer Vision: Algorithms and Applications* (Szeliski), dan *Deep Learning* (Goodfellow, Bengio & Courville). Lihat [referensi repository](docs/REFERENSI.md) untuk bahan bacaan tambahan.

## 🤝 Kontribusi

Perbaikan penjelasan, koreksi persamaan, contoh baru, bug fix, dataset dengan izin distribusi yang jelas, dan pengujian lintas platform sangat diterima.

1. Buat *issue* yang menjelaskan usulan atau kesalahan yang ditemukan.
2. Buat fork dan branch perubahan.
3. Perbarui notebook sekaligus dokumentasi yang terkait; pertahankan Bahasa Indonesia yang jelas dan notasi yang konsisten.
4. Jalankan pengujian yang relevan, lalu jelaskan lingkungan dan hasilnya.
5. Buka *pull request* dengan ringkasan perubahan serta dampaknya terhadap hasil eksperimen.

Panduan selengkapnya: [CONTRIBUTING.md](CONTRIBUTING.md).

## ⚖️ Lisensi dan atribusi

**Kode dan dokumentasi asli repository** menggunakan lisensi **MIT**, sebagaimana tercantum pada [LICENSE](LICENSE) dari paket awal. Materi pihak ketiga, pustaka, dataset, dan ilustrasi eksternal tetap tunduk pada lisensi masing-masing. Jika file `LICENSE` di branch publik telah diubah, ikuti teks lisensi yang benar-benar berlaku pada commit tersebut.

Pengembangan materi: **[Iwan Cony Setiadi](https://github.com/iwanconysetiadi)**. Repository ini merupakan sumber belajar terbuka; tidak dengan sendirinya menyatakan dukungan atau persetujuan institusi tertentu.

Jika materi digunakan untuk pengajaran atau penelitian, sertakan atribusi ke repository dan commit/versi yang digunakan agar eksperimen dapat ditelusuri.

---

<div align="center">

**Pengolahan citra bukan hanya membuat gambar tampak lebih baik, melainkan memastikan informasi yang diekstraksi dapat dipahami, diukur, dan dipertanggungjawabkan.**

[↑ Kembali ke atas](#pengolahan-citra-digital--machine-learning)

</div>
