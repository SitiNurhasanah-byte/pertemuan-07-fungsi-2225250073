# Program berbasis menu dengan beberapa fungsi matematika sederhana

def luas_persegi_panjang(p, l):
    return p * l

def luas_segitiga(a, t):
    return 0.5 * a * t

def jumlah_n(n):
    if n < 0:
        return None   # validasi: tidak boleh negatif
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def faktorial(n):
    if n < 0:
        return None   # validasi: tidak boleh negatif
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

def tampilkan_menu():
    print("\n=== MENU MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("0. Keluar")

# Program utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (0-4): ")

    if pilihan == "1":
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        print("Luas persegi panjang =", luas_persegi_panjang(p, l))

    elif pilihan == "2":
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        print("Luas segitiga =", luas_segitiga(a, t))

    elif pilihan == "3":
        n = int(input("Masukkan n: "))
        hasil = jumlah_n(n)
        if hasil is None:
            print("Error: n harus bilangan bulat nonnegatif")
        else:
            print(f"Jumlah 1 sampai {n} =", hasil)

    elif pilihan == "4":
        n = int(input("Masukkan n: "))
        hasil = faktorial(n)
        if hasil is None:
            print("Error: n harus bilangan bulat nonnegatif")
        else:
            print(f"{n}! =", hasil)

    elif pilihan == "0":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
