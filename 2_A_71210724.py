print("===== Selamat datang di Toko Andi Tersenyum, selamat berbelanja! =====")
totalbelanja = int(input("Total belanja :Rp."))

if totalbelanja < 100_000:
    print("Tidak ada diskon! Maka yang anda bayarkan adalah: Rp. ",totalbelanja)
elif totalbelanja >= 1_000_000:
    print("Biaya yang harus dibayar setelah diskon adalah: Rp. ", totalbelanja-(totalbelanja*0.10))
elif totalbelanja >= 500_000:
    print("Biaya yang harus dibayar setelah diskon adalah: Rp. ", totalbelanja-(totalbelanja*0.05))
else:
    print("Biaya yang harus dibayar setelah diskon adalah: Rp. ", totalbelanja-(totalbelanja*0.02))



