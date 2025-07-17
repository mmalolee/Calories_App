import streamlit as st
import numpy as np
import joblib
from pathlib import Path

# Paths to models
MALES_PATH = Path('models/lm_males.pkl')
FEMALES_PATH = Path('models/lm_females.pkl')

# Constants
MIN_BODY_TEMP = 36.6
MIN_HEART_RATE = 60
MIN_DURATION = 1

# Handling an exception when an invalid file path is provided
try:
    males = joblib.load(MALES_PATH)
    females = joblib.load(FEMALES_PATH)
except FileNotFoundError: 
    st.error('Error while loading file')
    st.stop()


st.title('Calorie Burn Approximator:running:')
st.header('Provide the required parameters')

# Memory of calories burned
if "total_males" not in st.session_state:
     st.session_state["total_males"] = 0
     
if "total_females" not in st.session_state:
     st.session_state["total_females"] = 0

#
## MAIN
#

c0, c1 = st.columns(2, border=True)

# Gender selection
with c0:
    gender = st.selectbox('Gender:', ['Female', 'Male'])

# Entering the running time
with c1:
    if gender == 'Female':
        duration = st.number_input(
            'Estimated running time',
            help='Estimated running time in minutes',
            step=1,
            min_value=MIN_DURATION)
    else:
        duration = st.number_input(
            'Estimated running time',
            help='Estimated running time in minutes',
            step=1,
            min_value=MIN_DURATION)

c0, c1 = st.columns(2, border=True)

# Entering your predicted heart rate
with c0:
    if gender == 'Female':
            heart_rate = st.number_input(
            'Estimated heart rate',
            help='Estimated number of beats per minute while running',
            step=1,
            min_value=MIN_HEART_RATE)
    else:
        heart_rate = st.number_input(
            'Estimated heart rate',
            help='Estimated number of beats per minute while running',
            step=1,
            min_value=MIN_HEART_RATE)

# Entering your predicted body temperature        
with c1:
    if gender == 'Female':
            body_temp = st.number_input(
            'Estimated body temperature',
            min_value=MIN_BODY_TEMP,
            format='%.1f',
            step=0.1,
            help='Estimated body temperature while running')
    else:
        body_temp = st.number_input(
            'Estimated body temperature',
            min_value=MIN_BODY_TEMP,
            format='%.1f',
            step=0.1,
            help='Estimated body temperature while running')

# Writing data to a numpy array
input_data = np.array([duration, heart_rate, body_temp]).reshape(1, 3)

# Predicting values
if st.button('Estimate burned calories', use_container_width=True):
    if gender == 'Female':
        calories = females.predict(input_data)
        st.header(f'Current session: {int(calories)} burned calories :fire:')
        st.session_state['total_females'] += calories
        st.header(f'Estimated total calories burned: {int(st.session_state["total_females"])} :fire:')
    else:
        calories = males.predict(input_data)
        st.header(f'Current session: {int(calories)} burned calories :fire:')
        st.session_state['total_males'] += calories
        st.header(f'Estimated total burned calories: {int(st.session_state["total_males"])} :fire:')
