print("Selamat sudah menyelesaikan ujian! Apakah kamu lulus? Mari kita cek!")

ut = int(input("Nilai ujian teori   : "))
up = int(input("Nilai ujian praktek : "))

if   ut >= 70 and up >= 70:
    print("Selamat, Anda lulus!")
elif ut >= 70 and up < 70:
    print("Anda harus mengulang ujian praktek.")
elif ut < 70 and up >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")
