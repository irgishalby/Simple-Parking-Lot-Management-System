import time

# Fungsi Mulai Timer
def timer_mulai():
    mulai_waktu = time.time()
    return mulai_waktu

# Fungsi Menghentikan Timer
def stop_timer(mulai_waktu):
    waktu_akhir = time.time()
    waktu_berlalu = waktu_akhir - mulai_waktu
    return waktu_berlalu

# Variable dan list
daftar_kendaraan = []
total_kendaraan_masuk = 0
total_kendaraan_keluar = 0

# Definisi Fungsi Menu Utama
def main_menu():
    while True:
        # Menu Utama
        print("""
    ========= Parkir Telkom =========
    |       1. Masuk Parkir         |
    |       2. Keluar Parkir        |
    |       3. Admin                |
    =================================
        """)
        
        # Input Menu
        pilih_menu = input("Pilih Menu : ")

        # Pilihan Menu 1: Masuk Parkir
        if pilih_menu == "1":
            masuk_parkir()
        # Pilihan Menu 2: Keluar Parkir
        elif pilih_menu == "2":
            keluar_parkir()
        # Pilihan Menu 3: Admin
        elif pilih_menu == "3":
            admin_menu()
        # Pesan Salah Input
        else:
            print("!!!Salah Masukan!!!")

# Fungsi Menu 1: Masuk Parkir
def masuk_parkir():
    while True:
        # Input Tipe Kendaraan Mobil/Motor
        while True:
            tipe_kendaraan = input("\n(1) Tipe Kendaraan : ").capitalize()
            if tipe_kendaraan not in ("Mobil", "Motor", "Car", "Motorcycle"):
                print("!!!Masukan Salah!!!")
            else:
                break
        # Input Plat Nomor
        plat_nomor = input("(2) Plat Nomor     : ").upper()
        

        # Cek kendaraan didalam sudah ada atau belum
        kendaraan_didalam = next((kendaraan for kendaraan in daftar_kendaraan if kendaraan["plat_nomor"] == plat_nomor), None)

        # Menolak plat nomor jika sudah ada di parkiran
        if kendaraan_didalam:
            print("""
==========================================
|  Kendaraan dengan plat nomor tersebut  |
|         SUDAH ADA DALAM PARKIR         | 
|          "Silahkan coba lagi"          |
==========================================
                """)
            
        # Menerima plat jika belum ada di parkiran
        else:
            # Variable waktu & tanggal masuk
            waktu_masuk = time.asctime()

            # Pesan Masuk
            print(f"""
========================================
|Waktu Masuk : {waktu_masuk}|
|                                      |
|            "Silahkan Masuk"          |
========================================
        \n""")
            
            #  Timer Mulai
            mulai_waktu = timer_mulai()

            # Masukin data ke Dictionary
            kendaraan = {
                "tipe_kendaraan": tipe_kendaraan,
                "plat_nomor": plat_nomor,
                "waktu_masuk": waktu_masuk,
                "mulai_waktu": mulai_waktu
            }

            # Memasukan kendaraan
            daftar_kendaraan.append(kendaraan)
            global total_kendaraan_masuk
            total_kendaraan_masuk += 1
            break

# Fungsi Menu 2: Keluar Parkir
def keluar_parkir():
    global total_kendaraan_keluar

    while True:
        if total_kendaraan_masuk - total_kendaraan_keluar == 0:
            print("""
  ======================================
  | Tidak Ada Kendaraan Dalam Parkiran |
  ======================================
            """)
            time.sleep(1)
            return

        print("""
  =======================================
  |   Masukan Plat Nomor Untuk Keluar   |
  =======================================
            """)
        # Input Plat Nomor
        plat = input("\n(1) Plat: ").upper()

        konfirmasi_kendaraan = next((kendaraan for kendaraan in daftar_kendaraan if kendaraan["plat_nomor"] == plat), None)

        # Cek kalau kendaraan sudah keluar atau blm
        if konfirmasi_kendaraan:
            if "waktu_keluar" in konfirmasi_kendaraan: # Kalo kendaraan udh kluar
                print("!!!Kendaraan sudah keluar!!!")
                break
            else: # Kalo belum keluar
                waktu_berlalu = stop_timer(konfirmasi_kendaraan["mulai_waktu"]) 
                waktu_keluar = time.asctime() 

                pembulatan_waktu = waktu_berlalu + 59
                detik_ke_menit = pembulatan_waktu // 60

                Tarif = detik_ke_menit * 10000
                persentase10 = Tarif * 0.1
                persentase25 = Tarif * 0.25

                if waktu_berlalu <= 240: # kurang sama dengan 4 menit
                    Tarif
                    denda = "Tidak Ada"
                elif waktu_berlalu <= 360: # Denda 4-6 menit
                    Tarif = Tarif + persentase10
                    denda = "10%"
                elif waktu_berlalu > 360: # Denda diatas 6 menit
                    Tarif = Tarif + persentase25
                    denda = "25%"

                # update dictionary
                konfirmasi_kendaraan.update({
                    "waktu_keluar": waktu_keluar,
                    "tarif": Tarif,
                    "denda": denda
                })
                
                total_kendaraan_keluar += 1

                print(f"""
  ========================================
  Waktu Keluar  : {waktu_keluar} 

  Durasi Parkir : {waktu_berlalu:.0f} Detik atau {detik_ke_menit} Menit

  Tarif         : Rp. {Tarif}
  Denda         : {denda}
  ========================================
                \n""")

                print("""
    ====== Metode Pembayaran ======
    |         1. E-Money          |
    |         2. Flazz            |
    |         3. Tunai            |
    ===============================
                """)

                while True:
                    menu_pembayaran = input("(2) Menu Pembayaran: ")

                    if menu_pembayaran == "1":
                        metode_pembayaran = "E-Money"
                        print("Silahkan Tap Kartu\n")
                        break
                    elif menu_pembayaran == "2":
                        metode_pembayaran = "Flazz"
                        print("Silahkan Tap Kartu\n")
                        break
                    elif menu_pembayaran == "3":
                        metode_pembayaran = "Tunai"
                        while True:
                            try:
                                while True:
                                    bayar_tunai = int(input("(3) Masukan Nominal: "))
                                    if bayar_tunai == Tarif:
                                        print("Transaksi SUKSES\n")
                                        break
                                    else:
                                        print("!!!Transaksi Gagal!!!\n")
                            except ValueError:
                                print("!!!Salah masukan!!!\n")
                            else:
                                break
                        break
                    else:
                        print("!!!Salah Masukan, Silahkan Coba lagi!!!\n")

                time.sleep(1.5)

                while True:
                    konfirmasi = input("Tekan ENTER Jika Sudah Bayar")
                    if konfirmasi == "":
                        konfirmasi_kendaraan["metode_pembayaran"] = metode_pembayaran

                        print(f"""\n
  ================ INVOICE ===============
  Pembayaran Menggunakan {metode_pembayaran}
  Transaksi Sebesar Rp. {Tarif} BERHASIL
  ======= TERIMA KASIH SELAMAT JALAN =====\n""")
                        main_menu()

                    else:
                        print("!!!Salah Masukan!!!\n")
        else:
            print("!!!Salah Masukan!!!\n")

# Fungsi Menu 3: Admin
def admin_menu():
    print("""
    ==================================
    |     Masukan PIN Untuk Masuk    |
    | Tekan Tombol Enter Untuk Balik |
    ==================================
""")
    while True:
        pin = input("Pin/Menu : ")
        # Input PIN
        while True:
        
            # Jika Pin Benar
            if pin == "2222":
                # Menu Admin
                print("""
    =========== MENU ADMIN ===========
    |     1. RIWAYAT TRANSAKSI       |
    |     2. RIWAYAT KENDARAAN       |
    |     3. KEMBALI KE MENU UTAMA   |
    |     4. KELUAR                  |
    ==================================\n""")
            
                # Input Admin
                pilih = input("Masukkan menu admin : ")

                # Admin Pilihan: 1 
                if pilih == "1":

                    # Judul
                    print("============ RIWAYAT TRANSAKSI ============")

                    # Variable Pendapatan
                    total_pendapatan = 0

                    # Loop Untuk Print Transaksi
                    for i, kendaraan in enumerate(daftar_kendaraan, start=1):
                        # Menentukan Tarif Sudah Dibayar atau Belum
                        tarif_value = kendaraan.get('tarif', 'Belum Keluar')
                        # Menambah Rp.
                        tarif_str = f"Rp. {tarif_value}" if isinstance(tarif_value, (int, float)) else tarif_value
                        print(f"""
[{i}]
Plat              : {kendaraan["plat_nomor"]}
Tipe Kendaraan    : {kendaraan["tipe_kendaraan"]}
Waktu Masuk       : {kendaraan["waktu_masuk"]}
Waktu Keluar      : {kendaraan.get("waktu_keluar", "Belum Keluar")}
Tarif             : {tarif_str}
Metode Pembayaran : {kendaraan.get("metode_pembayaran", "Belum Keluar")}
============================================
    """)
                        # Total pendapatan
                        total_pendapatan += kendaraan.get("tarif", 0)

                        # Print Pendapatan
                    print(f"Total Pendapatan: Rp. {total_pendapatan}\n")

                # Admin Pilihan 2
                elif pilih == "2":

                    # Riwayat Kendaraan
                    print(f"""
       ===== RIWAYAT KENDARAAN =====
       Total Kendaraan Didalam: {total_kendaraan_masuk - total_kendaraan_keluar}
       Total Kendaraan Keluar : {total_kendaraan_keluar}
       Total Semua Kendaraan  : {total_kendaraan_masuk}
       \n""")

                # Balik Ke Menu Utama
                elif pilih == "3":
                    main_menu()

                # Exit
                elif pilih == "4":
                    print("Terimakasih")
                    exit()

                # Salah Input
                else:
                    print("!!!Salah Masukan!!!\n")

            # Balik Ke Menu Utama
            elif pin == "":
                main_menu()
        
            # Pesan Salah PIN
            else:
                print("""
    ==================================
    |            PIN SALAH           |
    ==================================\n""")
                break

# Panggil Fungsi Main Menu
main_menu()