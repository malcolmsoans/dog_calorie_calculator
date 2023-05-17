import streamlit as st
from collections import defaultdict

age_list = ["Up to 4 Months","Over 4 Months Up to 18 Months", "Normal Neutered Adult","Intact Adult", "Obese Prone Adult","Weight Loss Adult"]
calc_list = [3,2,1.6,1.8,1.4,1]
calc_dict = {age_list[i]: calc_list[i] for i in range(len(age_list))}
size_list = ["Small", "Medium", "Large"]

def calculate_rer(dog_weight,dog_size):
    if dog_size == size_list[1]:
        return round((30 * dog_weight + 70), 2)
    else:
        return round((70 * (dog_weight**(3/4))),2)
 
def calculate_calories(dog_weight, dog_age, dog_size):
    dog_rer = calculate_rer(dog_weight,dog_size)
    return round(dog_rer * calc_dict[dog_age], 2)
     


st.title("Calculate calories for your :dog:")

st.write(f"""This application calculates the daily caloric needs for your dog based on their age/condition, size and weight.\n
         Please Note: This is an estimate and does not replace professional health advice.""")


dog_age = st.selectbox("Select your dog's age/condition", options=age_list,index=1)

dog_size = st.select_slider("Select your dog's size", options=size_list,value=size_list[1])

dog_weight = st.number_input("Enter your dog's current weight in kg", min_value=0.0, step=0.5, value=28.0)
# body_condition = st.select_slider("Enter your dogs BCS", options=[0,2,3,4,5,6,7,8,9], value=5)
# activity_level = st.selectbox("Select your dog's activity level", options=["Low", "Moderate", "High"], index=1)


if st.button("Calculate"):
    # ideal_weight = calculate_ideal_weight(weight, body_condition)
    calories = calculate_calories(dog_weight, dog_age, dog_size)
    
    # st.write(f"Your dogs ideal weight should be {ideal_weight}")
    st.write(f"Your dogs needs approximately {calories} calories per day.")

