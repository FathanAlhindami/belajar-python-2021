#nomor4
listku = []
angka = 0
while angka != '':
    angka = input('Masukan angka = ')
    if angka != '':
        listku.append(angka)
        urut = sorted(listku)

for i in urut:
    print(i)