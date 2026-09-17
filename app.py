import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Equipment Value Calculator",
    layout="wide"
)


# -------------------------
# LOAD MODEL
# -------------------------

@st.cache_resource
def load_model():
    return joblib.load("model/residual_value_model.joblib")


@st.cache_data
def load_classes():
    return pd.read_csv(
        "model/equipment_classes.csv",
        header=None
    )[0].tolist()


model = load_model()
classes = load_classes()


# -------------------------
# PAGE
# -------------------------

st.title("Heavy Equipment Value Calculator")

st.write(
    """
    Estimate the residual auction value of heavy equipment
    based on equipment class, age, and operating hours.
    """
)


# -------------------------
# INPUTS
# -------------------------

equipment_class = st.selectbox(
    "Equipment type and size",
    classes
)

age = st.slider(
    "Equipment age (years)",
    min_value=0,
    max_value=40,
    value=8,
    step=1
)

hours = st.slider(
    "Current operating hours",
    min_value=1,
    max_value=30000,
    value=5000,
    step=250
)


# -------------------------
# BUILD MODEL INPUT
# -------------------------

input_df = pd.DataFrame({
    "fiProductClassDesc": [equipment_class],
    "sale_year": [2012],
    "equipment_age": [age],
    "age_squared": [age ** 2],
    "log_machine_hours": [np.log1p(hours)]
})


# -------------------------
# PREDICTION
# -------------------------

log_prediction = model.predict(input_df)[0]

predicted_value = np.expm1(log_prediction)


# -------------------------
# DISPLAY RESULT
# -------------------------

st.subheader("Estimated residual value")

st.metric(
    "Estimated auction value",
    f"${predicted_value:,.0f}"
)

st.caption(
    "Estimate is based on historical heavy-equipment auction data."
)
