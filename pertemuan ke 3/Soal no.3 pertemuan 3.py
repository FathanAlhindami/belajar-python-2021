#soal3
s = float(input("Masukan kekuatan gempa (magnitude) = "))
if s >= 10.0:
    print("Gempa tersebut adalah gempa jenis Meteoric")
elif 8.0 <= s < 10.0:
    print("Gempa tersebut adalah gempa jenis Great")
elif 7.0 <= s < 8.0:
    print("Gempa tersebut adalah gempa jenis Major")
elif 6.0 <= s < 7.0:
    print("Gempa tersebut adalah gempa jenis Strong")
elif 5.0 <= s < 6.0:
    print("Gempa tersebut adalah gempa jenis Moderate")
elif 4.0 <= s < 5.0:
    print("Gempa tersebut adalah gempa jenis Light")
elif 3.0 <= s < 4.0:
    print("Gempa tersebut adalah gempa jenis Minor")
elif 2.0 <= s < 3.0:
    print("Gempa tersebut adalah gempa jenis Very minor")
else:
    print("Gempa tersebut adalah gempa jenis Micro")