import time

class Parkir:
    def __init__(self):
        self.kendaraan_masuk = {}
        self.tarif_per_detik = 10000  # Rp 10.000 per detik
        self.max_waktu_parkir = 240  # Maksimal waktu parkir adalah 4 menit (240 detik)
        self.denda_1 = 0.10  # Denda 10% untuk parkir lebih dari 4 menit
        self.denda_2 = 0.25  # Denda 25% untuk parkir lebih dari 6 menit
        self.admin_pin = "1234"  # PIN Admin Parkir

    def menu_utama(self):
        while True:
            print("\nMenu Utama:")
            print("1. Masuk Area Parkir")
            print("2. Keluar Area Parkir")
            print("3. Admin Parkir")
            print("4. Keluar")
            pilihan = input("Pilih menu (1/2/3/4): ")

            if pilihan == '1':
                self.masuk_area_parkir()
            elif pilihan == '2':
                self.keluar_area_parkir()
            elif pilihan == '3':
                self.menu_admin_parkir()
            elif pilihan == '4':
                print("Terima kasih. Sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")

    def masuk_area_parkir(self):
        nomor_plat = input("Masukkan nomor plat kendaraan: ")
        waktu_masuk = time.time()
        self.kendaraan_masuk[nomor_plat] = waktu_masuk
        print("Gerbang masuk terbuka. Silahkan masuk.")

    def keluar_area_parkir(self):
        nomor_plat = input("Masukkan nomor plat kendaraan: ")

        if nomor_plat not in self.kendaraan_masuk:
            print("Error: Kendaraan tidak tercatat masuk.")
            return

        waktu_masuk = self.kendaraan_masuk[nomor_plat]
        waktu_keluar = time.time()
        durasi_parkir = waktu_keluar - waktu_masuk

        biaya_parkir = self.hitung_biaya_parkir(durasi_parkir)
        print(f"Biaya parkir: Rp {biaya_parkir:,.2f}")

        nominal_pembayaran = float(input("Masukkan nominal pembayaran: "))
        if nominal_pembayaran < biaya_parkir:
            print("Pembayaran kurang. Silakan masukkan nominal yang cukup.")
        else:
            kembalian = nominal_pembayaran - biaya_parkir
            print(f"Kembalian: Rp {kembalian:,.2f}")
            del self.kendaraan_masuk[nomor_plat]
            print("Gerbang keluar terbuka. Terima kasih!")

    def hitung_biaya_parkir(self, durasi_parkir):
        durasi_parkir_detik = int(durasi_parkir)
        biaya_parkir = self.tarif_per_detik * (durasi_parkir_detik // 60)

        if durasi_parkir_detik % 60 > 0:
            biaya_parkir += self.tarif_per_detik

        if durasi_parkir_detik > self.max_waktu_parkir:
            biaya_parkir += biaya_parkir * self.denda_1
            if durasi_parkir_detik > (self.max_waktu_parkir + 120):
                biaya_parkir += biaya_parkir * self.denda_2

        return biaya_parkir

    def menu_admin_parkir(self):
        pin_admin = input("Masukkan PIN Admin Parkir: ")

        if pin_admin == self.admin_pin:
            while True:
                print("\nMenu Admin Parkir:")
                print("1. Cetak Seluruh Transaksi Parkir")
                print("2. Kembali ke Menu Utama")
                pilihan = input("Pilih menu (1/2): ")

                if pilihan == '1':
                    self.cetak_transaksi_parkir()
                elif pilihan == '2':
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih lagi.")
        else:
            print("PIN Admin Parkir salah.")

    def cetak_transaksi_parkir(self):
        print("\nTransaksi Parkir:")
        for nomor_plat, waktu_masuk in self.kendaraan_masuk.items():
            print(f"Nomor Plat: {nomor_plat}, Waktu Masuk: {time.ctime(waktu_masuk)}")

# Inisialisasi dan jalankan program
parkir_app = Parkir()
parkir_app.menu_utama()