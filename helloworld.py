print("Hello, World!")

daftar_kontak = []

def daftar ():
    for kontak in daftar_kontak:
        print("Nama: {}" . format(kontak["nama"]))
        print("No. Telepon: {}" . format(kontak["telepon"]))

def tambah ():
    kontak = {}
    nama_baru = input("Nama: ")
    telepon_baru = input("No. Telepon: ")
    kontak["nama"] = nama_baru
    kontak ["telepon"] = telepon_baru