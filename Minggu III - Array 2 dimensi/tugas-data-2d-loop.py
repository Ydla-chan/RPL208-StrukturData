# Inisialisasi array 3x3
data = [
    [123, 124, 126],
    [1, 2, 3],
    [10, 20, 30]
]

# Menampilkan array awal menggunakan loop
print("Array awal:")
for baris in range(3):
    for kolom in range(3):
        print("Data [" + str(baris) + "][" + str(kolom) + "] =", data[baris][kolom])

# Menambahkan elemen baru ke array
data.append([120, 122, 221])

# Menampilkan array setelah dimodifikasi
print("\nArray setelah dimodifikasi:")
for baris in range(len(data)):
    for kolom in range(len(data[0])):
        print("Data [" + str(baris) + "][" + str(kolom) + "] =", data[baris][kolom])
