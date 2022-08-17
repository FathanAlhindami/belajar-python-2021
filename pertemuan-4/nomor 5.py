#Nomor 5
list = ['abc','xyz','aba','1221']
banyaknya_string = 0
for i in list:
    if len(i) >1 and i[0]==i[-1]:
        banyaknya_string +=1
    else:
        continue
print(banyaknya_string)
print(list[2:])
