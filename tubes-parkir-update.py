import datetime
from tabulate import tabulate

kendaraanmasuk = []

def MenuUtama():
    while True:
        print("===== MENU AWAL =====")
        print("1. Masuk Area Parkir")
        print("2. Keluar Area Parkir")
        print("3. Admin Parkir")
        print("4. Keluar")

        try:
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
        except ValueError:
            print("Input tidak valid. Masukkan angka (1/2/3/4).")
            continue
    return MenuUtama

def MasukParkir():
    platnomor = str(input("Masukkan nomor/plat kendaraan: "))
    waktumasuk = datetime.datetime.now()
    waktukeluar = None
    kendaraanmasuk.append({'nomor_plat': platnomor, 'waktu_masuk': waktumasuk, 'waktu_keluar':waktukeluar})
    print("Waktu masuk:", waktumasuk)
    print("Silakan masuk")

def KeluarParkir():
    platnomor = str(input("Masukkan nomor/plat kendaraan: "))

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
            kendaraan['waktu_keluar'] = waktukeluar
            print(f'Biaya total parkir: Rp {biaya_parkir}')
            nominal_pembayaran = float(input('Masukkan nominal pembayaran: '))
            while nominal_pembayaran < biaya_parkir:
                print("Pembayaran kurang. Silakan masukkan nominal yang cukup.")
                nominal_pembayaran = float(input('Masukkan nominal pembayaran: '))

            kembalian = nominal_pembayaran - biaya_parkir
            print(f"Kembalian: Rp {kembalian:,.2f}")
            print('Terimakasih!')
        else:
            print("Error: Kendaraan tidak tercatat masuk.")
    except KeyError:
        print("Error: Kendaraan tidak tercatat masuk.")

def InputPin():
    max_coba = 3
    coba = 0
    while coba < max_coba:
        pin_admin = int(input("Masukkan PIN akses admin (4 digit): "))
        if pin_admin == 2810:
            print("PIN benar!")
            return True
        else:
            print("PIN salah")
            coba += 1
            if coba == max_coba:
              print("Maaf, Anda telah melebihi batas percobaan.")
              return False

def AdminParkir():
        if InputPin():
            while True:
                print("===== MENU ADMIN =====")
                print("1. Cetak Transaksi Parkir")
                print("2. Kembali Menu Utama")
                print("3. Keluar")
                try:
                    input_admin = int(input("Pilih menu (1/2/3): "))
                    if input_admin == 1:
                        CetakTransaksiParkir()
                    elif input_admin == 2:
                        return
                    elif input_admin == 3:
                        exit()
                    else:
                        print("Menu tidak valid. Silakan coba kembali")
                except ValueError:
                    print("Input tidak valid. Masukkan angka (1/2/3).")
        else:
            print("PIN salah, coba lagi!")

def CetakTransaksiParkir():
    if not kendaraanmasuk:
        print("Tidak ada transaksi parkir")
    else:
        print("\n===== TRANSAKSI PARKIR =====")
        headers = ["Nomor Plat", "Waktu Masuk", "Waktu Keluar", "Biaya Parkir"]
        rows = []
        
        for transaksi in kendaraanmasuk:
            nomor_plat = transaksi['nomor_plat']
            waktu_masuk = str(transaksi['waktu_masuk'])

            if 'waktu_keluar' in transaksi:
                waktu_keluar = str(transaksi['waktu_keluar'])
                if 'biaya_parkir' in transaksi:
                    biaya_parkir = f"Rp {transaksi['biaya_parkir']}"
                else:
                    biaya_parkir = "Belum dihitung"
            else:
                waktu_keluar = "Kendaraan masih dalam area parkir"
                biaya_parkir = ""

            rows.append([nomor_plat, waktu_masuk, waktu_keluar, biaya_parkir])

        print(tabulate(rows, headers, tablefmt="grid"))
                
def BiayaParkir(waktu_parkir_detik):
    tarif_per_60_detik = 10000
    pembulatan_waktu_parkir = ((waktu_parkir_detik - 1) // 60 + 1) * 60 
    biaya_parkir = (pembulatan_waktu_parkir // 60) * tarif_per_60_detik

    denda = 0

    if waktu_parkir_detik > 240:
        biaya_parkir = 40000
        denda = 0.1 * biaya_parkir
        print("Denda sebesar 10% dari biaya parkir diterapkan.")
    elif waktu_parkir_detik > 360:  
        biaya_parkir = 50000
        denda = 0.25 * biaya_parkir
        print("Denda sebesar 25% dari biaya parkir diterapkan.")
    biaya_parkir += denda

    return biaya_parkir

MenuUtama()
