import datetime

kendaraanmasuk = {}

def MenuUtama():
    while True:
        print("===== MENU AWAL =====")
        print("1. Masuk Area Parkir")
        print("2. Keluar Area Parkir")
        print("3. Admin Parkir")
        print("4. Keluar")
        pilihanmenu = int(input("Pilih menu (1/2/3/4): "))

        if pilihanmenu == 1:
            MasukParkir()
        elif pilihanmenu == 2:
            KeluarParkir()
        elif pilihanmenu == 3:
            AdminParkir()
        elif pilihanmenu == 4:
            break
        else:
            print("Menu tidak valid. Silakan coba kembali")

    return MenuUtama

def MasukParkir():
    platnomor = str(input("Masukkan nomor/plat kendaraan: "))
    waktumasuk = datetime.datetime.now()
    print("Waktu masuk:", waktumasuk)
    kendaraanmasuk[platnomor] = waktumasuk
    print("Silakan masuk")

def KeluarParkir():
    platnomor = str(input("Masukkan nomor/plat kendaraan: "))

    if platnomor not in kendaraanmasuk:
        print("Error: Kendaraan tidak tercatat masuk.")
        return

    waktukeluar = datetime.datetime.now()
    waktumasuk = kendaraanmasuk[platnomor]
    durasi_parkir = waktukeluar - waktumasuk
    print("Waktu keluar:", waktukeluar)
    print("Durasi parkir:", durasi_parkir)
    biaya_parkir = BiayaParkir(durasi_parkir.total_seconds())
    print(f'Biaya total parkir: Rp {biaya_parkir}')
    del kendaraanmasuk[platnomor] 

def AdminParkir():
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
                CetakTransaksiParkir()
            elif input_admin == 2:
                MenuUtama()
            elif input_admin == 3:
                exit()
            else:
                print("Menu tidak valid. Silakan coba kembali")
    else:
        print("PIN salah, coba lagi!")

def CetakTransaksiParkir():
    print("")

def BiayaParkir(waktu_parkir_detik):
    tarif_per_60_detik = 10000
    pembulatan_waktu_parkir = ((waktu_parkir_detik - 1) // 60 + 1) * 60
    biaya_parkir = (pembulatan_waktu_parkir // 60) * tarif_per_60_detik

    if waktu_parkir_detik > 240:  
        denda = 0.1 * biaya_parkir
        if waktu_parkir_detik > 360:  
            denda = 0.25 * biaya_parkir
        biaya_parkir += denda

        return biaya_parkir
    
MenuUtama()