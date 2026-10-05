def rekap_nilai(*args):
    if len(args) == 0:
        return None, None, None

    rata_rata = sum(args) / len(args)
    nilai_tertinggi = max(args)
    nilai_terendah = min(args)

    return rata_rata, nilai_tertinggi, nilai_terendah


nilai_siswa = []

while True:
    input_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ") 
    if input_nilai == "":
        break
    
    if int(input_nilai) < 0 :
        print("Input tidak valid, nilai tidak boleh negatif.")
        continue


    nilai_siswa.append(float(input_nilai))


rata, tertinggi, terendah = rekap_nilai(*nilai_siswa)

if len(nilai_siswa) == 0:
    print("Data nilai tidak tersedia.")
else:
    print("Rata-rata kelas:", rata)
    print("Nilai tertinggi:", tertinggi)
    print("Nilai terendah:", terendah)