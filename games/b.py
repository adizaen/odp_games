
def b():

    """
    Diberikan sebuah list angka, cari pasangan angka dengan selisih terkecil.

    MASUKAN
    data = [4, 8, 15, 16, 23, 42] 

    KELUARAN
    15 16
    """

    # write the code solution here
    n = input("Masukkan angka: ")

    n_list = [int(i) for i in n.split()]
    urutan=sorted(n_list)
    data=[]
    data_terkecil = None
    selisih_min = float('inf')
    for i in range(1,len(urutan)):
        hasil=urutan[i]-urutan[i-1]
        hasil=abs(hasil)
        data.append(hasil)
        if hasil<selisih_min:
            selisih_min=hasil
            data_terkecil=(urutan[i-1],urutan[i])
    print(data_terkecil) 

