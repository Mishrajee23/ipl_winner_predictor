import streamlit as st
import pickle
import pandas as pd
from playsound import playsound
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('IMZ.JPG')  



runs_left=0
balls_left=0
crr=0
rrr=0


teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Bengaluru', 'Indore', 'Dubai', 'Sharjah']

pipe = pickle.load(open('pipe.pkl','rb')) 

st.title("----------:red[IPL Winner Predictor]---------")
#st.title("This text  :red[colored red], and this is **:blue[colored]** and bold.")
st.header(" :blue[BY: Vikash Kumar Mishra]")


col1,col2=st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting teams',sorted(teams))

with col2:
    bowling_team = st.selectbox('Select the bowling teams',sorted(teams))    

selected_city =  st.selectbox('Select host city',sorted(cities))  
target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')

with col4:
    overs = st.number_input('overs completed')

with col5:
    wickets = st.number_input('Wickets')

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left
    st.balloons()
    playsound('F:/machine learning/ipl winning predictor/ayogi-309.mp3')
    
    

input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],
'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target], 
'crr':[crr],'rrr':[rrr]})

st.table(input_df)
result = pipe.predict_proba(input_df)
#st.text(result)
loss = result[0][0]
win = result[0][1]
st.subheader(":red[The winning probability of  ]  "+batting_team + "- " + str(round(win*100)) + "%")
st.subheader(":red[The winning probability of  ]  "+ bowling_team + "- " + str(round(loss*100)) + "%")

#playsound('F:/machine learning/ipl winning predictor/ayogi-309.mp3')
  