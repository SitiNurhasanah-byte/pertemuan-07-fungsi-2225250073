# Pertemuan 07 Fungsi Python
Nama: Siti Nurhasanah  
NIM: 2225250073
Kelas: 3B

## Tujuan
Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular.

## Cara Menjalankan
python3 praktik/utilitas_matematika.py

## Struktur Fungsi
- **luas_persegi_panjang(p, l)**  
  Parameter: panjang (p), lebar (l)  
  Return: luas persegi panjang  

- **luas_segitiga(a, t)**  
  Parameter: alas (a), tinggi (t)  
  Return: luas segitiga  

- **jumlah_n(n)**  
  Parameter: bilangan bulat n  
  Return: jumlah 1 + 2 + ... + n  
  Validasi: n ≥ 0  

- **faktorial(n)**  
  Parameter: bilangan bulat n  
  Return: hasil faktorial n!  
  Validasi: n ≥ 0  

- **tampilkan_menu()**  
  Tidak memiliki parameter  
  Menampilkan pilihan operasi ke layar  

## Hasil Pengujian
| Fungsi                | Input        | Hasil Diharapkan | Hasil Aktual | Status |
|------------------------|--------------|------------------|--------------|--------|
| luas_persegi_panjang   | p=8, l=5     | 40               | 40           | ✅     |
| luas_segitiga          | a=10, t=6    | 30.0             | 30.0         | ✅     |
| jumlah_n               | n=10         | 55               | 55           | ✅     |
| jumlah_n               | n=100        | 5050             | 5050         | ✅     |
| faktorial              | n=5          | 120              | 120          | ✅     |
| faktorial              | n=0          | 1                | 1            | ✅     |

## Refleksi
Dengan memisahkan program menjadi fungsi-fungsi kecil, kode menjadi lebih modular dan mudah dipahami.  
Contohnya, perhitungan faktorial yang awalnya berupa loop panjang bisa dipanggil cukup dengan `faktorial(n)`.  
Hal ini membuat program utama lebih sederhana, fokus pada alur menu, sementara detail perhitungan ditangani oleh fungsi masing-masing.
