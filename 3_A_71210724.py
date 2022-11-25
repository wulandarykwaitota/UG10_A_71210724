soal1 = input("Masukkan nilai soal 1: ")
soal2 = input("Masukkan nilai soal 2: ")
soal3 = input("Masukkan nilai soal 3: ")
umur = int(input("Masukkan umur anda: "))
hasil = (soal1*0.5) + (soal2*0.3) + (soal3*0.2)
print("Rata-rata nilai Anda: ",hasil)

if umur <= 25:
    if hasil >= 80:
        print("selamat anda lulus!")
    else:
        print("Coba lagi tahun depan!")
else:
    if hasil >= 90:
        print("selamat anda lulus!")
    else:
        print("Coba lagi tahun depan!")


