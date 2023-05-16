import streamlit as st

def calculate_ideal_weight(weight, body_condition):
    if body_condition < 5:
        if body_condition == 1:
            ideal_weight = weight * 2
        elif body_condition == 2:
            ideal_weight = weight * 1.8
        elif body_condition == 3:
            ideal_weight = weight * 1.5                  
        elif body_condition == 4:
            ideal_weight = weight * 1.2
    elif body_condition > 5:
        if body_condition == 6:
            ideal_weight = weight * 0.95
        if body_condition == 7:
            ideal_weight = weight * 0.9            
        if body_condition == 8:    
            ideal_weight = weight * 0.8
        if body_condition == 9:    
            ideal_weight = weight * 0.75
    else: 
        ideal_weight = weight
    return round(ideal_weight,2)            
            
def calculate_calories(weight, activity_level, body_condition, dog_size):
    rer = calculate_rer(weight,dog_size)
    if activity_level == "Low":
        calories = rer
    elif activity_level == "Moderate":
        calories = rer * 1.6
    else:  # High activity level
        calories = rer * 1.8
    return round(calories, 2)

def calculate_rer(weight,dog_size):
    if dog_size == "Medium":
        return round((30 * weight + 70), 2)
    else:
        return round((70 * (weight**(3/4))),2)
        

st.title("Dog Food Calorie Calculator")

st.write("This application calculates the daily calorie needs for your dog based on their weight and activity level.")

weight = st.number_input("Enter your dog's weight in kg", min_value=0.0, step=0.1)
body_condition = st.number_input("Enter your dogs BCS", min_value=1, max_value=9, step=1)
activity_level = st.selectbox("Select your dog's activity level", options=["Low", "Moderate", "High"])
dog_size = st.selectbox("Select your dogs size", options=["Small", "Medium", "Large"])


if st.button("Calculate"):
    ideal_weight = calculate_ideal_weight(weight, body_condition)
    calories = calculate_calories(ideal_weight, activity_level, body_condition, dog_size)
    
    st.write(f"Your dogs ideal weight should be {ideal_weight}")
    st.write(f"Your dogs needs approximately {calories} calories per day.")

