import streamlit as st
import pandas as pd
import pickle

# === Page Setup ===
st.set_page_config(
    page_title="BigMart Sales Predictor by Sanket",
    page_icon="🛒",
    layout="centered"
)

# === Load Model and Version Info ===
with open("bigmart_best_model.pkl", "rb") as f:
    model, sklearn_version = pickle.load(f)

# === Title & Intro ===
st.title("🛒 BigMart Sales Prediction App")
st.markdown(f"Using **scikit-learn v{sklearn_version}** model to predict item sales.")
st.markdown("Fill in the details below and click **Predict Sales** to estimate item outlet sales.")

st.divider()

# === Layout: Two Sections ===
st.header("📊 Item Details")
col1, col2 = st.columns(2)

with col1:
    Item_Identifier = st.text_input("Item Identifier", "FDA15")
    Item_Weight = st.number_input("Item Weight", min_value=0.0, value=12.5)
    Item_Fat_Content = st.selectbox("Item Fat Content", ["Low Fat", "Regular"])
    Item_Visibility = st.slider("Item Visibility", min_value=0.0, max_value=0.3, step=0.01, value=0.1)

with col2:
    Item_Type = st.selectbox("Item Type", [
        "Dairy", "Soft Drinks", "Meat", "Fruits and Vegetables", "Household",
        "Baking Goods", "Snack Foods", "Frozen Foods", "Breakfast",
        "Health and Hygiene", "Hard Drinks", "Canned", "Breads",
        "Starchy Foods", "Others", "Seafood"
    ])
    Item_MRP = st.number_input("Item MRP", min_value=0.0, value=150.0)

st.divider()

st.header("🏬 Outlet Details")
col3, col4 = st.columns(2)

with col3:
    Outlet_Identifier = st.selectbox("Outlet Identifier", [
        "OUT027", "OUT013", "OUT049", "OUT035", "OUT046",
        "OUT017", "OUT045", "OUT018", "OUT019", "OUT010"
    ])
    Outlet_Size = st.selectbox("Outlet Size", ["Small", "Medium", "High"])
    Outlet_Location_Type = st.selectbox("Outlet Location Type", ["Tier 1", "Tier 2", "Tier 3"])

with col4:
    Outlet_Type = st.selectbox("Outlet Type", [
        "Supermarket Type1", "Supermarket Type2",
        "Supermarket Type3", "Grocery Store"
    ])
    Outlet_Age = st.slider("Outlet Age (Years)", 0, 40, 15)

st.divider()

# === Predict Button ===
if st.button("🚀 Predict Sales"):
    input_df = pd.DataFrame([{
        "Item_Identifier": Item_Identifier,
        "Item_Weight": Item_Weight,
        "Item_Fat_Content": Item_Fat_Content,
        "Item_Visibility": Item_Visibility,
        "Item_Type": Item_Type,
        "Item_MRP": Item_MRP,
        "Outlet_Identifier": Outlet_Identifier,
        "Outlet_Size": Outlet_Size,
        "Outlet_Location_Type": Outlet_Location_Type,
        "Outlet_Type": Outlet_Type,
        "Outlet_Age": Outlet_Age
    }])

    prediction = model.predict(input_df)[0]
    st.success(f"✅ Predicted Item Outlet Sales: ₹{prediction:.2f}")

    # Optional: Show input summary
    st.markdown("### 🔎 Input Summary")
    st.dataframe(input_df)

st.markdown("---")
st.caption("Built with ❤️ by sanket using Streamlit and scikit-learn")