class KeranjangBelanja:
    def __init__(self):
        self.barang = []

    def tambah_barang(self, nama_barang):
        self.barang.append(nama_barang)
        print(f"{nama_barang} ditambahkan ke dalam keranjang belanja.")

    def hapus_barang_terakhir(self):
        if self.barang:
            barang_terhapus = self.barang.pop()
            print(f"{barang_terhapus} dihapus dari keranjang belanja.")
        else:
            print("Keranjang belanja sudah kosong.")

    def lihat_keranjang(self):
        if self.barang:
            print("Isi keranjang belanja:")
            for barang in reversed(self.barang):
                print(" -", barang)
        else:
            print("Keranjang belanja kosong.")

# Contoh penggunaan
keranjang = KeranjangBelanja()

while True:
    print("\nMenu:")
    print("1. Tambah Barang")
    print("2. Hapus Barang Terakhir")
    print("3. Lihat Keranjang")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == "1":
        nama_barang = input("Masukkan nama barang: ")
        keranjang.tambah_barang(nama_barang)
    elif pilihan == "2":
        keranjang.hapus_barang_terakhir()
    elif pilihan == "3":
        keranjang.lihat_keranjang()
    elif pilihan == "4":
        print("Terima kasih. Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan 1, 2, 3, atau 4.")
