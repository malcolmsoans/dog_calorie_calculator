import streamlit as st
from collections import defaultdict

# Set Lists for Body Condition, Neutered Status, and Age
body_condition_list = ["Healthy", "Obese Prone", "Weight Loss"]
neutered_status_list = ["Neutered", "Intact"]
age_list = ["Up to 4 Months", "4 to 18 Months", "Adult"]

# Multipliers for Calories Based on Condition
calc_dict = {
    ("Healthy", "Neutered", "Adult"): 1.6,
    ("Healthy", "Intact", "Adult"): 1.8,
    ("Obese Prone", "Neutered", "Adult"): 1.4,
    ("Weight Loss", "Neutered", "Adult"): 1.0,
    ("Healthy", "Neutered", "Puppy (Up to 4 Months)"): 3.0,
    ("Healthy", "Neutered", "Puppy (4 to 18 Months)"): 2.0,
}

# Set Size List
size_list = ["Small", "Medium", "Large"]

# Activity Level
activity_list = ["Low", "Medium", "High"]
activity_dict = {"Low": 1.0, "Medium": 1.2, "High": 1.4}

# Function to Calculate RER (Resting Energy Requirement) based on size
def calculate_rer(dog_weight, dog_size, activity_level):
    if dog_size == "Medium":
        rer = round((30 * dog_weight + 70), 2)
    else:
        rer = round((70 * (dog_weight ** (3 / 4))), 2)
    
    # Apply activity level adjustment
    return rer * activity_dict[activity_level]

# Function to Calculate Calories
def calculate_calories(dog_weight, body_condition, neutered_status, age, dog_size, activity_level):
    dog_rer = calculate_rer(dog_weight, dog_size, activity_level)
    # Default multiplier if condition is not found
    multiplier = calc_dict.get((body_condition, neutered_status, age), 1.6)
    return round(dog_rer * multiplier, 2)

# App Title     
st.title("Calculate Calories for Your 🐕")

# Display App Description
st.caption("This application provides an estimated calculation of the daily caloric needs for your dog based on their body condition, neutered status, age, size, weight, and activity level.")

# Display Disclaimer
st.caption("Please Note: This estimate does not replace the professional health advice of a veterinarian.")

# Input Fields
body_condition = st.selectbox("Select your dog's body condition", options=body_condition_list, index=0)
neutered_status = st.selectbox("Select your dog's neutered status", options=neutered_status_list, index=0)
age = st.selectbox("Select your dog's age", options=age_list, index=2)
dog_size = st.select_slider("Select your dog's size", options=size_list, value=size_list[1])
dog_weight = st.number_input("Enter your dog's current weight in kg", min_value=0.0, step=0.5, value=28.0)
activity_level = st.selectbox("Select your dog's activity level", options=activity_list, index=1)

# Calculate Button
if st.button("Calculate"):
    if dog_weight <= 0:
        st.error("Please enter a valid weight greater than 0.")
    else:
        calories = calculate_calories(dog_weight, body_condition, neutered_status, age, dog_size, activity_level)
        if age == age_list[0] or age == age_list[1]:
            st.markdown(f"<div style='background-color: #ffcccb; padding: 10px; border-radius: 10px;'><h3>Your dog's GER (Growth Energy Requirements) is <b>{calories}</b> calories per day.</h3></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='background-color: #ffcccb; padding: 10px; border-radius: 10px;'><h3>Your dog's DER (Daily Energy Requirements) is <b>{calories}</b> calories per day.</h3></div>", unsafe_allow_html=True)
