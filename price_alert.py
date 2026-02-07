def price_alert(nama, harga_skr, harga_trgt):
    print(f"\n--- Peringatan Harga Saham {nama} ---")

    if harga_skr <= harga_trgt:
        return f"Hudang!! {nama} udah nyentuh {harga_skr}. Saatnya Serok!!!"
    else:
        selisih = harga_skr - harga_trgt
        return f"cill, {nama} masih dipucuk, kurang {selisih} Lagi, Santai Kawan!!"
    

saham_target = input("Nama Saham: ")
harga_input = int(input("Harga Saat Ini: "))
target_input = int(input("Target beli: "))


Hasil = price_alert(saham_target, harga_input, target_input)
print(Hasil)