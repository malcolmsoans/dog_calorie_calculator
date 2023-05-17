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
    # st.caption(f"Your dogs RER(Resting Energy Requirement) is :red[{dog_rer}] calories per day.")
    return round(dog_rer * calc_dict[dog_age], 2)
     
st.title("Calculate calories for your :dog:")
st.caption("This application provides an estimated calculation of the daily caloric needs for your dog based on their age/condition, size and weight.")
st.caption(":red[Please Note: This estimate does not replace professional health advice of a veterinarian.]")

dog_age = st.selectbox("Select your dog's age/condition", options=age_list,index=2)
# st.markdown("""<a href="https://d2zp5xs5cp8zlg.cloudfront.net/image-35319-800.jpg"> Determine if your dog is obese.</a>""")
# st.write("Determine your dogs condition :link[https://d2zp5xs5cp8zlg.cloudfront.net/image-35319-800.jpg]")

dog_size = st.select_slider("Select your dog's size", options=size_list,value=size_list[1])

dog_weight = st.number_input("Enter your dog's current weight in kg", min_value=0.0, step=0.5, value=28.0)

if st.button("Calculate"):
    calories = calculate_calories(dog_weight, dog_age, dog_size)
    if dog_age == age_list[0] or dog_age == age_list[1]:
        st.write(f"Your dogs GER(Growth Energy Requirements) is :red[{calories}] calories per day.")
    else:
        st.write(f"Your dogs DER(Daily Energy Requirements) is :red[{calories}] calories per day.")    
