# 🎓 Prediksi Kelulusan Mahasiswa

Proyek ini dibuat untuk latihan data science sederhana — memprediksi apakah mahasiswa **lulus (1)** atau **tidak lulus (0)** berdasarkan IPK, absensi, dan waktu belajar.

---

---

## 🚀 Langkah Menjalankan Proyek

### **1️⃣ Clone Repository**
```
git clone https://github.com/0xRopik/pertemuan5
cd pertemuan5
```
2️⃣ Install Dependencies
Gunakan virtual environment atau langsung:
```
pip install -r requirements.txt
```
🧠 Jalankan Analisis (di Jupyter / Colab)
Langkah-langkah:
Buka model_kelulusan.ipynb
Jalankan sel secara berurutan:
Load dataset
Cleaning dan EDA
Split dataset
Training model
Evaluasi model (Confusion Matrix, ROC Curve)

Setelah selesai, file model.pkl dan roc_test.png akan otomatis dibuat.

💻 Menjalankan API (Opsional)
```

python app.py
Kemudian buka di browser:

http://127.0.0.1:5000/
Kirim data JSON via Postman:

{
  "IPK": 3.4,
  "Jumlah_Absensi": 5,
  "Waktu_Belajar_Jam": 8,
  "Rasio_Absensi": 0.35,
  "IPK_x_Study": 27.2
}
```

📊 Output yang Dihasilkan
✅ File processed_kelulusan.csv (data bersih)
✅ Visualisasi EDA (Heatmap, Histogram)
✅ Model Machine Learning Logistic Regression (model.pkl)
✅ Grafik ROC-AUC (roc_test.png)
✅ API Prediksi Sederhana (app.py)

🧾 Penulis
Nama: Muhamad Ropik
