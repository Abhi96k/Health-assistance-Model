import streamlit as st
import os
import pickle


st.set_page_config(
    page_title="Health Assistant",
    layout="wide",
    page_icon="🧑‍⚕️"
)


custom_css = """
<style>
   
.sidebar .sidebar-content {
    background-image: linear-gradient(#f5f5f5, #f5f5f5);
    color: black;
}
.subheader {  
    font-size: 20px;
    font-weight: bold;
    color: red;
    background-color: #f5f5f5;
    padding: 10px;
    margin-top: 10px;
    margin-bottom: 10px;
    border-radius: 10px;
}

</style>
"""     


st.markdown(custom_css, unsafe_allow_html=True)


st.title("Health Assistant")


working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(os.path.join(working_dir, 'diabetes_model.sav'), 'rb'))

heart_disease_model = pickle.load(open(os.path.join(working_dir, 'heart_disease_model.sav'), 'rb'))

parkinsons_model = pickle.load(open(os.path.join(working_dir, 'parkinsons_model.sav'), 'rb'))

liver_disease_model = pickle.load(open(os.path.join(working_dir, 'liver-disease.sav'), 'rb'))

asthma_disease_model = pickle.load(open(os.path.join(working_dir, 'asthma_disease.sav'), 'rb'))



def main():

    menu = ["Home", "Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction", "Liver Disease Prediction", "Asthma Disease Prediction"]
    selected = st.sidebar.selectbox("Menu", menu)

    if selected == "Home":
        st.subheader("Home")


        

        
        


    elif selected == "Diabetes Prediction":
        st.subheader("Diabetes Prediction")
        predict_diabetes(diabetes_model)

    elif selected == "Heart Disease Prediction":
        st.subheader("Heart Disease Prediction")
        predict_heart_disease(heart_disease_model)

    elif selected == "Parkinson's Prediction":
        st.subheader("Parkinson's Prediction")
        predict_parkinsons(parkinsons_model)

    elif selected == "Liver Disease Prediction":
        st.subheader("Liver Disease Prediction")
        predict_liver_disease(liver_disease_model)


    elif selected == "Asthma Disease Prediction":
        st.subheader("Asthma Disease Prediction")
        predict_asthma_disease(asthma_disease_model)        


def predict_diabetes(model):
    
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


    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

def predict_heart_disease(model):
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.selectbox('Sex', ['Male', 'Female'])

    with col3:
        cp = st.selectbox('Chest Pain Types', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['True', 'False'])

    with col1:
        restecg = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST-T wave abnormality', 'Probable or definite left ventricular hypertrophy'])

    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')

    with col3:
        exang = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.selectbox('Slope of the peak exercise ST segment', ['Upsloping', 'Flat', 'Downsloping'])

    with col3:
        ca = st.selectbox('Number of Major Vessels Colored by Flourosopy', ['0', '1', '2', '3'])

    with col1:
        thal = st.selectbox('Thal', ['Normal', 'Fixed Defect', 'Reversable Defect'])

  
    heart_diagnosis = ''

   
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        

        user_input = [float(x) if x.replace('.', '', 1).isdigit() else 0 for x in user_input]

        heart_prediction = model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

def predict_parkinsons(model):

    col1, col2, col3 = st.columns(3)

    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        MDVP_Fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        MDVP_Flo = st.text_input('MDVP:Flo(Hz)')

    with col1:
        MDVP_Jitter_Per = st.text_input('MDVP:Jitter(%)')

    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP')

    with col1:
        MDVP_PPQ = st.text_input('MDVP:PPQ')

    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP')

    with col3:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')

    with col1:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')

    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')

    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ')

    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA')

    with col3:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col1:
        spread1 = st.text_input('spread1')

    with col2:
        spread2 = st.text_input('spread2')

    with col3:
        D2 = st.text_input('D2')

    with col1:
        PPE = st.text_input('PPE')

  
    parkinsons_diagnosis = ''

  
    if st.button("Parkinson's Test Result"):
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter_Per, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP,
                      MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE,
                      DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's Disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's Disease"
  

    st.success(parkinsons_diagnosis)


    
def predict_liver_disease(model):
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            Age = st.text_input('Age')
    
        with col2:
            Gender = st.text_input('gender')

        with col3:
            Total_Bilirubin = st.text_input('Total Bilirubin')

        
               


        with col1:
            Direct_Bilirubin = st.text_input('Direct Bilirubin')

        with col2:
            Alkaline_Phosphotase = st.text_input('Alkaline Phosphotase')

        with col3:
            Alamine_Aminotransferase = st.text_input('Alamine Aminotransferase')


        with col1:
            Aspartate_Aminotransferase = st.text_input('Aspartate Aminotransferase')

        with col2:
            Total_Protiens = st.text_input('Total Protiens')

        with col3:
            Albumin = st.text_input('Albumin')


        with col1:
            Albumin_and_Globulin_Ratio = st.text_input('Albumin and Globulin Ratio')  

        with col2:
            Dataset = st.text_input('Target')

        

        liver_diagnosis = ''

        if st.button('Liver Disease Test Result'):


            user_input = [Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]

            user_input = [float(x) for x in user_input]

            liver_prediction = model.predict([user_input])

            if liver_prediction[0] == 1:
                liver_diagnosis = 'The person is having liver disease'
            else:
                liver_diagnosis = 'The person does not have any liver disease'

        st.success(liver_diagnosis)

def predict_asthma_disease(model):
        
            col1, col2, col3 = st.columns(3)
        
            with col1:
                Tiredness = st.text_input('Tiredness')
        
            with col2:
                Dry_Cough = st.text_input('Dry-Cough')

            with col3:
                Sour_throat = st.text_input('Sour-throat') 


            with col1:
                None_Sympton = st.text_input('None_Sympton')

            with col2:
                Pains = st.text_input('Pains')

            with col3:
                Nasal_Congestion = st.text_input('Nasal-Congestion')


            with col1:
                Runny_Nose = st.text_input('Runny-Nose')

            with col2:
                None_Experiencing = st.text_input('None-Experiencing')

            with col3:
                Age_0_9 = st.text_input('Age_0-9')


            with col1:
                Age_10_19 = st.text_input('Age_10-19')

            with col2:
                Age_20_24 = st.text_input('Age_20-24')

            with col3:
                Age_25_59 = st.text_input('Age_25-59')


            with col1:
                Age_60 = st.text_input('Age_60')

            with col2:
                Gender_Female= st.text_input('Gender_Female')

            with col3:
                Gender_Male= st.text_input('Gender_Male')


            with col1:
                Severity_Mild= st.text_input('Severity_Mild')

            with col2:
                Severity_Moderate= st.text_input('Severity_Moderate')

            

            asthma_diagnosis = ''

            if st.button('Asthma Disease Test Result'):
                user_input = [Tiredness,Dry_Cough,Sour_throat,None_Sympton,Pains,Nasal_Congestion,Runny_Nose,None_Experiencing,Age_0_9,Age_10_19,Age_20_24,Age_25_59,Age_60,
                              Gender_Female,Gender_Male,Severity_Mild,Severity_Moderate]
                
                user_input = [float(x) for x in user_input]

                asthma_prediction = model.predict([user_input])

                if asthma_prediction[0] == 1:
                    asthma_diagnosis = 'The person is having asthma disease'
                else:
                    asthma_diagnosis = 'The person does not have any asthma disease'

            st.success(asthma_diagnosis)


    
                                                      


if __name__ == "__main__":
  main()
