tinggi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 6, 5, 4, 3]

perkenalan = ['halo ', 'nama ', 'saya ',
              'yusuf ', 'tinggal ', 'di ', 'tangsel']

alamat = ["Jalan setia budi nomor", 5, "RT", 6, "RW", 9, "sektor", 1.2]


def operasi_interger():
    total = 0

    for angka in tinggi:
        total += angka
    print(f"penjumlahan: {total}")

    for i in tinggi:
        total *= i
    print(f"Perkalian: {total}")

    for i in tinggi:
        total /= i
    print(f"Pembagian: {total}")

    for i in tinggi:
        total -= i
    print(f"pengurangan: {total}")


def gabung_string():
    kalimat = ""

    for kata in perkenalan:
        kalimat += kata
    print(kalimat)


def gabung_string_integer():
    for kata in alamat:
        print(kata, end=" ")


gabung_string()
print("\n")
operasi_interger()
print("\n")
gabung_string_integer()
