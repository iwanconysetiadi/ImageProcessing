# Modul Teori: Pengolahan Citra Digital dan Pembelajaran Mesin

Dokumen ini adalah pendamping teoretis notebook praktikum. Fokusnya bukan hafalan fungsi pustaka, melainkan **bagaimana sistem pencitraan menghasilkan data, mengapa algoritma dapat berhasil atau gagal, dan bagaimana kesimpulan diuji secara ilmiah**. Cocok sebagai bahan bacaan mahasiswa S1 Teknik Fisika dan bidang serumpun.

## 1. Dari cahaya menuju citra digital

Kamera tidak mengukur “warna objek” secara langsung. Pada titik ruang tertentu, respons sensor ditentukan oleh radiansi spektral, karakteristik lensa, respons spektral kanal, waktu integrasi, dan penguatan elektronika. Sebuah model yang disederhanakan untuk kanal ke-$k$ ialah

\[
y_k(r,c)=g_k\int_{\lambda} L(r,c,\lambda)q_k(\lambda)\,\mathrm d\lambda+n_k(r,c),
\]

di mana $y_k$ adalah sinyal sensor terkode, $g_k$ penguatan, $L$ radiansi yang diterima, $q_k$ respons sensor-kanal terhadap panjang gelombang, dan $n_k$ noise. Persamaan ini menegaskan bahwa nilai RGB mentah dipengaruhi sumber cahaya dan kamera, bukan material saja. Hubungan tersebut sering kali nonlinier setelah gamma correction, demosaicing, tone mapping, dan kompresi JPEG.

Pencitraan juga memiliki sifat *spatial averaging*: objek ideal dikonvolusikan oleh *point spread function* (PSF), lalu disampling oleh kisi piksel. Representasi singkat untuk satu kanal adalah

\[
I_{\mathrm{ukur}}[r,c] \approx \mathcal Q\left\{\big(h*I_{\mathrm{ideal}}\big)(r\Delta y,c\Delta x)+\eta[r,c]\right\},
\]

dengan $h$ PSF, $*$ konvolusi, $\Delta x,\Delta y$ pitch sampling pada bidang yang relevan, $\eta$ noise, dan $\mathcal Q$ operasi kuantisasi. Model ini memiliki asumsi penting: geometri statis, sistem relatif linear dalam rentang intensitas kerja, dan pencahayaan berubah cukup lambat selama exposure.

**Implikasi engineering:** ketika objek cacat berukuran dua piksel, menambah algoritma ML tidak bisa memulihkan informasi yang tidak direkam. Diperlukan peninjauan magnifikasi, depth of field, MTF, motion blur, pencahayaan, dan resolusi efektif.

**Mini-pertanyaan:** sebuah inspeksi gagal karena refleksi spekular. Mengapa menaikkan resolusi kamera saja belum tentu membantu? Bagaimana opsi polarisasi silang atau pencahayaan difus dapat mengubah sinyal yang diterima?

## 2. Sampling, resolusi, dan kuantisasi

**Sampling spasial** mengambil nilai fungsi di koordinat diskret. Untuk pola periodik dengan frekuensi spasial $f_x$ (siklus/mm), sampling dengan frekuensi $f_s=1/\Delta x$ mesti memenuhi $f_s>2f_{\mathrm{maks}}$ untuk mencegah aliasing pada sistem ideal. Pada citra nyata, optical low-pass filtering, PSF, dan ukuran bukaan piksel menentukan bagaimana frekuensi tinggi dilemahkan.

Jika panjang lintang gambar yang diamati adalah $W$ mm dan ada $N$ piksel efektif, skala nominalnya $s=W/N$ mm/piksel. Untuk luas yang dibentuk oleh $A_{px}$ piksel, maka $A\simeq A_{px}s_xs_y$. Namun $s$ perlu kalibrasi menggunakan objek standar bila ada distorsi lensa dan perspektif. **Jumlah piksel tidak sama dengan ketidakpastian geometris**, terutama ketika threshold, blur, atau fokus menggeser batas objek.

**Kuantisasi intensitas** $b$ bit ideal mempunyai $L=2^b$ level. Dengan interval input $[0,1]$, langkah kuantisasi rata-rata $\Delta=1/(L-1)$. Jika error kuantisasi didekati uniform dan tidak berkorelasi terhadap sinyal, varians error $\sigma_q^2\approx \Delta^2/12$. Asumsi ini tidak selalu berlaku pada citra gelap atau bertekstur rendah.

Contoh `uint8`: operasi pengurangan antara dua angka unsigned dapat *wrap around* bila tidak dilakukan konversi yang tepat. Karena itu normalisasi ke `float32`/`float64` perlu menjadi keputusan sadar, bukan sekadar ritual teknis.

**Diskusi:** uji sampling dua citra dengan frekuensi pola berbeda; bandingkan *nearest neighbor*, bilinear, dan interpolasi yang memakai anti-aliasing. Apa konsekuensinya bila pengukuran dimensi dilakukan setelah resampling?

## 3. Histogram, kontras, dan transformasi intensitas

Histogram $h(k)$ menghitung jumlah piksel pada tingkat intensitas $k$. Histogram ternormalisasi $p(k)=h(k)/N$ dapat diperlakukan sebagai estimasi distribusi empirik piksel, bukan distribusi objek fisik. Untuk citra dengan rentang sempit, perentangan intensitas dapat memperbesar jarak numerik antar-level, tetapi tidak menciptakan informasi baru.

Pada histogram equalization, transformasi diskret didasarkan pada *cumulative distribution function* (CDF):

\[
T(k)=(L-1)\sum_{j=0}^{k}p(j).
\]

Metode ini mengubah distribusi keseluruhan. Bila sebuah area gelap penting tetapi hanya menempati sebagian kecil gambar, perubahan histogram global dapat menghasilkan kontras yang tidak diinginkan. **CLAHE** membagi gambar ke area lokal, menahan pertumbuhan histogram berlebih dengan *clip limit*, lalu menginterpolasi peta intensitas antarwilayah. Hasil yang tampak lebih jelas bagi manusia belum tentu lebih baik untuk fitur ML.

**Pengujian yang benar:** buat variasi iluminasi dan noise, jalankan histogram/CLAHE dengan parameter berbeda, lalu ukur efeknya pada metrik tugas akhir (misalnya F1 untuk klasifikasi) di **test yang tetap**. Jangan menilai hanya dari kesan visual satu contoh.

## 4. Noise, blur, dan filter spasial

Noise pada sensor terdiri atas berbagai komponen: **shot noise** yang sering didekati Poisson untuk jumlah foton, **read noise** akibat elektronika, **dark current** dan fixed-pattern noise, serta gangguan akuisisi lainnya. Model Gaussian aditif

\[
I_{\mathrm{obs}}=I_{\mathrm{ideal}}+\eta,\qquad \eta\sim \mathcal N(0,\sigma^2)
\]

adalah titik awal yang berguna, tetapi bukan hukum universal semua kamera. Untuk simulasi citra, catat apakah clipping dan normalisasi dilakukan sebelum atau setelah noise.

Konvolusi citra dengan kernel $K$ ialah

\[
(I*K)[r,c]=\sum_m\sum_n I[r-m,c-n]K[m,n].
\]

Filter Gaussian menggunakan kernel halus dengan bobot jarak dari pusat; ia baik untuk noise frekuensi tinggi namun meredam tepi. Median filter menggunakan median piksel tetangga; sifatnya nonlinier dan sering efektif menghilangkan noise impuls. Ukuran kernel lebih besar biasanya mengurangi noise namun menghapus detail objek kecil.

**PSNR**, untuk skala puncak $MAX_I$, didefinisikan sebagai

\[
\mathrm{PSNR}=10\log_{10}\left(\frac{MAX_I^2}{\mathrm{MSE}}\right),\quad
\mathrm{MSE}=\frac{1}{MN}\sum_{r,c}(I_{\mathrm{ref}}[r,c]-I_{\mathrm{hasil}}[r,c])^2.
\]

PSNR memerlukan referensi; pengukuran satu citra tanpa citra ideal tidak secara otomatis menghasilkan PSNR yang bermakna. **SSIM** mengevaluasi pola kemiripan lokal namun tetap memerlukan referensi. Keduanya tidak langsung menyatakan kualitas diagnostik atau mutu kontrol produk.

**Eksperimen:** pertahankan citra dan random seed yang sama, ubah $\sigma$ filter, ukur PSNR/SSIM, lalu uji perubahan ketajaman batas objek. Jelaskan mengapa titik terbaik bergantung tugas.

## 5. Deteksi tepi dan morfologi

Gradien citra adalah

\[
\nabla I = \left(\frac{\partial I}{\partial x},\frac{\partial I}{\partial y}\right),\quad
|\nabla I|=\sqrt{I_x^2+I_y^2}.
\]

Operator Sobel memberi taksiran gradien diskret setelah perataan sederhana. Canny lazim melibatkan smoothing, gradien, non-maximum suppression, dan hysteresis threshold. **Batas tepi citra bukan selalu batas benda:** perubahan reflektansi permukaan, bayangan, dan tekstur juga membuat gradien kuat.

Pada citra biner, **erosi** mengecilkan wilayah foreground menurut elemen struktur, sedangkan **dilasi** memperluasnya. *Opening* (erosi lalu dilasi) dapat menghilangkan komponen kecil; *closing* (dilasi lalu erosi) dapat menutup celah. Hasil berubah menurut bentuk dan radius elemen struktur. Objek yang relevan secara fisik bisa ikut hilang jika ukuran elemen terlalu besar.

**Studi kasus:** mendeteksi goresan pada pelat logam. Cahaya miring mungkin memperbesar gradien goresan, tetapi juga membuat refleksi. Rancang eksperimen yang memisahkan goresan dari bayangan akibat sudut iluminasi.

## 6. Segmentasi dan metrologi berbasis citra

Segmentasi memberi label piksel/region. **Global Otsu** memilih ambang yang memaksimalkan pemisahan antar-kelompok intensitas; asumsi implisitnya gambar memiliki kelompok statistik yang cukup terpisah. Pada pencahayaan tak homogen, satu threshold global dapat merusak topologi objek.

Setelah segmentasi, `connected components` memisahkan region sesuai konektivitas. Statistik `area`, `centroid`, `perimeter`, `eccentricity`, dan `solidity` membantu ekstraksi fitur. Circularity sering ditulis

\[
C=\frac{4\pi A}{P^2},
\]

di mana $A$ luas region dan $P$ keliling. Bentuk lingkaran ideal mempunyai $C=1$, tetapi estimasi diskret dapat menyimpang tergantung definisi perimeter dan resolusi. Karena itu algoritma dan satuan harus dicatat.

**Ketidakpastian area:** bila objek dianalisis pada skala $s$ mm/piksel dan terdapat ketidakpastian $u_s$ serta $u_{A_{px}}$, pendekatan propagasi orde pertama untuk $A=A_{px}s^2$ ialah

\[
\left(\frac{u_A}{A}\right)^2\approx\left(\frac{u_{A_{px}}}{A_{px}}\right)^2+
4\left(\frac{u_s}{s}\right)^2,
\]

asalkan ketidakpastian dianggap tak berkorelasi. Pada kenyataannya threshold, fokus, distorsi lensa, dan kalibrasi bisa berkorelasi; formula perlu disesuaikan.

**Pertanyaan HOTS:** dua eksperimen menggunakan kamera berbeda tetapi area objek sama dalam piksel. Apakah diameter fisiknya pasti sama? Sebutkan tiga data yang perlu diketahui.

## 7. FFT 2-D dan domain frekuensi

Transformasi Fourier diskret 2-D mengubah representasi posisi piksel ke frekuensi spasial:

\[
F[u,v]=\sum_{r=0}^{M-1}\sum_{c=0}^{N-1}I[r,c]
\exp\left[-j2\pi\left(\frac{ur}{M}+\frac{vc}{N}\right)\right].
\]

Komponen berfrekuensi rendah biasanya berasosiasi dengan variasi intensitas lambat; frekuensi tinggi dengan transisi cepat, termasuk tepi, tekstur, dan noise. `fftshift` memusatkan frekuensi nol untuk visualisasi. Spektrum magnitudo biasanya diplot pada skala log karena *dynamic range* sangat besar.

Filter domain frekuensi bekerja sebagai perkalian $G[u,v]=H[u,v]F[u,v]$, setara konvolusi tertentu pada domain spasial jika penanganan batas dan kondisi transformasi sesuai. *Low-pass* Gaussian menghaluskan gambar; *high-pass* menonjolkan detail cepat. Filter ideal dengan cutoff sangat tajam dapat menyebabkan ringing (*Gibbs phenomenon*).

**Eksperimen:** tambahkan pola kisi periodik pada citra, lihat dua puncak spektrum simetris, lalu rancang notch filter. Jelaskan konsekuensi jika frekuensi noise tumpang tindih dengan fitur objek.

## 8. Warna, ruang warna, dan kalibrasi

Nilai RGB dibatasi karakteristik iluminan, sensor, exposure, proses demosaicing, dan *tone curve*. Perbedaan RGB mentah antarhari belum cukup sebagai bukti perubahan objek. **Chromaticity sederhana** dapat dibentuk sebagai

\[
r=\frac{R}{R+G+B},\quad g=\frac{G}{R+G+B},\quad b=\frac{B}{R+G+B},
\]

dengan syarat penjumlahan kanal tidak nol. Rasio ini mengurangi pengaruh perubahan exposure skalar yang sama pada semua kanal, tetapi tidak menjamin invariansi terhadap *color cast*, clipping, atau respons kamera nonlinier.

HSV mengubah koordinat warna agar hue/saturation/value lebih mudah dikelola untuk sejumlah tugas. CIELAB digunakan dalam pengukuran warna berbasis standar, tetapi konversi yang benar bergantung definisi ruang asal, *white point*, dan color management. Penggunaan nilai $\Delta E$ memerlukan alur kalibrasi yang tepat; sekadar menghitung jarak dari RGB kamera bukan kolorimetri tervalidasi.

**Koreksi gray patch** dalam notebook 11 menggunakan gain kanal $g_R=R_{\mathrm{target}}/R_{\mathrm{ref}}$ dan analog untuk kanal lain. Perubahan ini merupakan ilustrasi *white balance* diagonal, bukan solusi universal untuk kalibrasi spektral kamera. Penelitian yang lebih serius memerlukan kartu target bersertifikat, iluminan terkontrol, ROI terstandar, raw capture jika dimungkinkan, pengaturan terkunci, serta ketidakpastian.

**Pertanyaan:** mengapa sumber LED berbeda dapat menghasilkan nilai RGB berbeda meskipun lux nominal sama? Apa batas informasi yang dapat diberikan oleh ukuran lux dibanding distribusi spektral?

## 9. Feature engineering: bentuk, intensitas, tekstur, HOG

Sebelum deep learning, sejumlah sistem vision banyak mengandalkan **handcrafted features**: luas objek, perimeter, sirkularitas, intensitas dan simpangan baku, distribusi tepi, LBP, HOG, dan sebagainya. Fitur yang tepat bergantung mekanisme kerusakan yang ingin dideteksi; tidak semua fitur berguna bagi seluruh cacat.

**HOG** mengestimasi gradien, membagi citra dalam sel, membentuk histogram orientasi, menormalisasi kelompok sel, lalu merangkainya menjadi vektor. Perubahan `pixels_per_cell` dan `cells_per_block` memengaruhi resolusi deskriptor, stabilitas, dan jumlah dimensi. Jika sebuah objek sangat kecil, ukuran sel terlalu besar bisa menghilangkan pola penting.

Keunggulan fitur manual adalah **transparansi** dan dapat bekerja pada data relatif kecil, sedangkan keterbatasannya adalah ketergantungan pada preprocessing, orientasi, dan variasi dunia nyata. Jangan menganggap fitur berkoefisien besar di regresi logistik sebagai sebab fisik tanpa pengujian dan analisis korelasi.

**Ablasi** berarti mematikan subset fitur secara terencana untuk memperkirakan kontribusinya pada evaluasi. Lakukan pemilihan fitur di **train** atau validasi yang benar; jika Anda terus mengubah fitur berdasarkan test, test telah menjadi bagian dari prosedur pengembangan model.

## 10. Machine learning: alur yang valid

### 10.1 Mulai dari pertanyaan ilmiah

Tentukan target yang dapat diperiksa oleh pihak independen: klasifikasi angka, label cacat berdasarkan aturan inspeksi, atau label warna. Tulis keputusan bisnis/fisik terkait false positive dan false negative. Tentukan apakah unit generalisasi adalah **gambar, objek, sesi pengambilan, perangkat, atau lokasi**.

### 10.2 Bagi data sebelum mempelajari statistiknya

Pada pembagian acak per-gambar, beberapa frame yang diambil dari benda/sesi sama dapat muncul di train dan test. Kualitas yang tampak sangat tinggi bisa berasal dari kebocoran faktor akuisisi. Gunakan `GroupShuffleSplit` atau `GroupKFold` ketika gambar memiliki struktur kelompok yang tidak boleh tumpang tindih.

**Pipeline** scikit-learn menggabungkan transformasi dan estimator. Contohnya `make_pipeline(StandardScaler(), LogisticRegression(...))`: mean dan simpangan baku data normalisasi dipelajari pada subset train ketika `fit` dipanggil; bukan pada seluruh data sebelum split.

### 10.3 Baseline dan evaluasi

Kelas mayoritas merupakan baseline minimum. Untuk kelas positif, definisikan

\[
\mathrm{Precision}=\frac{TP}{TP+FP},\qquad
\mathrm{Recall}=\frac{TP}{TP+FN},\qquad
F_1=\frac{2PR}{P+R}.
\]

Pada multi-kelas, `macro-F1` adalah rata-rata F1 masing-masing kelas. Ia berguna ketika kepedulian terhadap setiap kelas serupa, walaupun kebijakan biaya kesalahan yang nyata bisa berbeda. `Confusion matrix` memperlihatkan jenis kesalahan. Accuracy saja dapat menutupi kegagalan kelas minoritas.

Untuk pemilihan hiperparameter, gunakan validasi atau cross-validation hanya pada train. **Test sebaiknya diperlakukan sekali sebagai evaluasi final**. Ketika data diperbarui, tetapkan protokol uji ulang yang didokumentasikan.

### 10.4 Robustitas dan ketidakpastian

Untuk sistem vision nyata, ubah intensitas, white balance, blur, noise, ukuran, rotasi, latar, atau perangkat. Uji kelompok kondisi baru (*domain shift*). Kepercayaan model (*confidence*) tidak otomatis merupakan probabilitas yang terkalibrasi. Jika sistem berisiko tinggi, rancang mekanisme *reject/abstain*, peninjauan manusia, alarm, logging, dan audit berkala.

## 11. Studi kasus terarah

### 11.1 Angka tulisan tangan (notebook 09)

**Pertanyaan:** apakah perancangan fitur HOG memperbaiki generalisasi dibanding vektor piksel? Mulai dari citra `load_digits` berukuran $8\times8$. Gunakan split stratified dan baseline regresi logistik. Bandingkan HOG+SVM pada test yang sama, ukur macro-F1, tampilkan kesalahan, serta uji rotasi ringan. Perhatikan bahwa hasil bisa berbeda karena HOG pada citra sekecil 8×8 tidak selalu unggul.

**Batas inferensi:** dataset ini bukan sampel acak seluruh kemungkinan gaya tulisan tangan, kondisi sensor, dan populasi pengguna. Model yang baik pada dataset tersebut bisa gagal pada foto smartphone asli.

### 11.2 Inspeksi tablet sintetis (notebook 10)

**Pertanyaan:** dapatkah fitur bentuk dan intensitas membedakan tablet utuh dan cacat yang disimulasikan? Citra grayscale dibuat dengan variasi posisi, radius, intensitas antarbatches, retak gelap, atau tepi terkelupas. Ekstrak beberapa fitur interpretabel dan buat pemisahan data per batch. Bandingkan model logistik, model mayoritas, serta fitur bentuk saja. Bahas apakah tingginya metrik lebih banyak mengukur kemampuan menemukan *artefak generator* ketimbang kemampuan produksi nyata.

**Lanjutan penelitian:** bangun dataset tablet asli dengan foto berbagai orientasi, lot produksi, batch pencahayaan, alat, operator, dan tipe cacat. Bentuk protokol ground truth dengan inspector independen dan ketidaksepakatan antarpenilai. Kalibrasi skala, eksposur, dan traceability. Validasi false acceptance terhadap spesifikasi mutu dan biaya kesalahan.

### 11.3 Klasifikasi warna dengan patch abu-abu (notebook 11)

**Pertanyaan:** apakah koreksi referensi meningkatkan hasil pada kondisi lampu yang tak terlihat saat training? Simulator menghasilkan kelas dengan warna nominal berbeda dan gain RGB antarbatches. Uji fitur raw dan fitur terkoreksi pada batch yang identik. Laporkan *per-batch accuracy*, bukan hanya rerata. Hasil dipengaruhi asumsi model simulasi yang sengaja sederhana.

**Lanjutan penelitian:** gunakan objek/color chart nyata dengan pengendalian eksposur, iluminan, ColorChecker, geometrical ROI, capture RAW jika tersedia, randomisasi urutan sesi, serta pengukuran ulangan. Bedakan label kategori dari ukuran warna kontinu. Sebelum memakai $\Delta E_{00}$, definisikan prosedur color management dan uncertainty budget.

## 12. Cara menulis laporan ilmiah mini

Sebuah laporan 6–8 halaman yang baik berisi: **(a)** pertanyaan dan hipotesis yang dapat diuji; **(b)** sumber data, kelas, ukuran, batasan; **(c)** model pembentukan citra yang relevan; **(d)** skema preprocessing dan metode ML; **(e)** train/validation/test dengan penjelasan grouping; **(f)** baseline, grafik, confusion matrix, dan F1; **(g)** error analysis dan ablasi; **(h)** interpretasi mekanisme; **(i)** keterbatasan dan rencana validasi pada data dunia nyata.

Jangan menggunakan kalimat “algoritma terbukti bekerja di lapangan” ketika eksperimen hanya menggunakan data simulasi. Nyatakan ukuran sampel dan uncertainty sebelum menyebut peningkatan secara signifikan. Jelaskan apa yang tidak dapat ditafsirkan dari data. Kualitas laporan terutama dinilai dari argumentasi yang dapat diaudit, bukan banyaknya grafik atau kompleksitas model.

## 13. Bacaan lanjut dan praktik yang disarankan

Urutan membaca: bagian 1–3 sebelum notebook 01–02; bagian 4–6 sebelum notebook 03–05; bagian 7–9 sebelum notebook 06–08; bagian 10–11 sebelum notebook 09–12. Buku referensi dan dokumentasi API ada dalam [REFERENSI](REFERENSI.md). Untuk memperluas ke optik lanjut, kaji PSF, MTF, Bayer demosaicing, radiometri, interferometri, dan metrologi. Untuk ML lanjut, pelajari probabilistic calibration, class imbalance, domain adaptation, interpretability, dan estimasi ketidakpastian.
