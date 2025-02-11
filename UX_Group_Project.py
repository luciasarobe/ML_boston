import streamlit as st
import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression

col1, col2 = st.columns(2)

with col1:
        st.write("")
        st.write("")
        st.title("Welcome to Boston!")
with col2:
        st.image("Boston-white.webp",width=210)



st.header("The Mayor's Office of Housing is here to help you on your journey to find your home 	:house_buildings:")
st.write("**House Price Predictor: How does it work?**")

st.write("We know finding a house at the right price in a new city can be overwhelming, therefore we have created this page for you to input your criterias and we will provide you with an price estimate.")
st.write("If you would like to receive additional tips & tricks on how to find your dream home, we can send you a brochure directly to your inbox.")

with st.container():
	name=st.text_input("Enter your e-mail here:")
	submit_button=st.button("Submit your info")
	if submit_button:
                if name:
                        st.toast("The brochure has been sent to your inbox :incoming_envelope:")
                else:
                        st.warning("Please enter an email before submitting.")


st.write("If you need further assistance, please do not hesitate to reach out to us via support@bostonhousing.com")

st.write("---")

# Input criteria
st.subheader("Criteria")


def user_input():
        #Number of rooms (RM)
        rooms = st.slider("**Number of rooms:**",min_value=1, max_value=20, value=1)
        st.write(f"You selected {rooms} number of rooms")
        st.write("---")
        #Per capita Crime rate (CRIM)
        crime_rate = st.slider("**Crime rate per capita:**",min_value=0.00, max_value=90.00, value=0.01)
        st.write(f"Useful to know: The average crime rate in the whole Boston area is 3.61")
        st.write("---")
        #we could add IF statement a la "you chose XY, which is above the average..

        #Pollution (NOX)
        pollution = st.slider("**Pollution in area**",min_value=0.00, max_value=1.00, value=0.01)
        st.write(f"Useful to know: The average pollution in the whole Boston area is 0.55")
        st.write("---")

        #Percentage of lower status of population (LSTAT)
        lstat = st.slider("**Percentage of lower status of population (%)**",min_value=1.00, max_value=40.00, value=0.01)
        st.write(f"Useful to know: The average percentage of lower status of population is 12.65%")
        st.write("---")

        #Tax rate (TAX)
        tax_rate = st.slider("**Tax rate**",min_value=187.00, max_value=711.00, value=0.01)
        st.write("---")

        #Proportion of industrial business in area (INDUS)
        indus = st.slider("**Proportion of industrial business in area (%)**",min_value=1.00, max_value=40.00, value=0.01)
        st.write(f"Useful to know: The average percentage of industrial businesses in the area is 11.14%")
        st.write("---")


        #Pupil-teacher ratio (PTRATIO)
        ratio = st.slider("**Pupil-teacher ratio**",min_value=12, max_value=22, value=1)
        st.write(f"The boston average ratio is 18.45, meaning 1 teacher for every 18.45 pupils. You selected a ratio of {ratio}")
        st.write("---")

        #Residential Zone (ZN)
        zn = st.slider("**Percentage of residential zones in your desired area**",min_value=0, max_value=100, value=1)
        st.write(f"The higher the percentage is the lower is the house density and the more space you may expect in that area. You selected a percentage of {ratio}")
        st.write("---")

        #Near River (CHAS)
        near_river = st.selectbox('**Do you wish your house to be closes to the Charles River?**',('Yes','No'))
        st.write('Your selection is:', near_river)
        st.write("---")
        
        #OlderHomes (AGE)
        oldhomes = st.slider("**Percentage of older homes in your desired area**",min_value=0, max_value=100, value=1)
        st.write(f"Old houses are houses built before 1940. You selected a ratio of {ratio}")
        st.write("---")

        #Distance to Employment Centers (DIS)
        importance = st.slider("**How important is it to you that employment centers are close?**",min_value=0, max_value=10, value=0, step=1)
        min_dis = 1   # Closest to employment centers
        max_dis = 13  # Farthest from employment centers
        mapped_dis = np.interp(importance, [0, 10], [max_dis, min_dis])
        st.write(f"Higher importance means closer proximity to employment centers. Lower importance means houses can be further away. You selected an importance level of {importance}")
        st.write("---")
            
        #BlackPopIndex (B)
        importance_B = st.slider("**How important is it for you to live in an area with mixed ethnicity?**", 
                         min_value=0, max_value=10, value=0, step=1)
        min_B = 0   # Least diverse (low `B` value)
        max_B = 400  # Most diverse (highest observed `B` value in dataset)
        mapped_B = np.interp(importance_B, [0, 10], [min_B, max_B])
        st.write(f"Higher importance means choosing an area with a more diverse population. Lower importance means living in a less diverse area. You selected an importance level of {importance_B}")
        st.write("---")

        #HighwayAccess (RAD)
        

        data = {"rooms": rooms,
                "crime_rate": crime_rate,
                "pollution": pollution,
                "lstat": lstat,
                "tax_rate": tax_rate,
                "indus": indus,
                "pupil_teacher_ratio": ratio,
                "Residential zone": zn,
                "River Proximity": near_river,
                "Older Homes": oldhomes,
                "Distance to Employment Centers": importance,
                "Mixed ethnicity areas":importance_B}
        features = pd.DataFrame(data, index=[0])
        return features
                
df = user_input()              

#Summary of input parameters

st.subheader("Your criteria for your dream home")
st.write(df)
st.write("---")
#Regression Model


#Prediction

st.subheader("Prediction of your house price")

st.write("---")





