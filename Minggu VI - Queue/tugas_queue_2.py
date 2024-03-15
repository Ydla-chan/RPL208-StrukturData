class ClinicQueue:
    def __init__(self):
        self.queue = []
        self.max_capacity = 30

    def add_patient(self, patient_name):
        if len(self.queue) < self.max_capacity:
            self.queue.append(patient_name)
            print(f"{patient_name} telah ditambahkan ke dalam antrian.")
        else:
            print("Antrian sudah penuh, maaf tidak bisa menambahkan pasien.")

    def call_patient(self):
        if self.queue:
            next_patient = self.queue.pop(0)
            print(f"Silakan masuk, {next_patient}!")
        else:
            print("Tidak ada pasien dalam antrian.")

    def display_queue(self):
        if self.queue:
            print("Antrian saat ini:")
            for index, patient in enumerate(self.queue, start=1):
                print(f"{index}. {patient}")
        else:
            print("Antrian kosong.")

def main():
    clinic = ClinicQueue()
    while True:
        print("\nPilihan Menu:")
        print("1. Tambah Pasien")
        print("2. Panggil Pasien")
        print("3. Tampilkan Antrian Pasien")
        print("4. Keluar")
        choice = input("Masukkan pilihan Anda: ")

        if choice == '1':
            patient_name = input("Masukkan nama pasien: ")
            clinic.add_patient(patient_name)
        elif choice == '2':
            clinic.call_patient()
        elif choice == '3':
            clinic.display_queue()
        elif choice == '4':
            print("Terima kasih telah menggunakan layanan kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
