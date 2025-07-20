# 🚗 Car Price Prediction App

[![Streamlit App](https://img.shields.io/badge/Live%20App-Click%20Here-brightgreen?logo=streamlit)](https://carpriceprediction-89rutxby2pr2iappcdqzvc.streamlit.app/)

A user-friendly web application to predict the selling price of a used car based on key features like present price, kilometers driven, fuel type, transmission type, seller type, ownership status, and year of purchase.

---

## 📌 Features

- ✅ Real-time car price prediction
- 🖱️ Easy-to-use sliders and dropdowns
- 📊 Predictive model powered by XGBoost
- 🌐 Live deployment on Streamlit Cloud
- 🔧 Fully customizable and extendable

---

## 🚀 Live Demo

🔗 **[Try the App](https://carpriceprediction-89rutxby2pr2iappcdqzvc.streamlit.app/)** – no installation required!

---

## 📁 Project Structure

```
car-price-prediction/
├── app.py                      # Streamlit web app
├── car_price_prediction.pkl    # Trained XGBoost model (serialized)
├── requirements.txt            # Project dependencies
└── README.md                   # Documentation
```

---

## 💡 How It Works

1. User inputs car details like:
   - Present price
   - Kilometers driven
   - Fuel type
   - Seller type
   - Transmission type
   - Ownership
   - Year of purchase

2. The app encodes the inputs and calculates car age

3. The trained model predicts the estimated selling price

---

## 📦 Installation Guide

To run this project locally:

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/your-username/car-price-prediction.git
cd car-price-prediction
```

### 2️⃣ Create a Virtual Environment (Optional)

```bash
python -m venv venv
.env\Scriptsctivate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Launch the App

```bash
streamlit run app.py
```

---

## 🔍 Input Feature Guide

| Feature         | Description                                 |
|----------------|---------------------------------------------|
| `Present_Price` | Current ex-showroom price in Lakhs          |
| `Kms_Driven`    | Distance driven by the car in kilometers     |
| `Fuel_Type`     | Type of fuel: Petrol, Diesel, or CNG         |
| `Seller_Type`   | Dealer or Individual                         |
| `Transmission`  | Manual or Automatic                          |
| `Owner`         | Number of previous owners (0–3)              |
| `Year`          | Year the car was purchased                   |

🧠 The model also calculates `car_age` from the year of purchase.

---

## 🤖 Model Details

- **Algorithm**: XGBoost Regressor
- **Library**: `xgboost`, `scikit-learn`, `joblib`
- **Training**: Handled offline and serialized using `joblib`

---

## 🔮 Future Improvements

- Add brand/model dropdowns
- Integrate advanced price analytics and charts
- Support batch prediction from CSV
- Display confidence intervals

---

## 🤝 Contributing

Pull requests and suggestions are welcome!

1. Fork this repo
2. Create your branch (`git checkout -b feature-x`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push (`git push origin feature-x`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more info.

---

## 🌟 Show Your Support

If you like this project:

- ⭐ Star this repository
- 📢 Share the app
- 🙋 Give feedback or suggest features

---

Made with ❤️ using [Streamlit](https://streamlit.io/)
