import streamlit as st
import pickle

def main():
    label_encoder=pickle.load(open('/Users/harryphilip/PyCharmMiscProject/Project_File_one/label_encoders.sav','rb'))
    model=pickle.load(open('/Users/harryphilip/PyCharmMiscProject/Project_File_one/rf.sav','rb'))
    scaler=pickle.load(open('/Users/harryphilip/PyCharmMiscProject/Project_File_one/scaler.sav','rb'))
    st.title('Are You Okay?')
    gender=st.selectbox('Gender',options=['Male','Female'])
    age=st.text_input('Enter your Age ')
    academic_level=st.selectbox("Level of Education",options=['Bachelors', 'Masters', 'Doctorate', 'Class 12'])
    academic_pressure=st.selectbox('Academic Pressure ',options=[0,1,2,3,4,5])
    cgpa=st.text_input('Enter your CGPA (0-10)')
    study_satisfaction=st.selectbox('Study Satisfaction',options=[0,1,2,3,4,5])
    sleep_duration=st.selectbox('Sleep Duration',options=["'5-6 hours'", "'Less than 5 hours'", "'7-8 hours'",
       "'More than 8 hours'"])
    dietary_habit=st.selectbox('Dietary Habits',options=['Healthy', 'Moderate', 'Unhealthy'])
    thoughts=st.selectbox('Have you ever had suicidal thoughts ?',options=['No','Yes'])
    study=st.selectbox('Study Hours',options=[0,1,2,3,4,5,6,7,8,9,10,12])
    stress=st.selectbox('Financial Stress',options=['1.0','2.0','3.0','4.0','5.0'])
    history=st.selectbox('Family History of Mental Illness?',options=['No','Yes'])

    gender_new=label_encoder[0].transform([gender]).item()
    sleep_new=label_encoder[1].transform([sleep_duration]).item()
    diet_new=label_encoder[2].transform([dietary_habit]).item()
    thoughts_new=label_encoder[3].transform([thoughts]).item()
    stress_new=label_encoder[4].transform([stress]).item()
    history_new=label_encoder[5].transform([history]).item()
    academic_new=label_encoder[6].transform([academic_level]).item()

    features=[gender_new,age,academic_pressure,cgpa,study_satisfaction,sleep_new,diet_new,thoughts_new,study,stress_new,history_new,academic_new]

    pred=st.button('Predict')
    if pred:
        result = model.predict(scaler.transform([features]))
        if result==0:
            st.write(':green-background[NO,Based on what you have shared, you dont seem to be showing signs of depression.]')
        else:
            st.write(':red-background[YES,Based on your input, you may be experiencing depression. Please seek professional support.]')


main()
