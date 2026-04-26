import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# ==========================================
# 1. KONFIGURASI HALAMAN & STYLE
# ==========================================
st.set_page_config(
    page_title="Bike Sharing Dashboard 2026",
    page_icon="🚲",
    layout="wide"
)

# Judul Utama dengan Gaya
st.markdown("<h1 style='text-align: center;'>🚲 Bike Sharing Interactive Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# 2. LOAD & CLEANING DATA (Sesuai Kodingan Kamu)
# ==========================================
@st.cache_data
def load_data():
    day_df = pd.read_csv("day.csv")
    day_df["dteday"] = pd.to_datetime(day_df["dteday"])
    return day_df

day_df = load_data()

# ==========================================
# 3. SIDEBAR FEATURE (Fitur Filter)
# ==========================================
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1507035895480-2b3156c31fc8?q=80&w=500&auto=format&fit=crop")
    st.title("Filter Control")
    
    # Filter Tahun
    year_options = ["Semua Tahun", "2011", "2012"]
    selected_year = st.selectbox("Pilih Tahun Analisis:", year_options)
    
    st.markdown("---")
    st.write("**Analyst:** Nayza Azura Putri")
    st.write("**Date:** April 2026")

# Logika Filter
if selected_year == "2011":
    filtered_df = day_df[day_df["yr"] == 0]
elif selected_year == "2012":
    filtered_df = day_df[day_df["yr"] == 1]
else:
    filtered_df = day_df

# ==========================================
# 4. METRIC FEATURE (Key Performance Indicators)
# ==========================================
total_rental = filtered_df['cnt'].sum()
avg_rental = int(filtered_df['cnt'].mean())
max_rental = filtered_df['cnt'].max()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Penyewaan", f"{total_rental:,}")
with col2:
    st.metric("Rata-rata Harian", f"{avg_rental:,}")
with col3:
    st.metric("Rekor Sewa Tertinggi", f"{max_rental:,}")

st.markdown("---")

# ==========================================
# 5. VISUALISASI PERTANYAAN 1 (Line Chart)
# ==========================================
st.subheader("📊 Tren Penyewaan Bulanan (Tahun 2012)")

# Filter 2012 sesuai kodingan asli
day_2012_df = day_df[day_df["yr"] == 1]
monthly_rent_2012 = day_2012_df.groupby(by="mnth").agg({"cnt": "sum"}).reset_index()
monthly_rent_2012["mnth"] = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

fig1, ax1 = plt.subplots(figsize=(12, 5))
sns.lineplot(x="mnth", y="cnt", data=monthly_rent_2012, marker="o", color="#3498db", linewidth=2.5, ax=ax1)
ax1.set_ylabel("Total Penyewaan")
ax1.grid(True, alpha=0.3)
st.pyplot(fig1)

with st.expander("Klik untuk melihat tabel data bulanan"):
    st.dataframe(monthly_rent_2012, use_container_width=True)

st.markdown("---")

# ==========================================
# 6. VISUALISASI PERTANYAAN 2 (Bar Chart)
# ==========================================
st.subheader("📊 Perbandingan Hari Kerja vs Hari Libur (Tahun 2011)")

# Filter 2011 sesuai kodingan asli
day_2011_df = day_df[day_df["yr"] == 0]
workingday_rent_2011 = day_2011_df.groupby(by="workingday").agg({"cnt": "mean"}).reset_index()
workingday_rent_2011["workingday"] = workingday_rent_2011["workingday"].replace({0: "Holiday/Weekend", 1: "Working Day"})

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(x="workingday", y="cnt", data=workingday_rent_2011, palette=["#e74c3c", "#2ecc71"], ax=ax2)
ax2.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig2)

# Fitur Download Tabel
st.download_button(
    label="Download Data Perbandingan (CSV)",
    data=workingday_rent_2011.to_csv(index=False),
    file_name='perbandingan_hari_2011.csv',
    mime='text/csv',
)

st.markdown("---")

# ==========================================
# 7. ANALISIS RFM & REKOMENDASI (Fitur Box Warna)
# ==========================================
st.subheader("💡 Business Insights & Recommendations")

# Tabel RFM (Sesuai kodingan asli)
recent_date = day_df['dteday'].max()
rfm_df = day_df.groupby(by="yr", as_index=False).agg({
    "dteday": lambda x: (recent_date - x.max()).days,
    "instant": "count",
    "cnt": "sum"
})
rfm_df.columns = ["yr", "recency", "frequency", "monetary"]
rfm_df["yr"] = rfm_df["yr"].replace({0: "2011", 1: "2012"})

col_a, col_b = st.columns([1, 1])

with col_a:
    st.write("**Statistik RFM per Tahun:**")
    st.table(rfm_df)

with col_b:
    st.success("**Rekomendasi Action Item:**")
    st.markdown("""
    * **Scale Up:** Tingkatkan armada di kuartal 3 (Puncak September).
    * **Retention:** Buat program loyalitas untuk pengguna hari kerja.
    * **Promo:** Diskon khusus akhir pekan untuk menyeimbangkan bar hari libur.
    * **Maintenance:** Servis armada di bulan Januari-Februari.
    """)

st.caption("Dashboard Created by Nayza | Data Source: Bike Sharing Dataset")