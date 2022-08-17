#nomor 2
listku2 = []
angka2 = 0
while angka2 != '':
    angka2 = input('Masukan angka = ')
    if angka2 != '':
        listku2.append(angka2)
        balik = sorted(listku2, reverse = True)
for j in balik:
    print(j)