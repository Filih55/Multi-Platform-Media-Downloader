import os

# ================================
# KONFIGURASI
# ================================
# Ganti lokasi folder target di sini
FOLDER_TARGET = r'F:\Codingan\Ubah Ekstensi File\Target\altnf9090\video'

# Ekstensi baru yang diinginkan (misalnya: '.mp4', '.jpg', '.png', dll)
EKSTENSI_BARU = '.mp4'
# ================================


def ubah_ekstensi(folder, ekstensi_baru):
    """Ubah semua file di folder menjadi ekstensi_baru"""
    if not os.path.isdir(folder):
        print(f"Error: Folder tidak ditemukan di {folder}")
        return
    
    for filename in os.listdir(folder):
        old_path = os.path.join(folder, filename)
        if os.path.isfile(old_path):
            name, ext = os.path.splitext(filename)
            if ext.lower() != ekstensi_baru:
                new_path = os.path.join(folder, f"{name}{ekstensi_baru}")
                os.rename(old_path, new_path)
                print(f"Mengubah '{filename}' menjadi '{name}{ekstensi_baru}'")
    print("\nProses selesai.")


if __name__ == "__main__":
    ubah_ekstensi(FOLDER_TARGET, EKSTENSI_BARU)
