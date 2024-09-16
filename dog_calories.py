import streamlit as st
from collections import defaultdict

# Set Lists and Dictionary
age_list = ["Up to 4 Months","Over 4 Months Up to 18 Months", "Normal Neutered Adult","Intact Adult", "Obese Prone Adult","Weight Loss Adult"]
calc_list = [3,2,1.6,1.8,1.4,1]
calc_dict = {age_list[i]: calc_list[i] for i in range(len(age_list))}
size_list = ["Small", "Medium", "Large"]

# Calculate RER
def calculate_rer(dog_weight,dog_size):
    if dog_size == size_list[1]:
        return round((30 * dog_weight + 70), 2)
    else:
        return round((70 * (dog_weight**(3/4))),2)

# Calculate Growth DER & Maintenance DER 
def calculate_calories(dog_weight, dog_age, dog_size):
    dog_rer = calculate_rer(dog_weight,dog_size)
    return round(dog_rer * calc_dict[dog_age], 2)

# Set title     
st.title("PetCalulator :dog:")

# Display app description
st.caption("This application provides an estimated calculation of the daily caloric needs for your dog based on their age/condition, size and weight.")

# Display disclaimer
st.caption("Please Note: This estimate does not replace the professional health advice of a veterinarian.")

# Display input fields
dog_age = st.selectbox("Select your dog's age/condition", options=age_list,index=2)
dog_size = st.select_slider("Select your dog's size", options=size_list,value=size_list[1])
dog_weight = st.number_input("Enter your dog's current weight in kg", min_value=0.0, step=0.5, value=28.0)

# Calculate calories and display output
if st.button("Calculate"):
    calories = calculate_calories(dog_weight, dog_age, dog_size)
    if dog_age == age_list[0] or dog_age == age_list[1]:
        if dog_age == age_list[0] or dog_age == age_list[1]:
            st.markdown(f"<h3>Your dog's GER (Growth Energy Requirements) is <b>{calories}</b> calories per day.</h3>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h3>Your dog's DER (Daily Energy Requirements) is <b>{calories}</b> calories per day.</h3>", unsafe_allow_html=True)
