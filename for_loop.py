fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# mengulang sesuai jumlah data

pelanggan = int(input("Berapa Data = "))

nama = []
usia = []

for i in range(pelanggan):
    print("Data ke {}" . format(i+1))
    nama_pelanggan = input("Nama = ")
    usia_pelanggan = int(input("Umur = "))

    nama.append(nama_pelanggan)
    usia.append(usia_pelanggan)

for i in range(len(nama)):
    print("Pelanggan {} berusia {}" . format(nama[i], usia [i]))
    