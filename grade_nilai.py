import tkinter as tk
from tkinter import filedialog, messagebox
import csv
from pathlib import Path

# ===== LOGIKA PROGRAM =====
data_laporan = []

def hitung_grade(nilai):
    if nilai >= 90: return "A", "LULUS"
    elif nilai >= 80: return "B", "LULUS"
    elif nilai >= 75: return "C", "LULUS"
    else: return "D", "REMEDIAL"

def buat_template():
    filepath = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=(("CSV Files", "*.csv"),),
        initialfile="template_nilai_siswa.csv",
        title="Simpan Template CSV"
    )
    if filepath:
        try:
            with open(filepath, mode='w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(["Nama Siswa", "Nilai Angka"])
                writer.writerow(["Budi Santoso", "85"])
                writer.writerow(["Siti Aminah", "92"])
            messagebox.showinfo("Sukses", "Template dibuat! Silakan isi di Excel.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal: {e}")

def upload_file():
    global data_laporan
    filepath = filedialog.askopenfilename(title="Pilih File CSV", filetypes=(("CSV Files", "*.csv"),))
    if not filepath: return

    data_laporan = []
    try:
        with open(filepath, mode='r', encoding='utf-8-sig') as file:
            # Deteksi otomatis pemisah (koma atau titik koma)
            sample = file.readline()
            file.seek(0)
            pemisah = ';' if ';' in sample else ','
            
            csv_reader = csv.reader(file, delimiter=pemisah)
            next(csv_reader, None) # Skip header
            
            hasil = []
            for row in csv_reader:
                if len(row) >= 2:
                    nama = row[0].strip()
                    nilai_str = "".join(filter(str.isdigit, row[1]))
                    if nilai_str:
                        nilai = int(nilai_str)
                        grade, status = hitung_grade(nilai)
                        data_laporan.append([nama, nilai, grade, status])
                        hasil.append(f"✓ {nama} -> {grade} ({status})")

        text_hasil.config(state=tk.NORMAL)
        text_hasil.delete("1.0", tk.END)
        text_hasil.insert(tk.END, "\n".join(hasil))
        text_hasil.config(state=tk.DISABLED)
        
        # AKTIFKAN TOMBOL DOWNLOAD
        btn_download.config(state=tk.NORMAL, bg="#27ae60")
        messagebox.showinfo("Sukses", f"Berhasil memproses {len(data_laporan)} siswa.")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal baca: {e}")

def download_file():
    if not data_laporan: return
    filepath = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=(("CSV Files", "*.csv"),),
        initialfile="hasil_grading.csv",
        title="Simpan Hasil"
    )
    if filepath:
        try:
            with open(filepath, mode='w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(["Nama", "Nilai", "Grade", "Status"])
                writer.writerows(data_laporan)
            messagebox.showinfo("Berhasil", "Hasil grading sudah disimpan!")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal simpan: {e}")

# ===== TAMPILAN GUI =====
window = tk.Tk()
window.title("Sistem Penilaian Siswa")
window.geometry("600x700")
window.config(bg="#ecf0f1")

# 1. HEADER
tk.Label(window, text="SISTEM PENILAIAN OTOMATIS", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white", pady=20).pack(fill=tk.X)

# 2. FRAME DOWNLOAD (Dipaku di bawah agar tidak hilang)
download_frame = tk.Frame(window, bg="white", pady=10)
download_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=10)
btn_download = tk.Button(download_frame, text="DOWNLOAD HASIL", command=download_file, bg="#95a5a6", fg="white", state=tk.DISABLED, font=("Arial", 10, "bold"), pady=10)
btn_download.pack(fill=tk.X)

# 3. SECTION TEMPLATE & UPLOAD
top_frame = tk.Frame(window, bg="#ecf0f1")
top_frame.pack(side=tk.TOP, fill=tk.X, padx=20, pady=10)

tk.Button(top_frame, text="1. BUAT TEMPLATE CSV", command=buat_template, bg="#f39c12", fg="white", pady=10).pack(fill=tk.X, pady=5)
tk.Button(top_frame, text="2. UPLOAD DATA SISWA", command=upload_file, bg="#3498db", fg="white", font=("Arial", 10, "bold"), pady=10).pack(fill=tk.X, pady=5)

# 4. AREA HASIL (Sisanya dipakai untuk ini)
hasil_label = tk.Label(window, text="HASIL PROSES GRADING:", bg="#ecf0f1", font=("Arial", 10, "bold"))
hasil_label.pack(anchor=tk.W, padx=20)

text_hasil = tk.Text(window, height=10, bg="white", padx=10, pady=10)
text_hasil.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
text_hasil.insert(tk.END, "Belum ada data...")
text_hasil.config(state=tk.DISABLED)

window.mainloop()