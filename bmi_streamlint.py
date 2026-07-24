import streamlit as st


#title
st.title('BMI Calculator')
st.write("This BMI calculator allows you to input your weight and height to calculate your Body Mass Index (BMI).")

#get input from user
weight = st.number_input("Enter your weight (in kg):", min_value=1.0, max_value=300.0, value=70.0)
height = st.number_input("Enter your height (in cm):", min_value=50.0, max_value=250.0, value=170.0)

#button to calculate BMI
if st.button("Calculate BMI"):
    #calculate BMI
    height_m = height / 100  # convert height to meters
    bmi = weight / (height_m ** 2)

    #display result
    st.write(f"Your BMI is: {bmi:.2f}")

    #determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"

    st.write(f"You are classified as: {category}")