def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Daftar nilai n yang akan diuji
nilai_uji = [1, 5, 10, 100]

print("n\tHasil Fungsi\tRumus n(n+1)/2\tSama?")
print("-" * 45)

for n in nilai_uji:
    hasil_fungsi = jumlah_n(n)
    # Menggunakan integer division (//) agar hasilnya berbentuk integer
    hasil_rumus = n * (n + 1) // 2 
    sama = hasil_fungsi == hasil_rumus
    
    print(f"{n}\t{hasil_fungsi}\t\t{hasil_rumus}\t\t{sama}")