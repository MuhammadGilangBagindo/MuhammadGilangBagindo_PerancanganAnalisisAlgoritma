def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k-1) % n + 1

# Contoh penggunaan
n = 7 # Jumlah orang dalam lingkaran
k = 3 # Jumlah orang yang harus dilewati sebelum satu orang dieliminasi

print("Posisi orang terakhir yang tersisa adalah ", josephus(n, k))