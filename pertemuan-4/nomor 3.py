# nomor 3
mylist = []
angka = 0
while angka != '':
    angka = str(input('Masukan angka = '))
    if angka != '':
        mylist.append(angka)
        urut = sorted(set(mylist))
for i in urut:
    print(i)