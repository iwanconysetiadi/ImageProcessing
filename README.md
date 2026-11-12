# Pengolahan Citra Digital & Machine Learning — Bahasa Indonesia

**Repository terbuka untuk belajar, praktikum, dan pengajaran tingkat awal–menengah (S1).** Alur utamanya: dari fisika pembentukan citra → operasi piksel → filter → segmentasi → fitur → pengenalan pola → evaluasi machine learning → proyek mini.

Semua materi ditulis dalam Bahasa Indonesia. Notebook dapat dijalankan di JupyterLab atau VS Code dengan Python lokal. Dataset contoh disertakan lewat paket Python standar atau generator data sintetis sehingga **tidak memerlukan akses internet saat eksekusi** sesudah dependensi terpasang.

> **Status:** rilis awal v0.1.0. Modul dasar + ML klasik + demonstrasi CNN opsional. Contoh QC tablet/kolorimetri memakai data sintetis, **bukan hasil eksperimen industri atau bukti akurasi dunia nyata**.

## Mulai dalam 5 menit

Gunakan Python **3.10 atau lebih baru** (disarankan 3.11) dan terminal pada folder utama repository.

**Windows PowerShell:**

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[belajar,test]"
jupyter lab
```

Jika `py -3.11` tidak tersedia, gunakan `python -m venv .venv`. Jika PowerShell memblokir aktivasi, buka terminal Command Prompt dan gunakan `.venv\Scripts\activate.bat`.

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[belajar,test]'
jupyter lab
```

Lalu buka `notebooks/00_orientasi.ipynb`, jalankan sel berurutan (`Run All`). Di VS Code, buka folder repository dan pilih kernel dari `.venv`.

**Jalankan model tanpa notebook:**

```bash
python scripts/latih_model.py --kasus digit
python scripts/latih_model.py --kasus tablet
python scripts/latih_model.py --kasus warna
```

Perintah tersebut mencetak metrik dan confusion matrix sebagai JSON ke terminal; *tidak* mengunggah data ataupun menghubungi API.

**Uji kualitas kode:**

```bash
python -m pytest -q
python scripts/validasi_notebook.py
python scripts/uji_eksekusi_notebook.py
```

## Kurikulum: 14 sesi

| Sesi | Notebook | Materi utama | Keluaran pembelajaran |
|---|---|---|---|
| 1 | [00 Orientasi](notebooks/00_orientasi.ipynb) | Jupyter, citra dan ROI | Menjelaskan bentuk array |
| 2 | [01 Representasi](notebooks/01_representasi.ipynb) | Sampling, bit depth, kanal | Menguji aliasing/kuantisasi |
| 3 | [02 Histogram](notebooks/02_histogram.ipynb) | Kontras, histogram, CLAHE | Membaca perubahan distribusi |
| 4 | [03 Filter](notebooks/03_filter.ipynb) | Gaussian, median, noise | Menggunakan PSNR terkontrol |
| 5 | [04 Tepi](notebooks/04_tepi.ipynb) | Sobel, Canny, morfologi | Mengevaluasi hasil tepi |
| 6 | [05 Segmentasi](notebooks/05_segmentasi.ipynb) | Otsu, label, area, centroid | Mengukur objek dari piksel |
| 7 | [06 Frekuensi](notebooks/06_frekuensi.ipynb) | FFT 2D, filter frekuensi | Membaca domain spasial/Fourier |
| 8 | [07 Warna](notebooks/07_warna.ipynb) | RGB, HSV, Lab, iluminasi | Menilai perubahan white balance |
| 9 | [08 Fitur](notebooks/08_fitur.ipynb) | HOG, ekstraksi fitur | Menghubungkan gradien ke fitur ML |
| 10 | [09 ML Digit](notebooks/09_ml_digits.ipynb) | LogReg, HOG+SVM | Evaluasi klasifikasi multikelas |
| 11 | [10 ML Tablet](notebooks/10_ml_tablet.ipynb) | QC sintetis, fitur bentuk | Split antar-batch & ablasi |
| 12 | [11 ML Kolorimetri](notebooks/11_ml_kolorimetri.ipynb) | RGB, patch referensi, ML | Uji generalisasi iluminasi |
| 13 | [12 Proyek akhir](notebooks/12_proyek_akhir.ipynb) | Pipeline + GroupKFold | Laporan dan error analysis |
| 14 | [13 CNN opsional](notebooks/13_cnn_opsional.ipynb) | Conv2D, PyTorch | Membandingkan fitur klasik dan CNN |

Notebook `13` membutuhkan instalasi **opsional** PyTorch, lihat [panduan resminya](https://pytorch.org/get-started/locally/), disesuaikan dengan komputer. Semua notebook `00–12` hanya memerlukan dependensi inti dan `belajar`.

## Studi kasus machine learning

| Studi kasus | Sumber data | Model dan fitur | Disiplin evaluasi |
|---|---|---|---|
| **Mengenali angka** | `sklearn.load_digits` (1.797 citra 8×8) | Regresi logistik piksel; SVM + HOG | Split stratified; confusion matrix dan macro-F1 |
| **Inspeksi tablet** | Simulasi utuh, retak, tepi cacat | Fitur geometrik/intensitas + regresi logistik | Group split per batch; baseline mayoritas; ablasi |
| **Klasifikasi warna** | Simulasi objek dengan perubahan RGB antar lampu | Fitur raw vs koreksi patch referensi | Group split per kondisi iluminasi; pembahasan koreksi |
| **Pengenalan CNN** (opsional) | `sklearn.load_digits` | CNN PyTorch 2 konvolusi | Held-out test, hasil bergantung seed/epoch |

### Prinsip penting

- **Evaluasi objektif:** train/test dipisahkan sebelum mengukur hasil; normalisasi untuk ML dibungkus `Pipeline` agar parameter hanya dipelajari dari train.
- **Data leakage:** citra dari satu *batch* akuisisi tidak boleh otomatis dibagi ke train dan test; contoh sintetis menguji kondisi batch terpisah.
- **Akuntabilitas ilmiah:** akurasi tinggi pada data sintetis *tidak* membuktikan kesiapan inspeksi industri atau pengukuran warna sesungguhnya.
- **Reproducibility:** generator acak menggunakan seed tetap; perubahan parameter dan versi paket perlu dilaporkan.
- **Kegagalan harus dipelajari:** jangan berhenti setelah mencetak accuracy; bahas false positive/negative dan dampaknya pada sistem fisik.

## Struktur repository

```text
image-processing-indonesia/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── pyproject.toml
├── requirements.txt
├── notebooks/                 # 14 modul dengan visualisasi dan latihan
│   ├── 00_orientasi.ipynb
│   ├── 01_representasi.ipynb
│   └── ...
├── src/pengolahan_citra_id/
│   ├── datasets.py             # Generator simulasi tablet dan patch warna
│   ├── features.py             # Fitur bentuk, gradien, dan warna
│   └── evaluation.py           # Split per batch, macro-F1, balanced accuracy
├── scripts/
│   ├── latih_model.py          # Contoh CLI ML
│   ├── validasi_notebook.py    # Audit struktur/sintaks notebook
│   └── uji_eksekusi_notebook.py # Smoke test seluruh sel notebook inti
├── tests/                     # Unit tests Python
├── docs/                      # Panduan dosen, tugas, glosarium, referensi
├── data/README.md             # Sumber & batas interpretasi data
└── .github/workflows/test.yml # CI pytest dan cek notebook
```

## Untuk dosen / asisten praktikum

Baca [modul teori dan derivasi](docs/MODUL_TEORI.md), [panduan pengajaran](docs/PANDUAN_DOSEN.md), [rubrik penilaian](docs/TUGAS_DAN_RUBRIK.md), dan [glosarium](docs/GLOSARIUM.md). Setiap notebook berisi tujuan, ringkasan teori, kode runnable, analisis, pertanyaan HOTS, dan panduan laporan singkat. Atur sesi menjadi 2 × 50 menit dan tambah waktu mandiri untuk mini-project.

## Kontribusi dan publikasi di GitHub

1. Buat repository kosong di GitHub, misalnya `image-processing-indonesia`. **Jangan** centang README/License ketika membuatnya (keduanya telah ada di folder ini).
2. Buka terminal pada folder repository ini lalu jalankan (ganti `USERNAME`):

```bash
git init
git add .
git commit -m "Rilis awal materi pengolahan citra berbahasa Indonesia"
git branch -M main
git remote add origin https://github.com/USERNAME/image-processing-indonesia.git
git push -u origin main
```

Autentikasi GitHub (token/SSH/Git Credential Manager) harus disiapkan pada komputer pengguna. Jangan menaruh token dalam file atau commit. Jika repo sudah terhubung GitHub, cukup gunakan `git add`, `git commit`, dan `git push` tanpa membuat remote baru.

## Lisensi, data pihak ketiga, dan sumber ilmiah

Kode dan dokumentasi buatan repository ini menggunakan lisensi **MIT** (lihat `LICENSE`). Lisensi tidak otomatis berlaku untuk citra atau dataset pihak ketiga yang disediakan oleh paket pengembang. Dataset tidak disalin ke folder repository; hormati atribusi dan ketentuan pada dokumentasi sumber.

Sumber pustaka dan dokumentasi resmi tersedia di [REFERENSI](docs/REFERENSI.md), termasuk scikit-image, scikit-learn, PyTorch, dan buku dasar pengolahan citra.

## Pertanyaan riset yang bisa dikembangkan

Apa efek perubahan pencahayaan, resolusi, noise, dan orientasi terhadap prediksi? Seberapa berbeda performa random split vs batch split? Apa kontribusi koreksi warna terhadap generalisasi? Bagaimana mengukur ketidakpastian prediksi model saat kondisi gambar berubah?

**Tidak perlu API berbayar, kunci layanan, akun cloud, atau dataset sensitif.** Seluruh kode dapat dijalankan offline setelah pustaka terpasang.
