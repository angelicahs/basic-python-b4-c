pelanggan = {
    "Nama" : "Awan",
    "Umur" : 18
}

pelanggan_2 = {
    "Nama" : "Hendra",
    "Umur" : 20
}

# change value of dictionary
pelanggan["Umur"] = 22

#print("Nama: {}" . format(pelanggan["Nama"]))
#print("Usia: {}" . format(pelanggan["Umur"]))
#print("Nama: {}" . format(pelanggan_2["Nama"]))
#print("Usia: {}" . format(pelanggan_2["Umur"]))

# loop through dictionary
#for x in pelanggan:
    #print(x)
    #print(pelanggan[x])
    #print(pelanggan_2[x])
    #print("==========")

# list of dictionary
daftar_pelanggan = []
daftar_pelanggan.append(pelanggan)
daftar_pelanggan.append(pelanggan_2)

for pelanggan in daftar_pelanggan:
    print("Nama: {}" . format(pelanggan["Nama"]))
    print("Umur: {}" . format(pelanggan["Umur"]))