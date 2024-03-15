# Inisialisasi array 2 dimensi
data_kumpulan =[ ["PBL-TRPL01", "Aplikasi Survei", "Yeni Rokhayati"],
                 ["PBL-TRPL02","Pengembangan E-SPMI Polibatam ","Iqbal Afif"],
                 ["PBL-TRPL03","Aplikasi Pendaftaran Imunisasi Wajib Balita","Sartikha"],
                 ["PBL-TRPL04","Rancang Bangun Prototipe Aplikas CEISA 4.0 versi dummy untuk dokumen BC 2.0","Metta Sanitputri"],
                 ["PBL-TRPL05","E-Assessment Berbasis Passing Grade","Ahmadi Irmansyah Lubis"]
                 ]

print("list Judul PBL TRPL Semester Ganjil tahun ajaaran 2020 / 2023")
for i, data in enumerate(data_kumpulan):
    print(f"{i+1}. {data[0]} dengan berjudul {data[1]} dengan di kordinator oleh {data[2]}")
