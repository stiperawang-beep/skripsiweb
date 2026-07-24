# Master Prompt: Web Presentasi Skripsi 3D Apple-Style

**Tujuan:**
Buatkan saya sebuah presentasi web interaktif (Single Page Application) menggunakan murni **HTML**, **CSS**, dan **Vanilla JavaScript** dengan *framework* **Reveal.js**. Web ini akan digunakan untuk sidang skripsi. 

**Persyaratan Desain (Krusial & Harus 100% Mirip):**
1. **Tema & Estetika (Apple Smooth & Premium):**
   - Gunakan gaya desain **Apple / iOS / macOS modern**. Desain harus terlihat *super clean*, cerah, elegan, futuristik, dan terkesan sangat mahal.
   - Gunakan palet warna Apple: putih bersih (`#ffffff`), abu-abu terang (`#f2f2f7`), teks utama abu-abu gelap kehitaman (`#1d1d1f`), teks sekunder (`#86868b`), serta warna aksen pastel yang tajam (Biru `#007AFF`, Ungu `#AF52DE`, Pink `#FF2D55`, Orange `#FF9500`, Hijau `#34C759`).
   - Gunakan font **'Inter'** (impor dari Google Fonts) atau `-apple-system`.

2. **Efek 3D & Glassmorphism (Sangat Penting):**
   - Semua *container* utama harus menggunakan gaya **Bento Grid** (kotak-kotak bersudut melengkung halus `border-radius: 30px`).
   - Gunakan efek **Glassmorphism**: latar belakang kotak semi-transparan (`rgba(255, 255, 255, 0.65)`), efek blur yang kuat (`backdrop-filter: blur(25px)`), border putih tipis (`border: 1px solid rgba(255,255,255,0.8)`), dan bayangan jatuh yang halus (`box-shadow: 0 10px 40px rgba(0,0,0,0.06)`).
   - Terapkan **3D Hover Tilt Effect**: Saat kursor digerakkan di atas *bento box*, kotak tersebut harus sedikit miring ke arah kursor menggunakan properti CSS `transform: rotateX()` dan `rotateY()` (dikendalikan via JavaScript `mousemove`).
   - Terapkan efek elevasi 3D pada elemen dalam kotak saat *hover* (`transform: translateZ(30px)`).

3. **Latar Belakang (Animated Glowing Orbs):**
   - Background utama berwarna krem/abu sangat terang.
   - Tambahkan 3-4 bola gradien (*orbs*) berukuran besar (sekitar 600px - 800px) yang ditempatkan dengan posisi absolut di belakang konten (`z-index: -1`).
   - Berikan warna gradien mencolok pada bola tersebut (misal: campuran biru-ungu, pink-orange, cyan).
   - Beri efek *blur* ekstrem pada bola tersebut (`filter: blur(120px)`) agar tampak seperti pendaran cahaya (*glow*).
   - Buat bola-bola tersebut bergerak lambat mengambang naik turun menggunakan CSS `@keyframes`.

4. **Struktur Layout & Grid:**
   - Gunakan CSS Grid untuk membuat sistem Bento Box.
   - Buat utilitas class: `.bento-grid-2` (2 kolom), `.bento-grid-3` (3 kolom), `.bento-grid-4` (4 kolom).
   - Pastikan *gap* antar kotak adalah 30px.

5. **Responsivitas Sempurna (Multi-Device):**
   - Konfigurasi Reveal.js harus di-*set* *fluid*: `width: '100%', height: '100%', margin: 0, minScale: 1, maxScale: 1`.
   - Tambahkan `@media (max-width: 768px)` untuk memastikan di layar HP semua Bento Grid berubah menjadi 1 kolom (`grid-template-columns: 1fr`).
   - Tambahkan `overflow-y: auto;` pada slide saat di HP agar konten yang panjang bisa digulir ke bawah secara vertikal.
   - Tabel harus dibungkus dalam `.table-3d-wrapper` dengan `overflow-x: auto` agar bisa di-*swipe* ke samping di HP tanpa merusak *layout*.

6. **Komponen Visual Khusus:**
   - **Tabel Apple Style:** Tabel dengan desain minimalis, tanpa garis vertikal, baris tabel bergantian warna tipis (*zebra-striping* super tipis), *header* di-bold warna redup, serta sudut melengkung.
   - **Stat Ring 3D:** Buat lingkaran SVG progres/persentase (*donut chart*) menggunakan `<circle>` dengan *stroke-dasharray* dan *linearGradient* tebal yang seolah melayang (`filter: drop-shadow`). Angka persentase besar di tengahnya menggunakan *font-weight: 900*.
   - **Tombol/Badge 3D:** Label atau lencana kecil dengan efek gradien warna, teks putih, border tipis, dan *box-shadow*.
   - **Lightbox Image:** Setiap gambar harus memiliki kelas/fungsi klik yang saat ditekan akan memunculkan gambar penuh di layar depan dengan efek *overlay* gelap dan transisi *zoom in*.

7. **Konten Penelitian (Teori & Kesimpulan Ilmiah):**
   - Saat menyajikan hasil SPSS (Validitas, Reliabilitas, Normalitas, Regresi, Determinasi), buatlah dua kotak khusus yang saling terhubung:
     1. **Theory Box**: Kotak bergradasi tipis biru/ungu dengan *border-left* tebal. Harus menyertakan "Dasar Teori" dan "Cara Membaca" yang mencantumkan nama pakar (misal: *Sugiyono, 2019* atau *Ghozali, 2018*).
     2. **Conclusion Box**: Kotak bergradasi hijau tipis dengan *border-left* hijau tebal. Berisi interpretasi dari angka statistik secara formal (misal: "$H_1$ diterima karena $t_{hitung} > t_{tabel}$").

8. **Animasi Masuk (Entry Animations):**
   - Jangan gunakan transisi bawaan Reveal.js (`transition: 'none'`).
   - Buat kelas CSS animasi 3D sendiri:
     - `.anim-3d-slide-r`: Masuk dari kanan sambil berputar 3D (sumbu Y).
     - `.anim-3d-flip`: Terbuka dari bawah ke atas seperti lipatan kertas.
     - `.anim-3d-pop`: Membesar dari skala 0 (efek *spring*).
   - Gunakan atribut `data-auto-animate` dari Reveal.js antar slide untuk memperhalus perpindahan elemen.

**Instruksi Akhir untuk AI:**
Tuliskan semua kode (HTML, CSS, JS) dalam satu *file* tunggal yang rapi dan terstruktur (Inline CSS dan Inline JS). Gunakan ikon dari **Remix Icon** (via CDN). Jangan berikan *placeholder*; tuliskan struktur kode yang fungsional, estetik, responsif, dan mencakup interaktivitas 3D *mousemove* secara presisi. Desain akhir harus memukau, membuat orang yang melihatnya berdecak kagum!
