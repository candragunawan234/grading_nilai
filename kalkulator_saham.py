def hitung_cuan():
    print("=== Kalkulator Cuan Saham ===")

    harga_beli = int(input("Harga Beli (Per Lembar): "))
    harga_jual = int(input("Harga Jual (Per Lembar): "))
    jumlah_lot = int(input("Jumlah Lot: "))

    modal_mentah = harga_beli * jumlah_lot * 100
    fee_beli = modal_mentah * 0.0015
    total_modal = modal_mentah + fee_beli

    omzet_mentah = harga_jual * jumlah_lot * 100
    fee_jual = omzet_mentah * 0.0025
    pendapatan_bersih = omzet_mentah - fee_jual

    profit = pendapatan_bersih - total_modal
    persentase = (profit / total_modal)

    print("-" * 30)
    print(f"Total Modal(inc. fee): Rp {total_modal:,.0f}")
    print(f"Proft bersih         : Rp {profit:,.0f} ")
    print(f"Prsentase Cuan       : Rp { persentase:.2f}% ")

hitung_cuan()
hitung_cuan()