import ctypes
# pointer : variabel yang menyimpan alamat memory sebagai nilai nya

'''
Berdasarkan GeeksForGeeks,
kita bisa mendapatkan memory address
dalam format hexadesimal dengan memanggil
fungsi hex(), untuk mengubah alamat memory
menjadi representasi hexadesimal
'''


def penjumlahan(num1, num2):
    print(f"alamat angka pertama: {hex(num1)}")
    print(f"alamat angka kedua: {hex(num2)}")

    total = ctypes.cast(num1, ctypes.py_object).value + \
        ctypes.cast(num2, ctypes.py_object).value

    print(f"hasil penjumlahan: {total}")
    print(f"alamat hasil penjumlahan: {hex(id(total))}")


def gabung_kalimat(string1, string2):
    print(f"alamat string pertama: {hex(id(string1))}")
    print(f"alamat string kedua: {hex(id(string2))}")

    hasil = ctypes.cast(string1, ctypes.py_object).value + \
        ctypes.cast(string2, ctypes.py_object).value
    print(f"hasil penggabungan: {hasil}")
    print(f"alamat hasil penggabungan: {hex(id(hasil))}")


penjumlahan(id(3), id(30))
print("\n")
gabung_kalimat(id("hello"), id(" dunia!"))
