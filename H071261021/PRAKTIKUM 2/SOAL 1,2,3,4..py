#menentukan level kepedasan
cabai = float(input("masukan peresentase cabai:"))

if cabai < 0:
    print("input tidak valid")
elif cabai <= 10:
    print("level aman")
elif cabai <= 40:
    print("level sedang")
elif cabai <= 70:
    print("level pedas")
else:
    print("level ekstrem")

#tarif pengiriman
jarak = float(input("masukan jarak pengiriman (km): "))
express = input("layanan express (ya/tidak):")
if jarak < 5:
    tarif_dasar = 10000
elif jarak <= 20:
    tarif_dasar = 20000
else:
    tarif_dasar = 35000
biaya_express = 15000 if express == "ya" else 0 
total_tarif = tarif_dasar + biaya_express 
print("total tarif pengiriman: Rp", total_tarif)

#kelolosan pelamaran 
nilai = float(input("masukan nilai tes: "))
pengalaman = float(input("masukan pengalamn kearja (tahun):"))
if nilai >= 80:
    print("lolos ke tahan wawancara")
elif nilai >= 65 and pengalaman >= 2:
    
    print("lolos bersyarat")
else:
    print("tidak lolos ")

#rekomndasi pake wisata 
tujuan = input("masukan tujuan (pantai/pengunungan/kota): ")
waktu = input("msaukan waktu (pagi/malam):")
pengunjung = input("masukkan tipe pengunjung (anak/dewasa): ")

match tujuan:
    case "pantai":
        if waktu == "pagi":
            print("paket rekomendasi: paket A")
        else:
            if pengunjung == "dewasa":
                print("paket rekomendasi: paket C")
            else:
                print("tidak ada paket yang cocok")
    case "pegunungan":
        if waktu == "pagi" and pengunjung == "dewasa":
            print("paket rekomendasi: paket B")
        else:
            if waktu == "malam " and pengunjung == "dewasa":
                print("paket rekomendasi: paket C")
            else:
                print("tidak ada paket yang cocok")
    case "kota":
        if waktu == "malam":
            print("paket rekomendasi: paket C")
        else:
            print("tidak ada paket yang cocok ")
    case _:
        print("tidak ada yang cocok")