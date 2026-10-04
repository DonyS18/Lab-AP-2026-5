#1. Rekapitulasi Transaksi "Dins Store"
while True:
    try:
        jumlah = int(input("Masukkan jumlah item: "))

        if jumlah == 0:
            print("Toko ditutup. Sesi rekap selesai.")
            break

        if jumlah < 0:
            print("Jumlah tidak boleh negatif")
            continue

        if jumlah > 100:
            print("Maksimal 100 item per transaksi!")
            continue

        print(f"Transaksi {jumlah} item berhasil!")

    except ValueError:
        print("Input harus berupa angka!")

#Denah Kursi Bioskop
while True:
    try:
        N = int(input("Masukkan jumlah baris: "))

        if N <= 0:
            print("Jumlah harus lebih dari 0")
        else:
            break

    except ValueError:
        print("Input harus berupa angka!")


while True:
    try:
        M = int(input("Masukkan jumlah kursi: "))

        if M <= 0:
            print("Jumlah harus lebih dari 0")
        else:
            break

    except ValueError:
        print("Input harus berupa angka!")


for baris in range(1, N + 1):

    for kursi in range(1, M + 1):

        if kursi == 13:
            continue

        if baris == 1:
            if kursi % 2 == 1:
                print("Baris", baris, "Kursi", kursi)
        else:
            print("Baris", baris, "Kursi", kursi)

#Sistem Reservasi "PO Bioskop"
N = int(input("Masukkan jumlah kursi bus: "))

sisa_kursi = N
total_pendapatan = 0

while sisa_kursi > 0:
    umur = int(input("Masukkan umur penumpang: "))

    if umur < 0:
        print("Umur tidak valid!")
        continue

    if umur <= 5:
        harga = 0
    elif umur <= 12:
        harga = 50000
    else:
        harga = 100000

    sisa_kursi -= 1
    total_pendapatan += harga

    print("Tiket berhasil diproses.")
    print("Sisa kursi:", sisa_kursi)

print("Total pendapatan bus: Rp", total_pendapatan)