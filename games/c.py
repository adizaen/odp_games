
def c():
    """
    Buat program untuk memeriksa apakah sebuah angka merupakan bilangan Armstrong.
    Bilangan Armstrong adalah angka yang sama dengan jumlah pangkat 𝑛-nya, di mana 𝑛 adalah jumlah digit angka tersebut.

    MASUKAN
    n = 153

    KELUARAN
    153 adalah bilangan Armstrong
    """

    # write the code solution here
    n = input("Masukkan angka: ")

    n_string = str(n)
    
    temp = 0
    for i in n_string:
        temp = temp + int(i)**len(n_string)

    if temp == int(n_string):
        print(f"Bilangan {n_string} adalah bilangan Armstrong")
    else:
        print(f"Bilangan {n_string} bukan bilangan Armstrong")
