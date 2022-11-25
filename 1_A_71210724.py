nama = input("Masukkan nama mahasiswa : ")
nim = input("Masukkan NIM-nya : ")
string =(nim[0:4])
if nim[0:2] == '71' and int(nim[2:4]) <= 22 and int(nim[2:4]) >= 20:
    
    print(nim, "Merupakan mahasiswa informatika angkatan 20 hingga 22")
    
else:
    print("bukan mahasiswa informatika angktan 20 hingga 22")