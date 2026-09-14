menu = ["kopi susu", "matcha latte", "americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]
total_seluruh = sub_kopi + sub_matcha + sub_americano
BIAYA_OPERASIONAL = 15000 
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL
jumlah_barang = 4 + 3 + 5
target_tercapai = total_seluruh > 2000000 and jumlah_barang >  10

print(subtotal_pendapatan)
print(pendapatan_bersih)
print(target_tercapai)
