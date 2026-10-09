jenis_kelamin = input("Masukkan jenis kelamin (wanita/pria): ")
umur = int(input("Masukkan umur: "))
tinggi = float(input("Masukkan tinggi badan (cm): "))
iq = int(input("Masukkan IQ: "))

if umur >= 18 and umur <= 25 and iq >= 130:
    if jenis_kelamin == "wanita" and tinggi >= 170:
        print("Anda memenuhi syarat menjadi model catwalk.")
    elif jenis_kelamin == "pria" and tinggi >= 175:
        print("Anda memenuhi syarat menjadi model catwalk.")
    else:
        print("Anda tidak memenuhi syarat menjadi model catwalk.")
else:
    print("Anda tidak memenuhi syarat menjadi model catwalk.")