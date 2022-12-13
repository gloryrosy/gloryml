
import pickle
import streamlit as st


cal_model = pickle.load(open('C:/Users/GLORYROSY/Desktop/caloriesweb/trained_model.sav', 'rb'))
   
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age ')
        
    with col2:
        Height = st.text_input('Height')
    
    with col3:
        Weight = st.text_input('Weight')
    
    with col1:
        Duration = st.text_input('Exercise Duration')
    
    with col2:
        Heart_Rate = st.text_input('Heart Rate')
    
    with col3:
        Body_Temp = st.text_input('Body Temparature')
    
   
    
    # code for Prediction
    
    # creating a button for Prediction
    
    if st.button('Predict Calories'):
        cal_prediction = cal_model.predict([[Age, Height, Weight, Duration, Heart_Rate, Body_Temp]])
        st.success('The Calories Burnt is',cal_prediction[0])
        
    




