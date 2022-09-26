import streamlit as st
import pandas as pd
import pickle
from PIL import Image
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
def main():
    #hiding navbar
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    
    with st.sidebar:
        
        selected = option_menu("MAIN MENU", ["HOME","PROJECT","CONTACT"],icons=["house","code-slash","envelope"],menu_icon="cast", default_index=0)
    if selected=="HOME":
        st.title ("Health Insurance Cost Predictor")
        
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
        lottie_url= "https://assets3.lottiefiles.com/packages/lf20_ginda0jy.json"
        lottie_anime = load_lottieurl(lottie_url)
        st_lottie(lottie_anime, key="animation")
        st.markdown("Health Insurance is a type of insurance that covers medical expenses. A person who has taken a health insurance policy gets health insurance cover by paying a particular premium amount.")
    if selected=="PROJECT":
        #title of page
        st.title ("Health Insurance Cost Predictor")
        #image 
        imag = Image.open('health.jpeg')
        st.image(imag, width=None)

        st.set_option('deprecation.showfileUploaderEncoding', False)
        model =pickle.load(open('insurance.pkl', 'rb'))

        #independent variables input
        age=st.slider("Input age",0,100)
        s = st.selectbox(" Input your Gender", ['male','female'])
        if s=="male":
            sex=0
        elif s=="female":
            sex=1
        bmi=st.number_input("Input your BMI", 0.0, 70.0, 0.0, 0.01)
        children=st.selectbox(" How many Children ",[0,1,2,3,4,5,6,7,8,9,10])
        smoker =st.slider(" Are you a smoker 0 for no and 1 for yes ", 0, 1)
        reg=st.selectbox("Select region",['southeast','southwest','northeast','northwest'])
        if reg=="southeast":
            region=0
        elif reg =="southwest":
            region=1
        elif reg=="northeast":
            region=2
        elif reg =="northwest":
            region=3
        #onclick of button
        if st.button('Predict'):
            data = {'age': [age], 'sex': [sex], 'bmi': [bmi], 'children': [children], 'smoker': [smoker], 'region': [region]}
            cust_df = pd.DataFrame(data)
            cost_pred = model.predict(cust_df)
            st.header("Insurance cost will be Rs." + str(cost_pred[0]))
    if selected=="CONTACT":
        st.header("Get In Touch")
        st.subheader("Name : Shreyas")
        st.subheader("Check out my [Portfolio](https://shreyas-achar.github.io/)")
        col1, col2 = st.columns(2)

        with col1:
            contact_form = """
            <form action="https://formsubmit.co/shreyasachar7@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here"></textarea>
            <button type="submit">Send</button>
            </form>
            """

            st.markdown(contact_form, unsafe_allow_html=True)
            def local_css(file_name):
                with open(file_name) as f:
                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


            local_css("style/style.css")
#file runs as a script but not when imported
if __name__ == '__main__':
    main()
