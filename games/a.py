
def a():
    """
    Buatlah fungsi Python yang mengonversi angka menjadi format teks
    bahasa Indonesia untuk angka 1 hingga 1.000.000.000

    MASUKAN
    n = 345

    KELUARAN
    Tiga ratus empat puluh lima
    """

    # write the code solution here
    n = input("Masukkan angka: ")
    angka = int(n)

    if angka < 0 or angka > 999999999:
        print("Maaf, angka minimal 0 dan maksimal 999.999.999")
        return
    else:
        if angka == 0:
            print("Nol")

        satuan = ["", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan"]
        belasan = ["sepuluh", "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas",
                "enam belas", "tujuh belas", "delapan belas", "sembilan belas"]
        puluhan = ["", "", "dua puluh", "tiga puluh", "empat puluh", "lima puluh",
                "enam puluh", "tujuh puluh", "delapan puluh", "sembilan puluh"]

        def convert_below_thousand(num):
            """Mengonversi angka di bawah 1000 menjadi teks."""
            teks = ""
            if num >= 100:
                if num // 100 == 1:
                    teks += "seratus "
                else:
                    teks += satuan[num // 100] + " ratus "
                num %= 100
            if 10 <= num < 20:
                teks += belasan[num - 10]
            else:
                if num >= 20:
                    teks += puluhan[num // 10] + " "
                    num %= 10
                if num > 0:
                    teks += satuan[num]
            return teks.strip()

        hasil = ""
        bagian = ["", "ribu", "juta", "miliar"]  # Untuk angka hingga 1 miliar
        i = 0

        while angka > 0:
            tiga_digit = angka % 1000
            if tiga_digit > 0:
                if i > 0 and tiga_digit == 1 and i == 1:
                    hasil = "seribu " + hasil
                else:
                    bagian_teks = bagian[i]
                    hasil = convert_below_thousand(tiga_digit) + (" " + bagian_teks if bagian_teks else "") + " " + hasil
            angka //= 1000
            i += 1

        text = hasil.strip()
        print(text)