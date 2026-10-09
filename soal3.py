nama = str(input("Masukkan nama: "))
tugas = float(input("Masukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

rata_rata = (tugas + uts + uas) / 3

print("Rata-rata nilai:", rata_rata)

if rata_rata >= 70:
    if tugas >= 60 and uts >= 60 and uas >= 60:
        print(nama, "kamu LULUS tanpa remedial")
    else:
        print(nama, "kamu LULUS dengan remedial")
elif rata_rata >= 50:
        print(nama, "kamu TUDAk LULUS, boleh remedial")
else:
    print(nama, "kamu TIDAK LULUS, tidak boleh remedial")
         
       



        
