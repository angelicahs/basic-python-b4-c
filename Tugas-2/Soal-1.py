#daftar nama kontak

nama_kontak   = []
nomor_telepon = []

def daftar ():
    panjang_data = len(nama_kontak)
    if panjang_data == 0:
        print("Data kosong, silakan masukkan kontak")
        print("====================================")
        menu()
    else:
        for x in range(panjang_data):
            print("Data Kontak : ")
            print("Nama : ", nama_kontak[x])
            print("Nomor telepon : ", nomor_telepon[x])
            print("--------------------------------")
        print("==================================")
        menu()

def tambah():
    nama  = input("Masukkan nama kontak : ")
    nomor = input("Masukkan nomor telepon : ")
    nama_kontak.append(nama)
    nomor_telepon.append(nomor)
    print("Kontak telah berhasil ditambahkan.")
    print("==================================")
    menu()

def keluar():
    print("Terima kasih! Program telah selesai.")

def menu():
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    pilihan = input("Pilih Menu : ")

    if pilihan == '1':
        daftar()
    elif pilihan == '2':
        tambah()
    elif pilihan == '3':
        keluar()
    else:
        print("Maaf menu tidak tersedia, Silakan pilih menu yang ada!")
        menu()

print("Selamat datang, silakan pilih menu yang tersedia!")
menu()