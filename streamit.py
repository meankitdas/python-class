import streamlit as st


def calculate_bmi(weight, height, unit):
    if unit == "meters":
        bmi = weight / (height**2)
    elif unit == "centimeters":
        bmi = weight / ((height/100)**2)
    elif unit == "feet":
        bmi = weight / ((height * 0.3048)**2)
    return bmi


st.title("Welcome to BMI Calculator")

weight = st.number_input("Weight (kgs)", min_value=0.0, value=70.0)

unit = st.radio("Select your height format:", ["meters", "centimeters", "feet"])

if unit == "meters":
    height = st.number_input("Meters", min_value=0.0, value=1.70)
elif unit == "centimeters":
    height = st.number_input("Centimeters", min_value=0.0, value=170.0)
else:
    height = st.number_input("Feet", min_value=0.0, value=5.58)

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height, unit)
    st.write("Your BMI Index is:", bmi)

    if bmi < 18.5:
        st.error("Underweight")
    elif bmi >= 18.5 and bmi < 25:
        st.success("Normal weight")
    elif bmi >= 25 and bmi < 30:
        st.error("Overweight")
    else:
        st.error("Obesity")
