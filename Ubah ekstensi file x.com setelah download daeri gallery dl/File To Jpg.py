import os

# ================================
# KONFIGURASI (UBAH BAGIAN INI SAJA)
# ================================
# Lokasi folder target
FOLDER_TARGET = r'F:\Codingan\Ubah Ekstensi File\Target\xiaruoxi520'

# Ekstensi default untuk file non-video (contoh: '.jpg', '.png')
EKSTENSI_BARU = '.jpg'

# Daftar ekstensi video yang ingin dipaksa jadi .mp4
VIDEO_EXT = ['.mkv', '.avi', '.mov', '.wmv', '.flv', '.mpeg', '.mpg', '.3gp']
# ================================


def buat_nama_unik(folder, nama_baru):
    """Jika nama file sudah ada, tambahkan _1, _2, dst"""
    base, ext = os.path.splitext(nama_baru)
    counter = 1
    nama_final = nama_baru
    while os.path.exists(os.path.join(folder, nama_final)):
        nama_final = f"{base}_{counter}{ext}"
        counter += 1
    return nama_final


def ubah_ekstensi(folder, ekstensi_baru):
    """Mengubah semua file di folder ke ekstensi baru"""
    if not os.path.isdir(folder):
        print(f"❌ Error: Direktori tidak ditemukan - {folder}")
        return
    
    for nama_file in os.listdir(folder):
        jalur_lama = os.path.join(folder, nama_file)

        if os.path.isfile(jalur_lama):
            nama_dasar, ext_lama = os.path.splitext(nama_file)
            ext_lama = ext_lama.lower()

            # Jika sudah sesuai, skip
            if ext_lama == ekstensi_baru.lower() or ext_lama == ".mp4":
                print(f"⏩ Lewati '{nama_file}' (sudah {ext_lama})")
                continue

            # Kalau file video → ubah ke .mp4
            if ext_lama in VIDEO_EXT:
                nama_baru = nama_dasar + ".mp4"
            else:
                # Selain video → ubah sesuai EKSTENSI_BARU
                nama_baru = nama_dasar + ekstensi_baru

            # Pastikan nama unik
            nama_baru = buat_nama_unik(folder, nama_baru)

            jalur_baru = os.path.join(folder, nama_baru)
            os.rename(jalur_lama, jalur_baru)
            print(f"✅ Mengubah '{nama_file}' → '{nama_baru}'")

    print("\n✨ Proses selesai.")


if __name__ == "__main__":
    ubah_ekstensi(FOLDER_TARGET, EKSTENSI_BARU)
