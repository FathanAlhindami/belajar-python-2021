#soal 5
tinggi = float(input("Masukan Tinggi Badan Anda :"))
satuan = input("Dalam satuan kaki atau inci? ")
if satuan == "kaki":
    kaki = tinggi*12*2.54
    print("Tinggi badan kamu adalah : ",kaki, "cm")
else:
    inci = tinggi*2.54
    print("Tinggi badan kamu adalah : ",inci,"cm")