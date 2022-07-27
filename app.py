import streamlit as st
import pandas as pd
import pickle
import numpy as np
import base64
import streamlit as st
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp
     {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('ven.png')


pickle_in = open('model_pickel.pkl' , 'rb')

regressor = pickle.load(pickle_in)



def predict_pressure(breadth_id,C,R,time_step,u_in,u_out):
    x = np.zeros(243)
    x[0] = breadth_id
    x[1] = C
    x[2] = R
    x[3] = time_step
    x[4] = u_in
    x[5] = u_out
    return np.round(regressor.predict([x])[0],6)
def main():
    home = pd.read_csv("test.csv")
    st.title("Ventilator Pressure Prediction")
    #html_temp = """
    #<h2 style = "color:black;text-align:left:"> Pressure Prediction ML APP </h2>
    #"""
    #st.markdown(html_temp,unsafe_allow_html= True)
    html_temp = """
    <h2 style = "color:black;text-align:left:"> Please Enter the required details </h2>
    """
    #st.subheader("Please Enter the required details")
    breadth_id = st.markdown("""### breadth_id""", True)
    breadth_id = st.text_input(" ","")
    C = st.markdown("""### C""" , True)
    C = st.selectbox(" " , [" " , "10" , "20" , "50"])
    R = st.markdown("""### R""", True)
    R = st.selectbox(" ", [" " , 5 , 20 , 50])
    time_step = st.markdown("""### time_step""", True)
    time_step = st.text_input("Enter value between 0 to 3 :" , "")
    u_in = st.markdown("""### u_in""", True)
    u_in = st.text_input("" , " ")
    u_out = st.markdown("""### u_out""", True)    
    u_out = st.selectbox(" ", [" " , 0 , 1])
    
    result = ""
    if st.button("Predicted Pressure"):
        result = predict_pressure(breadth_id,C,R,time_step,u_in,u_out)
    st.success("The Pressure is {}\-".format(result))


if __name__ == "__main__":
    main()


