import os
import re
import time
import threading
import itertools
from pathlib import Path

# ================================
# 🔧 KONFIGURASI
# ================================
# Ubah nilai di bawah ini untuk mengatur folder target Anda.
FOLDER_TARGET_PATH = r'F:\Codingan\Ubah Ekstensi File\Target\luzziimom'

# Konversi string path menjadi objek Path
try:
    FOLDER_TARGET = Path(FOLDER_TARGET_PATH)
except TypeError as e:
    print(f"❌ Kesalahan pada jalur folder: {e}. Pastikan format string benar.")
    exit()

DEFAULT_IMG_EXT = '.jpg'
MOVE_TO_VIDEO_FOLDER = True

VIDEO_EXTS = {
    'mp4', 'mkv', 'avi', 'mov', 'wmv', 'flv',
    'mpeg', 'mpg', '3gp', 'webm', 'm4v', 'ts', 'm2ts', 'ogv'
}
KEEP_GIF_AS_GIF = True

LOGO_ASCII = """
    ███████╗██╗██╗     ██╗██╗  ██╗
    ██╔════╝██║██║     ██║██║  ██║
    █████╗  ██║██║     ██║███████║
    ██╔══╝  ██║██║     ██║██╔══██║
    ██║     ██║███████╗██║██║  ██║
    ╚═╝     ╚═╝╚══════╝╚═╝╚═╝  ╚═╝
"""

# ================================
# 🧠 POLA "PENYAKIT"
# ================================
POLA_SALAH = re.compile(
    r'^(?P<base>.*?)[._\-\s]*(?P<vext>(?:' + "|".join(VIDEO_EXTS | {'gif'}) + r'))[0-9]*(\.[a-z0-9]+)?$',
    re.IGNORECASE
)

# ================================
# 🛠️ UTILITAS
# ================================
class Spinner:
    """Class untuk menampilkan animasi spinner di terminal."""
    def __init__(self, message="Memproses..."):
        self.spinner = itertools.cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])
        self.message = message
        self.running = False
        self.thread = None

    def _spin(self):
        while self.running:
            print(f"\r{next(self.spinner)} {self.message}", end="", flush=True)
            time.sleep(0.1)

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._spin, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
        print("\r" + " " * (len(self.message) + 2) + "\r", end="", flush=True)

def log(ikon, pesan):
    """Fungsi sederhana untuk mencetak pesan log."""
    print(f"{ikon} {pesan}")

def buat_nama_unik(jalur_baru: Path) -> Path:
    """Membuat jalur file unik jika sudah ada file dengan nama yang sama."""
    if not jalur_baru.exists():
        return jalur_baru
    
    base = jalur_baru.stem
    ext = jalur_baru.suffix
    counter = 1
    while True:
        kandidat_baru = jalur_baru.with_name(f"{base}_{counter}{ext}")
        if not kandidat_baru.exists():
            return kandidat_baru
        counter += 1

def update_progress_bar(progress, total, bar_length=40):
    """Menampilkan progress bar persentase di terminal."""
    percent = (progress / total)
    filled_length = int(bar_length * percent)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f"\rProgress: [{bar}] {percent:.0%} selesai", end="", flush=True)

# ================================
# 🚀 PROSES UTAMA
# ================================
def ubah_ekstensi(folder: Path, ekstensi_default: str, pindah_video: bool):
    """
    Mengubah ekstensi file dan memindahkannya ke folder yang sesuai.
    """
    if not folder.is_dir():
        log("❌", f"Direktori tidak ditemukan: {folder}")
        return

    log("🔍", f"Memulai pemindaian di: {folder}")
    
    if pindah_video:
        video_folder = folder / "video"
        try:
            if not video_folder.exists():
                os.makedirs(video_folder)
                log("📁", f"Folder 'video' telah dibuat di: {video_folder}")
        except OSError as e:
            log("❌", f"Gagal membuat folder 'video': {e}")
            video_folder = None
    else:
        video_folder = None
    
    # Mulai animasi spinner saat memindai file
    spinner = Spinner(message="Memindai file...")
    spinner.start()

    # Dapatkan daftar file untuk diproses
    file_list = [f for f in folder.rglob('*') if f.is_file() and (not video_folder or f.parent != video_folder)]
    total_files = len(file_list)
    
    spinner.stop()
    print() # Pindah ke baris baru setelah spinner selesai

    if not file_list:
        log("ℹ️", "Tidak ada file yang ditemukan untuk diproses.")
        log("✨", "Proses selesai.")
        return
    
    log("📊", f"Ditemukan {total_files} file untuk diproses.")
    
    processed_count = 0
    for file_path in file_list:
        update_progress_bar(processed_count, total_files)
        
        nama_file = file_path.name
        nama_baru = None
        is_video = False

        m = POLA_SALAH.fullmatch(nama_file)
        if m:
            base = m.group('base')
            vext = m.group('vext').lower()
            if vext == 'gif' and KEEP_GIF_AS_GIF:
                nama_baru = f"{base}.gif"
            else:
                nama_baru = f"{base}.mp4"
                is_video = True
            
        if not nama_baru:
            ext = file_path.suffix.lower().lstrip('.')
            base = file_path.stem

            if ext in VIDEO_EXTS:
                nama_baru = f"{base}.mp4"
                is_video = True
            elif ext == "gif" and KEEP_GIF_AS_GIF:
                nama_baru = f"{base}.gif"
            else:
                nama_baru = f"{base}{ekstensi_default}"

        if nama_baru == nama_file and (not is_video or not pindah_video):
            processed_count += 1
            continue
        
        if is_video and pindah_video and video_folder:
            target_folder = video_folder
        else:
            target_folder = file_path.parent
        
        jalur_baru = buat_nama_unik(target_folder / nama_baru)
        
        try:
            file_path.rename(jalur_baru)
            log("✅", f"'{nama_file}' → '{jalur_baru.name}'")
        except OSError as e:
            log("❌", f"Gagal mengubah nama '{nama_file}': {e}")
        
        processed_count += 1
        
    update_progress_bar(total_files, total_files) # Update progress bar hingga 100%
    print("\n") # Pindah ke baris baru setelah progress bar selesai
            
    log("✨", "Proses selesai.")

# ================================
# ▶️ EKSEKUSI
# ================================
if __name__ == "__main__":
    ubah_ekstensi(FOLDER_TARGET, DEFAULT_IMG_EXT, MOVE_TO_VIDEO_FOLDER)
    
    # Menambahkan logo, pesan akhir, dan menunggu input pengguna
    print("\n" + LOGO_ASCII)
    print("----------------------------------------------------")
    print("        ✨ Proses Selesai! Terima kasih telah menggunakan skrip ini. 😊")
    print("----------------------------------------------------")
    input("Tekan ENTER untuk keluar...")