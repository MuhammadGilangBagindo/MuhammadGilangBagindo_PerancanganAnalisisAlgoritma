def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k-1) % n + 1

# Contoh penggunaan
n = int(input('Masukkan jumlah orang dalam lingkaran: ')) # Jumlah orang dalam lingkaran
k = int(input('Masukkan jumlah orang yang harus dilewati sebelum satu orang dieliminasi: ')) #Jumlah orang yang harus
#dilewati sebelum satu orang dieliminasi        

print("Posisi orang terakhir yang tersisa adalah ", josephus(n, k))