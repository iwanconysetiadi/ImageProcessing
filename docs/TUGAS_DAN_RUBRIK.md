# Proyek Akhir: Rancangan, Eksperimen, dan Audit Model Pengolahan Citra

## Deskripsi dan persyaratan

Pilih satu kasus (digit / tablet sintetis / klasifikasi patch warna sintetis) dan formulasi pertanyaan yang bisa diuji. Bandingkan minimal **dua pipeline model** dan **satu baseline**. Lakukan split train/test satu kali, pastikan transformasi fit hanya pada train, lakukan optimasi memakai validasi pada train, lalu laporkan test akhir. Bagi data berdasarkan batch bila satu kelompok gambar memiliki kondisi akuisisi identik.

## Keluaran

1. **Notebook `.ipynb`** yang dapat dijalankan dari kernel kosong; berisi sumber/versi data, visualisasi, kode, grafik, hasil.
2. **Laporan PDF** 6–8 halaman: abstrak singkat; latar belakang; metode; instrumen/data; rancangan evaluasi; hasil; pembahasan; keterbatasan; kesimpulan; referensi.
3. **Lampiran reproducibility**: versi Python/pustaka, seed, rasio data, pengelompokan batch, definisi label, dan tipe metrik.

## Rubrik (total 100)

| Aspek | Bobot | Sangat baik | Perlu perbaikan |
|---|---:|---|---|
| Definisi masalah dan teori | 15 | Pertanyaan dan model matematis tepat | Masalah/variabel tidak jelas |
| Kualitas data dan akuisisi | 15 | Sumber, label, tipe, batch, potensi bias dijelaskan | Data tidak bisa ditelusuri |
| Preprocessing dan fitur | 15 | Tiap operasi punya alasan dan uji | Parameter tidak dipertanggungjawabkan |
| Rancangan evaluasi dan anti leakage | 20 | Train/test dan kelompok benar; validasi tidak menyentuh test | Test dipakai melatih/tuning |
| Baseline, perbandingan, dan metrik | 15 | Tabel, F1, confusion matrix; analisis kelas | Hanya accuracy tunggal |
| Interpretasi ilmiah & keterbatasan | 15 | Membedakan simulasi dan validasi nyata; analisis kegagalan | Generalisasi tanpa bukti |
| Reproducibility dan presentasi | 5 | Eksekusi ulang, tampilan, sitasi rapi | Notebook gagal dieksekusi |

## Pertanyaan HOTS

1. Model memiliki akurasi 98% tetapi hanya menguji batch iluminasi yang sama dengan data latih. Jelaskan mengapa hasil ini mungkin bias dan rancang evaluasi alternatif.
2. Jika 2% kesalahan terjadi pada inspeksi 200.000 produk per hari, bagaimana menafsirkan dampak operasional? Metrik tambahan apa yang perlu diketahui (false reject/false accept)?
3. Pada citra warna, terjadi perubahan white balance. Susun eksperimen yang memisahkan perubahan material dari perubahan pencahayaan.
4. Jelaskan kapan simple threshold + regionprops lebih tepat dibanding CNN, ditinjau dari transparansi, biaya data, dan variasi scene.
5. Apa bukti minimum yang Anda perlukan sebelum menyebut model layak untuk sistem riil? Rancang protokol uji dan acceptance criteria yang dapat diaudit.

**Integritas akademik:** mahasiswa harus menjelaskan semua hasil dan bertanggung jawab atas kebenaran kode, sumber data, dan penggunaan bantuan AI. Tidak boleh menyatakan dataset sintetis sebagai data industri/medis nyata.
