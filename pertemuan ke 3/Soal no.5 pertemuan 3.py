#soal5
t = int(input("Masukan Tahun = "))
if t%400 == 0:
    print("Tahun", t ,"sudah pasti tahun kabisat")
elif t%100 == 0:
    print("Tahun", t ,"sudah pasti bukan tahun kabisat")
elif t%4 == 0:
    print("Tahun", t ,"merupakan tahun kabisat")
else:
    print("Tahun", t ,"bukan merupakan tahun kabisat")