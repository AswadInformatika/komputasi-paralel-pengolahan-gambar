
import os
import time
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from PIL import Image, ImageFilter

# Lokasi folder proyek
folder_utama = Path(__file__).resolve().parent
folder_asli = folder_utama / "gambar_asli"
folder_sekuensial = folder_utama / "hasil_sekuensial"
folder_paralel = folder_utama / "hasil_paralel"

# Membuat folder hasil jika belum tersedia
folder_sekuensial.mkdir(exist_ok=True)
folder_paralel.mkdir(exist_ok=True)


# Fungsi untuk mengolah satu gambar
def proses_gambar(data):
    lokasi_gambar, folder_hasil = data

    with Image.open(lokasi_gambar) as gambar:
        gambar = gambar.convert("RGB")

        # Mengubah ukuran gambar
        gambar.thumbnail((800, 600))

        # Memberikan efek blur
        gambar = gambar.filter(
            ImageFilter.GaussianBlur(radius=2)
        )

        # Menyimpan hasil
        nama = (
            f"{lokasi_gambar.stem}_"
            f"{lokasi_gambar.suffix[1:].lower()}.jpg"
        )
        gambar.save(
            folder_hasil / nama,
            "JPEG",
            quality=85
        )


def main():
    # Mengambil daftar foto
    daftar_gambar = sorted(
        foto for foto in folder_asli.iterdir()
        if foto.suffix.lower() in [".jpg", ".jpeg", ".png"]
    )

    jumlah = len(daftar_gambar)

    print("=== PRAKTIKUM KOMPUTASI PARALEL ===")
    print(f"Jumlah gambar: {jumlah}")

    if jumlah == 0:
        print("Tidak ada gambar di folder gambar_asli!")
        return

    # METODE SEKUENSIAL
    print("\nMemulai pemrosesan sekuensial...")

    mulai = time.perf_counter()

    for foto in daftar_gambar:
        proses_gambar((foto, folder_sekuensial))

    waktu_sekuensial = time.perf_counter() - mulai

    print("Pemrosesan sekuensial selesai!")


    # METODE PARALEL
    print("\nMemulai pemrosesan paralel...")

    jumlah_pekerja = min(4, os.cpu_count() or 1)

    tugas = [
        (foto, folder_paralel)
        for foto in daftar_gambar
    ]

    mulai = time.perf_counter()

    with ProcessPoolExecutor(
        max_workers=jumlah_pekerja
    ) as executor:
        list(executor.map(proses_gambar, tugas))

    waktu_paralel = time.perf_counter() - mulai

    print("Pemrosesan paralel selesai!")


    # HASIL PENGUJIAN
    print("\n=== HASIL PERBANDINGAN ===")
    print(f"Jumlah gambar       : {jumlah}")
    print(f"Jumlah pekerja      : {jumlah_pekerja}")
    print(f"Waktu sekuensial    : {waktu_sekuensial:.4f} detik")
    print(f"Waktu paralel       : {waktu_paralel:.4f} detik")

    if waktu_paralel > 0:
        percepatan = waktu_sekuensial / waktu_paralel
        print(f"Speedup             : {percepatan:.2f}x")

    print("\nPraktikum selesai!")


if __name__ == "__main__":
    main()
