# 🚲 Bike Sharing Analysis Dashboard

Proyek ini adalah aplikasi dashboard interaktif yang dibangun menggunakan **Streamlit** untuk menganalisis data penyewaan sepeda. Fokus utama analisis ini adalah melihat tren pertumbuhan bisnis pada tahun 2012 dan membandingkan profil pengguna pada hari kerja vs hari libur di tahun 2011.

## 📂 Struktur Direktori

```text
.
├── dashboard.py
├── main_data.csv
├── day.csv
├── hour.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt

```

## 🚀 Fitur Utama Dashboard
Dashboard ini menyajikan insight mendalam melalui:
1.  **Business Overview**: Ringkasan performa total penyewaan dan pertumbuhan tahunan.
2.  **Monthly Trends (2012)**: Visualisasi tren bulanan untuk menentukan periode performa bisnis terbaik (Peak Season).
3.  **Working Day vs Holiday (2011)**: Analisis perbandingan untuk memahami karakteristik utama pengguna sepeda (Komuter vs Rekreasi).
4.  **Analisis RFM**: Statistik lanjutan berdasarkan Recency, Frequency, dan Monetary per tahun.
5.  **Action Items**: Rekomendasi strategis berbasis data untuk manajemen operasional dan pemasaran.

## 🛠️ Cara Menjalankan Dashboard

### 1. Prasyarat
Pastikan Anda telah menginstal **Python (versi 3.9 ke atas)** di perangkat Anda.

### 2. Instalasi Library
Buka terminal atau command prompt, lalu instal pustaka yang diperlukan dengan menjalankan:
```bash
pip install -r requirements.txt
```
---
 (Harus ada baris kosong di sini)
### 3. Menyiapkan Main Data
# Jalankan ini di notebook Anda
day_df.to_csv("dashboard/main_data.csv", index=False)

### 4. Menjalankan Aplikasi
```bash
streamlit run dashboard/dashboard.py
```
---

## Kesimpulan Analisis
1. **Tren Bisnis:** Penjualan mencapai titik tertinggi pada bulan September 2012, menunjukkan adanya pengaruh musiman yang kuat.
2. **Profil Pengguna:** Mayoritas penyewaan terjadi pada Hari Kerja, mengindikasikan bahwa sepeda digunakan sebagai alat transportasi utama menuju tempat aktivitas harian.
3. **Pertumbuhan:** Terjadi peningkatan volume penyewaan yang signifikan sebesar 64.8% dari tahun 2011 ke 2012.
