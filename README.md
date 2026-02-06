# BigMart Sales Prediction 🛒

An end‑to‑end machine learning pipeline to predict sales for BigMart outlets.  
The project covers **data ingestion**, **processing**, **model training**, and **deployment** via a Streamlit app.

---

## 📥 Data Ingestion
- `df_item.xml` → stored in **MySQL: item_info**
- `df_outlet.xml` → stored in **MySQL: outlet_info**
- `df_sales.xml` → stored in **MySQL: sales_info**

---

## ⚙️ Data Processing
1. **Merge Tables**: Combine item, outlet, and sales data.  
2. **Cleaning & Feature Engineering**: Handle missing values, encode categorical variables, and create new features.  
3. **Train/Test Split**: Prepare datasets for model training and evaluation.  

---

## 🤖 Model Training
- Algorithm: **GradientBoostingRegressor**  
- Output: Trained model saved as `bigmart_best_model.pkl`  

---

## 🚀 Deployment
- **Streamlit Web Interface**: Interactive app for predictions.  
- **Predict Sales**: Input item/outlet details and get sales forecasts.  

---

## 📊 Tech Stack
- **Python** (pandas, scikit‑learn, Streamlit)  
- **MySQL** (data storage)  
- **Gradient Boosting** (machine learning model)  

---

## ▶️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/bigmart-sales-prediction.git
cd bigmart-sales-prediction
