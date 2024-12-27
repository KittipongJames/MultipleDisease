import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# ตั้งค่าสิ่งต่างๆบนหน้าเว็บ Parameter | page_title คือชื่อเว็บ layout='wide' รุปแบบของเว็บแบบกว้าง
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")  

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# ทำการใช้ pickle.load ที่ในโค้ดipynb เราแปลงให้มันเป็นในรูปแบบบิต)serializing แต่มาตอนนี้เราต้อง แปลงกลับมาเป็นโครงสร้างpython object(de-serializing) เก็บในตัวแปร diabetes_model 
diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/parkinsons_model.sav', 'rb'))

# สร้างตัวนำทาง Navigator โดยใช้คำสั่ง st.sidebar
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)


# เมื่อมีคนกดNavigator 'Heart Disease Prediction ซ้ายมือ
if selected == 'Heart Disease Prediction':

    # ใส่หัวข้อในหน้าที่กดเป็น Heart Disease Prediction using ML โดยเข้าถึง st(streamlit) ใช้คำสั่ง title
    st.title('Heart Disease Prediction using ML')

    # ทำการสร้างรูปแบบ layout แบบคอลัมน์3ช่องไว้โดยแบ่งช่องเท่าๆกัน อ่านต่อใน Onenote
    col1, col2, col3 = st.columns(3)
    
    # with col1: เป็นการเข้าถึง col1 
    with col1:
        # นำเข้า st(streamlit)จากโค้ดด้านบนที่วางรุปแบบคอลัมน์ไว้ 3ช่อง ใช้คำสั่ง text_input สร้างกล่องป้อนข้อมูลแล้วเก็บไว้ในตัวแปร age
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # สร้าง ค่าว่างไว้ เอาไว้ทำการเพิ่มข้อความทำนายค่าของโรคนั้นๆ ลงไป
    heart_diagnosis = ''

    # เมื่อ user กดปุุ่ม Heart Disease Test Result
    if st.button('Heart Disease Test Result'):

        # รับค่าในแต่ล่ะตัวแปร แต่ล่ะค่าที่นำเข้ามาเก็บสอดคล้องกับ ข้อมูลตัวอย่าง(features) ที่ใช้ในการทำนายโรค
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        #ทำการใช้ for loop สร้างตัวแปร x เป็นค่าเปล่าเข้าไปลูปในตัวแปร user_input อัพเดทเก็บในตัวแปร x ที่ละตัว แล้วแปลงจากข้อมูล string เป็น float โดยใช้ float(x) | ML ส่วนมากต้องการข้อมูลที่เป็นตัวเลข(numeric data) เช่น float integer
        # ที่ใช้ [] เพราะต้องทำหลายๆเงื่อนไข แปลงเป็น float + ใช้ for loop
        user_input = [float(x) for x in user_input]

        # นำเข้า model heart_disease.ipynb ที่ได้ฝึกฝนข้อมูลทดสอบและข้อมูลชุดเฉลย โดยฐานข้อมูลเหมือนกัน เป็นโมเดลที่มีประสิทธิภาพที่สุด เอามาทำการ predict ค่าในตัวแปร user_input ที่ userคนใหม่ๆป้อนเข้ามา
        # หลักการทำงาน ระบบจะนำค่าที่ user กรอกเข้ามา12ช่อง หรือ 12คอลัมน์เอาไปทดสอบกับโมเดลที่มีประสิทธิภาพที่สุด ว่าถ้าค่าที่user ใหม่ป้อนมาประมาณนี้จะตรงกับ ข้อมูลชุดเฉลยประมาณนี้นะ แล้วก็ output
        heart_prediction = heart_disease_model.predict([user_input])

        # เชคค่าที่ได้ผลฌแลยมาแล้วในตัวแปร heart_prediction ว่าถ้าเป็น1 ถือว่า เป็น 0 ถือว่าไม่เป็น
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    # โชว์ข้อความว่า เป็นโรคหรือไม่เป็น
    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
