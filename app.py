import streamlit as st
from PIL import Image
import pickle

def main():
    st.title("Lung Cancer Prediction System")
    img=Image.open('lung.jpg')
    st.image(img,width=800)

    age=st.number_input("Age", min_value=1, max_value=120, step=1)

    smoke=st.number_input("Smokes", min_value=1, max_value=120, step=1)
    areaQ=st.number_input("Area Quality", min_value=1, max_value=120, step=1)
    alcohol=st.number_input("Alcohol", min_value=1, max_value=120, step=1)
    st.markdown("""
    <style>
    div.stButton > button {
        width: 250px;
        height: 50px;
        font-size: 20px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    pred=st.button("Predict")

    features=[age,smoke,areaQ,alcohol]

    model=pickle.load(open('knn_model.sav','rb'))
    scaler=pickle.load(open('std_scaler.sav','rb'))

    if pred:
        result=model.predict(scaler.transform([features]))
        st.info(
        "⚠️ This application is for study purposes only. "
        "Predictions may not be accurate and should not be used for medical diagnosis."
        )
        st.subheader("Prediction")
        if result[0]==0:
            st.write("✅ No significant lung cancer risk indicated by the model.")
        else:
            st.write("⚠️ The prediction indicates a potential risk of lung cancer.")

main()