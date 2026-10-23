harga_satuan = float(input("Masukkan harga satuan: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))
persen_diskon = float(input("Masukkan persentase diskon: "))

subtotal = harga_satuan * jumlah_barang
nominal_diskon = subtotal * persen_diskon / 100
total_bayar = subtotal - nominal_diskon

print("Subtotal =", subtotal)
print("Nominal Diskon=", nominal_diskon)
print("Total Bayar =", total_bayar)                                                                                                                          