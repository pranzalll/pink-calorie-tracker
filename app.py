import streamlit as st
import pandas as pd
import os

# Page settings
st.set_page_config(
    page_title="Nutrition Tracker",
    page_icon="꧁🪷🌷🌸🌺🦩꧂",
    layout="centered"
)

# Custom pink styling
st.markdown("""
    <style>
    .stApp {
        background-color: #ffd6e7;
    }

    h1 {
        color: #ff1493;
        text-align: center;
    }

    .stButton>button {
        background-color: #ff69b4;
        color: blue;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
    }

    .stButton>button:hover {
        background-color: #ff1493;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("꧁🪷🌷🌸🌺🦩꧂ Nutrition Tracker")

# User input
food = st.text_input("Food Name")
calories = st.number_input("Calories", min_value=0)

# Add food button
if st.button("Add Food 🪷"):

    new_food = pd.DataFrame({
        "Food": [food],
        "Calories": [calories]
    })

    if os.path.exists("foods.csv"):
        old_data = pd.read_csv("foods.csv")
        updated_data = pd.concat([old_data, new_food], ignore_index=True)
    else:
        updated_data = new_food

    updated_data.to_csv("foods.csv", index=False)

    st.success("Food Added!")

# Display saved foods
if os.path.exists("foods.csv"):

    data = pd.read_csv("foods.csv")

    st.subheader("Today's Foods 🍽️")
    st.dataframe(data)

    total = data["Calories"].sum()

    st.subheader(f"✨ Total Calories: {total}")