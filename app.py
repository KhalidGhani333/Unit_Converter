import streamlit as st

# Title
st.title("🔄 Unit Converter")

# Define conversion 
conversion = {
    "Length": {
        "Metre": 1,"Kilometre": 1000, "Centimetre": 0.01, "Millimetre": 0.001,
        "Micrometre": 1e-6, "Nanometre": 1e-9, "Mile": 1609.34, "Yard": 0.9144,
        "Foot": 0.3048, "Inch": 0.0254, "Nautical Mile": 1852
    },
    "Mass": {
        "Kilogram": 1, "Gram": 0.001, "Milligram": 0.000001, "Metric Ton": 1000,
        "Pound": 0.453592, "Ounce": 0.0283495
    },
    "Area": {
        "Square Metre": 1, "Square Kilometre": 1_000_000, "Square Centimetre": 0.0001,
        "Square Millimetre": 0.000001, "Hectare": 10_000, "Acre": 4046.86
    },
    "Speed": {
        "Metre per Second": 1, "Kilometre per Hour": 0.277778, "Mile per Hour": 0.44704,
        "Foot per Second": 0.3048, "Knot": 0.514444
    },
    "Time": {
        "Second": 1, "Minute": 60, "Hour": 3600, "Day": 86400, "Week": 604800
    },
    "Volume": {
        "Cubic Metre": 1, "Litre": 0.001, "Millilitre": 0.000001, "Gallon (US)": 0.00378541,
        "Gallon (UK)": 0.00454609, "Cubic Inch": 0.000016387, "Cubic Foot": 0.0283168
    }
}

# Function to convert
def convert_units(value, from_unit, to_unit, category):
    if category not in conversion:
        return None
    
    units = conversion[category]
    if from_unit not in units or to_unit not in units:
        return None
    
    # Convert to base unit and then to the target unit
    value_in_base = value * units[from_unit]
    converted_value = value_in_base / units[to_unit]
    return converted_value

# User input section
category = st.selectbox("Select Category:", list(conversion.keys()))
units = list(conversion[category].keys())

# Layout
col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("From Unit:", units)
    value = st.number_input("Enter value:", min_value=0.0, format="%f")

with col2:
    to_unit = st.selectbox("To Unit:", units)
    converted = convert_units(value, from_unit, to_unit, category)
    
    # Display result
    st.text_input("Converted Value:", converted) 
