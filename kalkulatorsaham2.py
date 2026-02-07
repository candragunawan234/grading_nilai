import tkinter as tk
from tkinter import messagebox

def hitung_cuan():
    try:
        
        harga_beli = int(entry_beli.get())
        harga_jual = int(entry_jual.get())
        jumlah_lot = int(entry_lot.get())

        modal_mentah = harga_beli * jumlah_lot * 100
        fee_beli = modal_mentah * 0.0015
        total_modal = modal_mentah + fee_beli

        omzet_mentah = harga_jual * jumlah_lot * 100
        fee_jual = omzet_mentah * 0.0025
        pendapatan_bersih = omzet_mentah - fee_jual

        profit = pendapatan_bersih - total_modal
        persentase = (profit / total_modal) * 100

        hasil_text = f"Modal: Rp {total_modal:,.0f}\nCuan: Rp {profit:,.0f}\nPersentase: {persentase:.2f}%"
        label_hasil.config(text=hasil_text, fg="blue")

    except ValueError:
        messagebox.showerror("Error", "Masukin angka yang bener dong bos!")


window = tk.Tk()
window.title("Kalkulator Cuan Saham")
window.geometry("300x400") 

label1 = tk.Label(window, text="Harga Beli (per lembar):")
label1.pack(pady=5) # pack() itu buat naruh barangnya ke layar
entry_beli = tk.Entry(window)
entry_beli.pack(pady=5)

label2 = tk.Label(window, text="Harga Jual (per lembar):")
label2.pack(pady=5)
entry_jual = tk.Entry(window)
entry_jual.pack(pady=5)

label3 = tk.Label(window, text="Jumlah Lot:")
label3.pack(pady=5)
entry_lot = tk.Entry(window)
entry_lot.pack(pady=5)

tombol = tk.Button(window, text="HITUNG CUAN!", command=hitung_cuan, bg="green", fg="white")
tombol.pack(pady=20)

label_hasil = tk.Label(window, text="Hasil akan muncul di sini", font=("Arial", 12, "bold"))
label_hasil.pack(pady=10)

window.mainloop()