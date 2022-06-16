#soal 6
jumlah = 0
data = 0
n = 0
while data != '':
    data = input("Masukan angka = ")
    if data != '':
        data = float(data)
        jumlah += data
        n += 1
        
print("rata-rata = ",jumlah/n)