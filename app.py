import streamlit as st

# Title
st.title("Mechanical Unit Converter and Material Density Checker")

# Your Information
st.write("Name: TAUFEEQ ULLAH")
st.write("Roll Number: 25-ME-160")

# ---------------- UNIT CONVERTER ----------------

st.header("Mechanical Unit Converter")

conversion = st.selectbox(
    "Choose Conversion",
    ["Meter to Centimeter", "Kilogram to Gram", "Celsius to Fahrenheit"]
)

value = st.number_input("Enter Value")

if conversion == "Meter to Centimeter":
    result = value * 100
    st.success(f"Result: {result} cm")

elif conversion == "Kilogram to Gram":
    result = value * 1000
    st.success(f"Result: {result} g")

elif conversion == "Celsius to Fahrenheit":
    result = (value * 9/5) + 32
    st.success(f"Result: {result} °F")

# ---------------- DENSITY CHECKER ----------------

st.header("Material Density Checker")

material = st.selectbox(
    "Choose Material",
    ["Steel", "Aluminum", "Copper"]
)

densities = {
    "Steel": "7850 kg/m³",
    "Aluminum": "2700 kg/m³",
    "Copper": "8960 kg/m³"
}

st.info(f"Density of {material}: {densities[material]}")
