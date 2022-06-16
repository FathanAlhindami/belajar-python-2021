#soal4
w = float(input("Masukan panjang gelombang cahaya (nm) = "))
if 380 <= w < 450:
    print("Spektrum yang terlihat adalah Violet")
elif 450 <= w < 495:
    print("Spektrum yang terlihat adalah Blue")
elif 495 <= w < 570:
    print("Spektrum yang terlihat adalah Green")
elif 570 <= w < 590:
    print("Spektrum yang terlihat adalah Yellow")
elif 590 <= w < 620:
    print("Spektrum yang terlihat adalah Orange")
elif 620 <= w <= 750:
    print("Spektrum yang terlihat adalah Red")
else:
    print("Input kamu diluar spektrum yang diketahui")
    