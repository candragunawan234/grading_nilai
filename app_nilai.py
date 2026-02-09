import streamlit as st
import pandas as pd
from fpdf import FPDF
import io

#Judul Website
st.set_page_config(page_title="Sistem Nilai SMK", page_icon="📊")

st.title("📊 Sistem Penilaian Siswa Otomatis")
st.write("Aplikasi khusus guru SMK Al Ittihad Mabdaul Ulum untuk grading cepat.")

#LOGIKA GRADING
def hitung_grade(nilai):
    if nilai >= 90: return "A", "LULUS"
    elif nilai >= 80: return "B", "LULUS"
    elif nilai >= 75: return "C", "LULUS"
    else: return "D", "REMEDIAL"

#FUNGSI GENERATE PDF
def generate_pdf(dataframe):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "LAPORAN HASIL PENILAIAN SISWA", ln=True, align="C")
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, "SMK AL - Ittihad Mabdaul Uluum" , ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Ringkasan Statistik:", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 10, f"Total Siswa: {len(dataframe)}", ln=True)
    pdf.cell(0, 10, f"Lulus: {len(dataframe[dataframe['Status'] == 'LULUS'])}", ln=True)
    pdf.cell(0, 10, f"Remedial: {len(dataframe[dataframe['Status'] == 'REMEDIAL'])}", ln=True)
    pdf.ln(10)  

    pdf.set_font("Arial", "B", 10)
    pdf.cell(60, 10, "Nama Siswa", 1)
    pdf.cell(30, 10, "Nilai", 1)
    pdf.cell(30, 10, "Grade", 1)
    pdf.cell(40, 10, "Status", 1)
    pdf.ln()

    for _, row in dataframe.iterrows():
        pdf.set_font("Arial", "", 10)
        pdf.cell(60, 10, str(row['Nama Siswa']), 1)
        pdf.cell(30, 10, str(row['Nilai']), 1)
        pdf.cell(30, 10, str(row['Grade']), 1)
        pdf.cell(40, 10, str(row['Status']), 1)
        pdf.ln()
    return pdf.output()

#SIDEBAR: DOWNLOAD TEMPLATE
st.sidebar.header("Template Nilai Siswa")
example_data = pd.DataFrame({
    "Nama Siswa": ["Budi", "Siti", "Joko"],
    "Nilai": [85, 92, 70]
})


csv_template = example_data.to_csv(index=False, sep=';', encoding='utf-8-sig').encode('utf-8-sig')

st.sidebar.download_button(
    label="📥 Download Template CSV", 
    data=csv_template, 
    file_name="template_siswa.csv",
    mime="text/csv"
)

#MAIN: UPLOAD
st.header("Upload Data")
uploaded_file = st.file_uploader("Pilih file CSV hasil edit kamu", type=["csv"])

if uploaded_file is not None:
    try:
       
        df = pd.read_csv(uploaded_file, sep=';', encoding='utf-8-sig')
        
        # Cek apakah kolom Nilai ada 
        if "Nilai" in df.columns:
            #PROSES DATA
            df = df.drop_duplicates() # Hapus data ganda
            
            # Terapkan rumus grading ke setiap baris
            df[['Grade', 'Status']] = df.apply(
                lambda x: pd.Series(hitung_grade(x['Nilai'])), axis=1
            )

            #TAMPILAN DASHBOARD (METRICS)
            st.header("📊 Ringkasan Nilai")
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Siswa", len(df))
            col2.metric("Lulus", len(df[df['Status'] == 'LULUS']))
            col3.metric("Remedial", len(df[df['Status'] == 'REMEDIAL']))

            #GRAFIK DISTRIBUSI GRADE
            st.subheader("📈 Distribusi Grade")
            if not df.empty:
                grade_counts = df['Grade'].value_counts().sort_index()
                st.bar_chart(grade_counts, color="#3498db")

            #TABEL HASIL DENGAN WARNA
            st.header("📋 Daftar Hasil Grading")
            
            # Fungsi warna: Merah untuk Remedial, Hijau untuk Lulus
            def style_status(val):
                color = '#ff4b4b' if val == 'REMEDIAL' else '#2ecc71'
                return f'background-color: {color}; color: white; font-weight: bold'

            # Terapkan warna
            styled_df = df.style.applymap(style_status, subset=['Status'])
            st.dataframe(styled_df, use_container_width=True)
            
            #TOMBOL DOWNLOAD HASIL
            hasil_csv = df.to_csv(index=False, sep=';', encoding='utf-8-sig').encode('utf-8-sig')
            st.download_button(
                label="💾 Download Hasil Jadi (CSV)",
                data=hasil_csv,
                file_name="hasil_penilaian_lengkap.csv",
                mime="text/csv"
            )
        else:
            st.error("❌ Kolom 'Nilai' tidak ditemukan! Pastikan pakai template yang benar.")
            st.write(f"Kolom yang terbaca: {list(df.columns)}")

    except Exception as e:
        st.error("❌ Terjadi Kesalahan Membaca File!")
        st.write(f"Detail Error: {e}")