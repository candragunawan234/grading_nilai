import tkinter as tk
from tkinter import messagebox

def cek_nilai():
    try:
        nama = entry_nama.get()
        nilai = int(entry_nilai.get())

        if nilai >= 90:
            grade = "A"
            status = "Lulus, Pertahankan!"
            warna = "green"
        elif nilai >= 80:
            grade = "B"
            status = "Lulus, Bisa Lebih Baik Lagi!"
            warna = "blue"
        elif nilai >= 75:
            grade = "C"
            status = "Lulus, Pas KKM!"
            warna = "yellow"
        else:
            grade = "D"
            status = "Remedial, Hubungi Guru Bersangkutan!"
            warna = "red"

        hasil_text = f"Nama: {nama}\nNilai: {nilai}\nGrade: {grade}\n{status}"
        label_hasil.config(text=hasil_text, fg=warna)

    except ValueError:
        messagebox.showerror("Error", "Masukin Angka Yang Bener!!")


window = tk.Tk()
window.title("Cek Grade nilai Siswa")
window.geometry("300x350")

judul = tk.Label(window, text="Masukan Nilai Siswa", font=("Arial", 14, "bold"))
judul.pack(pady=10)

label1 = tk.Label(window, text="Nama Siswa: ")
label1.pack()
entry_nama = tk.Entry(window)
entry_nama.pack(pady=5)

label2 = tk.Label(window, text = "Masukan Nilai (1-100): ")
label2.pack()
entry_nilai = tk.Entry(window)
entry_nilai.pack(pady=5)

tombol = tk.Button(window, text="Cek Grade!!", command=cek_nilai, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
tombol.pack(pady=20)

label_hasil = tk.Label(window, text="Hasil......", font=("Arial", 12, "bold"))
label_hasil.pack(pady=10)

window.mainloop()