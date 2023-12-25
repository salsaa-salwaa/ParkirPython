import datetime

kendaraanmasuk = []

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
    platnomor = str(input("Masukkan nomor/plat kendaraan (contoh: D1234AF): "))
    waktumasuk = datetime.datetime.now()
    kendaraanmasuk.append(
        {'nomor_plat': platnomor, 
        'waktu_masuk': waktumasuk})
    print("Waktu masuk:", waktumasuk)
    print("Gerbang masuk terbuka. Silakan masuk")

def KeluarParkir():
    platnomor = str(input("Masukkan nomor/plat kendaraan (contoh: D1234AF): "))

    try:
        kendaraan = next((k for k in kendaraanmasuk if k["nomor_plat"] == platnomor), None)
        if kendaraan:
            waktukeluar = datetime.datetime.now()
            waktumasuk = kendaraan['waktu_masuk']
            durasi_parkir = waktukeluar - waktumasuk
            print("Waktu keluar:", waktukeluar)
            print("Durasi parkir:", durasi_parkir)

            biaya_parkir = BiayaParkir(durasi_parkir.total_seconds())
            kendaraan['biaya_parkir'] = biaya_parkir
            print(f'Biaya total parkir: Rp {biaya_parkir}')
            nominal_pembayaran = float(input('Masukkan nominal pembayaran: '))
            while nominal_pembayaran < biaya_parkir:
                print("Pembayaran kurang. Silakan masukkan nominal yang cukup.")
                nominal_pembayaran = float(input('Masukkan nominal pembayaran: '))

            kembalian = nominal_pembayaran - biaya_parkir
            print(f"Kembalian: Rp {kembalian:,.2f}")
            print('Gerbang keluar terbuka.Terima kasih!')
        else:
            print("Error: Kendaraan tidak tercatat masuk.")
    except KeyError:
        print("Error: Kendaraan tidak tercatat masuk.")

def InputPin():
    pin_admin = int(input("Masukkan PIN akses admin (4 digit): "))
    if pin_admin == 2810:
        print("PIN benar!")
        return True
    else:
        print("PIN salah")
        return False

def AdminParkir():
        if InputPin():
            print("===== MENU ADMIN =====")
            print("1. Cetak Transaksi Parkir")
            print("2. Kembali Menu Utama")
            print("3. Keluar")
            input_admin = int(input("Pilih menu (1/2/3): "))
            if input_admin == 1:
                CetakTransaksiParkir()
            elif input_admin == 2:
                pass
            elif input_admin == 3:
                exit()
            else:
                print("Menu tidak valid. Silakan coba kembali")
        else:
            print("PIN salah, coba lagi!")

def CetakTransaksiParkir():
    if not kendaraanmasuk:
        print("Tidak ada transaksi parkir")
    else:
        print("\n===== TRANSAKSI PARKIR =====")
    for transaksi in kendaraanmasuk:
        print(f"Nomor Plat: {transaksi['nomor_plat']}")
        print(f"Waktu Masuk: {transaksi['waktu_masuk']}")
        
        if 'biaya_parkir' in transaksi:
            print(f"Biaya Parkir: Rp {transaksi['biaya_parkir']}")
        else:
            print("Biaya Parkir: Belum dihitung")
            
        print("=" * 30)

    total_biaya_parkir = sum(BiayaParkir((datetime.datetime.now() - transaksi['waktu_masuk']).total_seconds()) for transaksi in kendaraanmasuk if 'biaya_parkir' in transaksi)
    print(f"Total Biaya Parkir: Rp {total_biaya_parkir}")
    
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