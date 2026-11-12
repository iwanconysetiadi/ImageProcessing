# Studi Kasus Teknik Fisika dalam Pengolahan Citra

## 1. Thermography untuk inspeksi material
Kasus ini mempelajari distribusi suhu pada benda uji setelah dipanaskan secara terkontrol. Citra termal digunakan untuk mendeteksi cacat internal, delaminasi, dan non-uniformity temperatur. Dalam konteks Teknik Fisika, fokusnya bukan hanya klasifikasi “baik/buruk”, tetapi juga interpretasi terhadap perubahan termal, difusi panas, dan asumsi model.

### Masalah utama
- bagaimana memisahkan defect dari variasi background?
- bagaimana membedakan efek thermal dari variasi emissivitas?
- bagaimana mengukur kedalaman defect dari respons termal?

### Metode yang umum
- preprocessing termal
- segmentation berdasarkan threshold atau region-based
- ekstraksi fitur suhu dan tekstur
- evaluasi berdasarkan lokasi defect dan ketepatan geometri

---

## 2. Digital Image Correlation (DIC)
DIC merupakan teknik yang memanfaatkan perubahan pola speckle pada permukaan benda untuk mengestimasi pergeseran, deformasi, dan regangan. Dalam konteks sistem fisik, ini adalah salah satu contoh paling kuat bahwa citra adalah data pengukuran.

### Masalah utama
- akurasi tracking poin/area
- sensitivitas terhadap noise dan blur
- pada kondisi apa metode matching gagal?

### Metode yang umum
- pattern tracking
- cross-correlation
- subpixel refinement
- analisis regangan lokal

---

## 3. Electroluminescence sel surya
EL imaging sering digunakan untuk inspeksi sel surya. Citra EL dapat menampilkan microcrack, hotspot, maupun ketidakseragaman respons listrik. Studi ini cocok untuk membandingkan metode berbasis fitur dan metode pembelajaran mesin.

### Masalah utama
- mengidentifikasi defect dengan resolusi tinggi
- membedakan microcrack dari noise sensor
- mengukur kualitas modul secara objektif

---

## 4. Karakterisasi mikrostruktur material
Karakterisasi material dapat dilakukan dengan citra mikroskopi, SEM, atau pencitraan optik dengan berbagai resolusi. Tujuannya bisa berupa analisis struktur, ukuran grain, porositas, atau retakan.

### Masalah utama
- segmentasi struktur dari background
- evaluasi hasil berdasarkan geometri dan tekstur
- memvalidasi metode dengan dataset yang terukur

---

## 5. Metrologi optik
Metrologi optik membahas bagaimana dimensi, bentuk, dan posisi objek diestimasi dari citra. Ini terkait erat dengan kalibrasi, transformasi perspektif, dan ketidakpastian pengukuran.

### Fokus utama
- pemetaan piksel ke satuan panjang
- koreksi geometrik
- evaluasi kesalahan pengukuran
- pendekatan statistik terhadap hasil

---

## Prinsip evaluasi ilmiah
Setiap studi kasus harus menilai:
- apakah model tersebut benar-benar mengukur fenomena atau hanya memprediksi pola visual?
- apakah data train dan test benar-benar dipisahkan?
- apakah ada leakage akibat batch, kamera, atau kondisi eksperimen?
- apa batas penggunaan model?
- apakah hasil dapat direproduksi?

---

## Pertanyaan yang sering muncul
1. Apakah hasil model cukup valid untuk digunakan pada sistem fisik?
2. Apakah model sensitif terhadap perubahan kondisi akuisisi?
3. Apakah akurasi tinggi memang mencerminkan kualitas pengukuran?
4. Apakah terdapat bias akibat karakteristik sensor atau pencahayaan?
5. Apakah pendekatan yang digunakan benar-benar sesuai dengan fisika fenomena yang diamati?
