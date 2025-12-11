# 🚗 Car Price Prediction API (FastAPI + Machine Learning)

Proyek ini adalah **REST API sederhana** menggunakan **FastAPI** untuk memprediksi harga mobil berdasarkan fitur-fitur tertentu seperti harga awal, kilometer tempuh, umur kendaraan, jumlah pemilik sebelumnya, dan jenis bahan bakar.

Model yang digunakan: **Ridge Regression** (disimpan dalam file `ridge.pkl`).

---

## 📌 Fitur Utama
- Prediksi harga mobil dalam **satuan Lakhs (Lacs)**.
- Konversi otomatis dari **Lacs → Rupee → Rupiah**.
- Endpoint API yang simple dan cepat.
- Sudah include **CORS Middleware**.
- Bisa diakses langsung lewat **Swagger UI**.

---

## 📁 Struktur Folder

```
project/
│── main.py
│── model/
│     └── ridge.pkl
│── static/        (opsional, jika ingin pakai frontend)
│── requirements.txt
└── README.md
```

---

## 🛠️ Instalasi & Setup

### 1️⃣ Clone Repo
```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

### 2️⃣ Buat Virtual Environment
```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

Jika tidak ada `requirements.txt`, install manual:
```bash
pip install fastapi uvicorn scikit-learn numpy pandas
```

---

## 🚀 Menjalankan Server

```
uvicorn main:app --reload
```

Server akan berjalan di:

```
http://localhost:8000
```

Swagger UI otomatis tersedia di:

```
http://localhost:8000/docs
```

---

## 🔮 Cara Pakai (Testing di Swagger)

1. Buka browser → `http://localhost:8000/docs`
2. Pilih endpoint:

```
POST /predict
```

3. Input field seperti:

```json
{
  "Present_Price": 5.59,
  "Kms_Driven": 27000,
  "Past_Owners": 0,
  "Age": 6,
  "Fuel_Type_Diesel": false,
  "Fuel_Type_Petrol": true,
  "Seller_Type_Individual": false,
  "Transmission_Manual": true
}
```

4. Klik **Execute**, dan API akan mengembalikan:

```json
{
  "predicted_price_lacs": 0.63,
  "predicted_price_rupiah": 11970000
}
```

---

## 📦 Deployment (Opsional)

- Bisa deploy ke **Railway**, **Render**, atau **VPS** (Gunicorn/Uvicorn).
- Bisa juga ditambah FE pakai HTML + Bootstrap (opsional).

---

## 👤 Author
**Ahmad Harun**  
AI Engineer

---

## 📝 License
Bebas digunakan untuk belajar dan pengembangan pribadi.
