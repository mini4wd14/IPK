list_nim = []
list_nama = []
list_alamat = []
list_asal_sekolah = []
list_prodi = []
list_ipk_awal = []
list_nilai_gabung = []
list_ips = []
list_ipk_akhir = []
list_ket = []
x = int(input("Masukan jumlah siswa :"))

for i in range(x):
    nim = input("Masukan NIM : ")
    nama = input("Masukan Nama : ")
    alamat = input("Masukan Alamat : ")
    asal_sekolah = input("Masukan asal sekolah : ")
    prodi = input("Masukan kode Prodi : ")
    ipk_awal = int(input("Masukan IPK Awal : "))
    uts,uas,tm = input("Nilai UTS, UAS, TM (dipisahkan dengan spasi) : ").split(" ")
    list_temp_nilai = [uts,uas,tm]
    list_nilai = list(map(int,list_temp_nilai))
    list_nim.append(nim)
    list_nama.append(nama)
    list_alamat.append(alamat)
    list_asal_sekolah.append(asal_sekolah)
    list_prodi.append(prodi)
    list_ipk_awal.append(ipk_awal)
    list_nilai_gabung.append(list_nilai)

for i in range(x):
    ips = 0.3*list_nilai_gabung[i][0] + 0.3*list_nilai_gabung[i][2] + 0.4*list_nilai_gabung[i][1]
    list_ips.append(ips)

for i in range(x):
    ipk_final = (list_ipk_awal[i]+list_ips[i])*0.5
    list_ipk_akhir.append(ipk_final)

for i in range(x):
    if list_prodi[i] == "TI" or "SI":
        if 75 < list_ipk_akhir[i] < 85:
            list_ket.append("20 %")
        elif 85 < list_ipk_akhir[i] < 100:
            list_ket.append("30 %")
        else:
            list_ket.append("Tidak mendapat beasiswa")
    elif list_prodi[i] == "DKV" or "Teknik Industri":
        if 75 < list_ipk_akhir[i] < 85:
            list_ket.append("25 %")
        elif 85 < list_ipk_akhir[i] < 100:
            list_ket.append("35 %")
        else:
            list_ket.append("Tidak mendapat beasiswa")

print("Rekap data mahasiswa")
print("_________________________________________________________________________________________________________________________________________________________________________")
print("| NIM       | Nama      | Alamat    | Asal Sekolah | Kode Prodi | Nilai IPK Awal | Nilai UTS | Nilai UAS | Nilai TM  | Nilai IPS | Nilai Akhir | Keterangan Beasiswa     |")

for i in range(x):
    print("| " + list_nim[i] + " "*(10-len(list_nim[i])) + "| " 
    + list_nama[i] + " "*(10-len(list_nama[i])) + "| " 
    + list_alamat[i] + " "*(10-len(list_alamat[i])) + "| " 
    + list_asal_sekolah[i] + " "*(13-len(list_asal_sekolah[i])) + "| " 
    + list_prodi[i]  + " "*(11-len(list_prodi[i])) + "| " 
    + str(list_ipk_awal[i]) + " "*(15-len(str(list_ipk_awal[i]))) + "| " 
    + str(list_nilai_gabung[i][0]) + " "*(10-len(str(list_nilai_gabung[i][0]))) + "| " 
    + str(list_nilai_gabung[i][1]) + " "*(10-len(str(list_nilai_gabung[i][1]))) + "| " 
    + str(list_nilai_gabung[i][2]) + " "*(10-len(str(list_nilai_gabung[i][2]))) + "| " 
    + str(list_ips[i]) + " "*(10-len(str(list_ips[i]))) + "| " 
    + str(list_ipk_akhir[i]) + " "*(12-len(str(list_ipk_akhir[i]))) + "| " 
    + list_ket[i] + " "*(24-len(str(list_ket[i]))) + "| ")