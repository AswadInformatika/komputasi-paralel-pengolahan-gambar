
# Komputasi Paralel pada Pengolahan Gambar

## Identitas Mahasiswa
- Nama: Aswad
- NIM: D0224020
- Kelas: C
- Mata Kuliah: Komputasi Paralel dan Sistem Terdistribusi

## 1. Deskripsi Proyek
Proyek ini merupakan praktikum penerapan komputasi paralel dalam pengolahan gambar menggunakan Python.

Permasalahan yang diangkat adalah pemrosesan banyak gambar yang membutuhkan waktu apabila dilakukan satu per satu.

Untuk menyelesaikan permasalahan tersebut, digunakan dua metode, yaitu komputasi sekuensial dan komputasi paralel.

## 2. Tujuan
- Menerapkan teknik komputasi paralel.
- Mengolah 100 gambar menggunakan Python.
- Membandingkan waktu pemrosesan sekuensial dan paralel.
- Mengukur peningkatan kecepatan menggunakan speedup.

## 3. Teknologi yang Digunakan
- Python 3.12.6
- Pillow 13.0.0
- concurrent.futures.ProcessPoolExecutor
- Visual Studio Code
- Windows 11

## 4. Cara Kerja Program

### Metode Sekuensial
Program memproses gambar satu per satu menggunakan perulangan.

### Metode Paralel
Program membagi pekerjaan pengolahan gambar kepada 4 proses pekerja menggunakan ProcessPoolExecutor.

Setiap gambar diproses dengan tahapan:
1. Membuka gambar.
2. Mengubah format warna menjadi RGB.
3. Mengubah ukuran maksimal menjadi 800 × 600 piksel.
4. Memberikan efek Gaussian Blur.
5. Menyimpan hasil dalam format JPG.

Kedua metode menjalankan operasi pengolahan gambar yang sama.

## 5. Struktur Folder
```text
Komputasi_Paralel_Gambar/
├── gambar_asli/
├── hasil_sekuensial/
├── hasil_paralel/
└── main.py
```

Folder gambar_asli digunakan untuk menyimpan 100 gambar masukan. Kedua folder hasil digunakan untuk menyimpan keluaran program.

## 6. Cara Menjalankan
Pastikan Python sudah terpasang.

Instal library Pillow:
```bash
py -m pip install pillow
```

Masukkan foto JPG atau PNG ke folder gambar_asli, kemudian jalankan:
```bash
py main.py
```

Program akan memproses gambar menggunakan dua metode dan menampilkan perbandingan waktu eksekusi.

## 7. Hasil Pengujian

Pengujian dilakukan terhadap 100 gambar menggunakan 4 pekerja paralel.

| Uji | Sekuensial (detik) | Paralel (detik) | Speedup |
|---|---:|---:|---:|
| 1 | 3.0109 | 0.9628 | 3.13x |
| 2 | 2.3833 | 0.9291 | 2.57x |
| 3 | 2.3884 | 0.8419 | 2.84x |
| 4 | 2.3291 | 0.9323 | 2.50x |
| Rata-rata | 2.5279 | 0.9165 | 2.76x |

Speedup keseluruhan dihitung dari perbandingan rata-rata waktu sekuensial dan paralel.

Hasil menunjukkan bahwa metode paralel lebih cepat pada keempat pengujian, dengan percepatan keseluruhan sekitar 2.76 kali.

Jumlah keluaran telah diperiksa:
- Hasil sekuensial: 100 gambar
- Hasil paralel: 100 gambar

## 8. Kesimpulan
Berdasarkan pengujian, komputasi paralel dapat mempercepat pengolahan 100 gambar dibandingkan metode sekuensial pada komputer yang digunakan.

Pembagian pekerjaan kepada beberapa proses memungkinkan pemanfaatan sumber daya CPU secara bersamaan.

## 9. Disclaimer Penggunaan AI
ChatGPT digunakan sebagai alat bantu dalam menentukan ide proyek, menyusun rancangan kode Python, menjelaskan konsep komputasi paralel, dan menyusun dokumentasi.

Pelaksanaan program, pengujian waktu eksekusi, pemeriksaan jumlah gambar keluaran, dan pengambilan hasil praktikum dilakukan oleh mahasiswa secara mandiri.
