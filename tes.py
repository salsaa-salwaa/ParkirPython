import datetime

kendaraan_masuk = {}

def masuk_parkir():
    plat_nomor = str(input("Masukkan nomor/plat kendaraan: "))
    waktu_masuk = datetime.datetime.now()
    print("Waktu masuk:", waktu_masuk)
    kendaraan_masuk[plat_nomor] = waktu_masuk
    print("Silakan masuk")

def keluar_parkir():
    plat_nomor = str(input("Masukkan nomor/plat kendaraan: "))

    if plat_nomor not in kendaraan_masuk:
        print("Error: Kendaraan tidak tercatat masuk.")
        return

    waktu_keluar = datetime.datetime.now()
    waktu_masuk = kendaraan_masuk[plat_nomor]
    durasi_parkir = waktu_keluar - waktu_masuk
    print("Waktu keluar:", waktu_keluar)
    print("Durasi parkir:", durasi_parkir)
    biaya_parkir = biaya_parkir_calculation(durasi_parkir.total_seconds())
    print(f'Biaya total parkir: Rp {biaya_parkir:,}')
    del kendaraan_masuk[plat_nomor]

def admin_parkir():
    pin_admin = int(input("Masukkan PIN akses admin (4 digit): "))
    if pin_admin == 2810:
        print("PIN benar!")
        while True:
            print("===== MENU ADMIN =====")
            print("1. Cetak Transaksi Parkir")
            print("2. Kembali Menu Utama")
            print("3. Keluar")
            input_admin = int(input("Pilih menu (1/2/3): "))
            if input_admin == 1:
                cetak_transaksi_parkir()
            elif input_admin == 2:
                break
            elif input_admin == 3:
                exit()
            else:
                print("Menu tidak valid. Silakan coba kembali")
    else:
        print("PIN salah, coba lagi!")

def cetak_transaksi_parkir():
    print("Daftar Transaksi Parkir:")
    for plat_nomor, waktu_masuk in kendaraan_masuk.items():
        print(f"{plat_nomor}: Waktu Masuk - {waktu_masuk}")

def biaya_parkir_calculation(waktu_parkir_detik):
    tarif_per_60_detik = 10000
    pembulatan_waktu_parkir = ((waktu_parkir_detik - 1) // 60 + 1) * 60
    biaya_parkir = (pembulatan_waktu_parkir // 60) * tarif_per_60_detik

    if waktu_parkir_detik > 240:
        denda = 0.1 * biaya_parkir
        if waktu_parkir_detik > 360:
            denda = 0.25 * biaya_parkir
        biaya_parkir += denda

    return biaya_parkir

while True:
    print("===== MENU AWAL =====")
    print("1. Masuk Area Parkir")
    print("2. Keluar Area Parkir")
    print("3. Admin Parkir")
    print("4. Keluar")
    pilihan_menu = int(input("Pilih menu (1/2/3/4): "))

    if pilihan_menu == 1:
        masuk_parkir()
    elif pilihan_menu == 2:
        keluar_parkir()
    elif pilihan_menu == 3:
        admin_parkir()
    elif pilihan_menu == 4:
        break
    else:
        print("Menu tidak valid. Silakan coba kembali")
