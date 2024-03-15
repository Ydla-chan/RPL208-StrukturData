# Inisialisasi array 3x3
data = [
    [123, 124, 126],
    [1, 2, 3],
    [10, 20, 30]
]

# Menampilkan array awal menggunakan loop
print("Array awal:")
for baris in range(0, 3):
    print("data [" + str(baris) + "] =", data[baris])

# Menambahkan elemen baru ke array
data.append([120, 122, 221])

# Menampilkan array setelah dimodifikasi
print("\nArray setelah dimodifikasi:")
# Adjust the range to cover the updated length of the array
for baris in range(0, 4):
    print("data [" + str(baris) + "] =", data[baris])
