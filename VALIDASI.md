# Catatan Pengujian Rilis v0.1.0

**Tanggal pengujian:** 12 November 2026.

## Lingkungan pengujian yang tersedia

- Python: 3.13.5 (Linux)
- NumPy: 2.3.5
- scikit-image: 0.26.0
- scikit-learn: 1.8.0
- matplotlib: 3.10.8
- SciPy: 1.17.0
- pandas: 2.2.3
- PyTorch: 2.10.0+cpu (hanya notebook opsional)

## Pemeriksaan yang benar-benar dijalankan

| Uji | Hasil | Cara ulang |
|---|---|---|
| Paket lokal terpasang | Lulus, editable install tanpa mengunduh dependencies | `pip install --no-deps --no-build-isolation -e .` hanya jika dependencies sudah terinstal |
| Unit test datasets/features/split/metrics | **6/6 lulus** | `python -m pytest -q` |
| Struktur dan sintaks 14 notebook | **14/14 valid** | `python scripts/validasi_notebook.py` |
| Eksekusi seluruh sel kode notebook | **14/14 lulus** pada lingkungan tersebut | `python scripts/uji_eksekusi_notebook.py --cnn` |
| CLI digit / tablet / warna | Ketiganya selesai tanpa error | `python scripts/latih_model.py --kasus ...` |

**Batas pengujian:** Eksekusi notebook dilakukan melalui smoke-test Python yang menjalankan sel kode berurutan dengan backend Matplotlib noninteraktif, bukan melalui sesi GUI JupyterLab. Belum dilakukan verifikasi di Windows dan macOS. GitHub Actions sudah disiapkan, tetapi belum dijalankan di server GitHub sebelum repository dipublikasikan. Notebook CNN opsional memerlukan `torch` yang dipasang terpisah.

## Contoh hasil yang diamati pada satu seed dan split

| Kasus | Sampel train | Sampel test | Macro-F1 |
|---|---:|---:|---:|
| Digit | 1.347 | 450 | 0,9776 |
| Tablet sintetis | 288 | 96 | 1,0000 |
| Warna sintetis + patch referensi | 324 | 108 | 1,0000 |

**PERINGATAN ILMIAH:** Dua hasil sempurna merupakan capaian pada **simulasi yang dibuat sederhana**. Ini *bukan* validasi terhadap tablet farmasi, warna bahan, kamera, atau pengukuran nyata. Hasil juga dapat berubah ketika seed, generator, pencahayaan, gangguan, dependensi, atau metode pembagian data diubah. Peningkatan kualitas studi perlu memprioritaskan desain dataset dan domain shift, bukan menaikkan akurasi simulasi semata.

## Langkah quality assurance untuk kontributor

1. Jalankan unit test dan pemeriksaan sintaks.
2. Jalankan notebook dengan `Kernel → Restart Kernel and Run All Cells` di JupyterLab.
3. Pastikan grafik dan tabel konsisten dengan narasi, bentuk array, dan definisi fitur.
4. Jika menambahkan sumber data nyata, dokumentasikan lisensi, provenans, unit akuisisi, prosedur kalibrasi, label, dan aturan privasi.
5. Jalankan validasi antarbatches, klasifikasi per kelas, audit leakage, dan monitoring sesudah penerapan.
