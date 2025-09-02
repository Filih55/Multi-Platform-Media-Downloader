# Gallery-dl
Program Gallery-dl.py ini adalah sebuah wrapper sederhana berbasis Python yang berfungsi untuk mempermudah penggunaan tool gallery-dl (sebuah downloader konten dari berbagai platform seperti Twitter/X, Instagram, dan lain-lain).

📝 Deskripsi Program

Program ini dibuat untuk memberikan antarmuka menu interaktif di terminal agar pengguna dapat lebih mudah menjalankan perintah gallery-dl tanpa harus mengetik manual sintaks panjang.

Menu Utama

Menampilkan logo ASCII dan daftar opsi.

Pengguna dapat memilih platform:

1. X.com (Twitter) → Unduh media dari akun Twitter/X.

2. Instagram.com → Unduh media dari akun Instagram.

3. URL manual → Memasukkan link langsung atau perintah kustom.

4. Keluar → Menghentikan program.

Proses Eksekusi

Program menerima input pengguna (username atau URL).

Membentuk perintah lengkap untuk menjalankan gallery-dl dengan subprocess.run().

Menangani kemungkinan error, seperti:

gallery-dl belum terinstal / tidak ada di PATH.

Username atau URL salah.

Error tak terduga lainnya.

Menu Setelah Unduhan

Setelah perintah selesai, muncul pilihan:

1. Jalankan lagi → Kembali ke menu utama.

2. Keluar → Mengakhiri program.

Penanganan Ctrl+C (SIGINT)

Jika pengguna menekan Ctrl+C, program tidak langsung keluar.

Akan muncul menu konfirmasi: jalankan ulang atau keluar dari program.

=========================================================================================
🎯 interaktif.py

Skrip Python interaktif untuk merapikan file media (gambar & video) dalam sebuah folder.
Program ini akan menormalkan nama & ekstensi file, memindahkan video ke folder khusus, serta memberikan pengalaman interaktif dengan menu sederhana.

Menampilkan logo ASCII saat dijalankan.

Menggunakan ikon dan log status (✅, ❌, 📁, 🔍, dll.) untuk memudahkan pengguna memahami proses.

Ada pesan kesalahan jika path salah atau file gagal diproses.

✨ Fitur Utama

🔍 Pemindaian otomatis semua file dalam folder & sub-folder.

🖼 Normalisasi ekstensi file:

Video → .mp4

GIF → tetap .gif

File lain → default .jpg

📂 Manajemen folder video: semua file video bisa dipindahkan otomatis ke sub-folder video/.

🛡 Cegah duplikasi nama: file yang sama otomatis diberi nomor urut (file.mp4, file_1.mp4, dst.).

📊 Progress bar & animasi spinner untuk status proses.

✅ Menu interaktif: pilih folder lain atau keluar setelah proses selesai.

🎨 Tampilan terminal ramah pengguna dengan logo ASCII & ikon status (✅ ❌ 📁 🔍).

⚙️ Cara Menggunakan

Jalankan skrip:

python interaktif.py


Masukkan path folder yang ingin diproses.

Contoh: C:\Users\Nama\Downloads atau /home/user/Downloads.

Tunggu proses pemindaian & normalisasi selesai.

Pilih apakah ingin memproses folder lain atau keluar dari program.

🔧 Konfigurasi

Beberapa opsi bisa diubah langsung di dalam skrip:

DEFAULT_IMG_EXT = '.jpg' → Ekstensi default untuk file non-video/non-gif.

MOVE_TO_VIDEO_FOLDER = True → Pindahkan video ke folder video/.

KEEP_GIF_AS_GIF = True → Biarkan GIF tetap .gif (jika False, diubah ke .mp4).

VIDEO_EXTS = {...} → Daftar ekstensi video yang dikenali.
