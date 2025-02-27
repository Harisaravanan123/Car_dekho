import  pandas as pd
import pickle
import base64
import streamlit as st
import numpy as np
st.set_page_config(page_title="car dekho",page_icon=":car:",layout="centered")
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg("C:/Users/nambi/OneDrive/Pictures/png-transparent-sports-car-cartoon-running-car-compact-car-blue-car-accident.png")

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #9899AA;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color:brown;'>CarsDekho - Cars Price Prediction</h1>", unsafe_allow_html=True)

st.title("CAR DEKHO - USED CAR PRICE PREDICTION")

with open("le.pkl",'rb')as encoder:
    encode = pickle.load(encoder)
with open("rfr_b.pkl",'rb')as model_file:
    ml = pickle.load(model_file) 
data = pd.read_csv("preprocessed1.csv")    
df = pd.read_csv("E:\projects\car dekho\car_dekho1.csv")
def encoders(cols):
    original_cols = list(df[cols].unique())
    encoded_cols = list(data[cols].unique())
    cols_dic={}
    if len(original_cols) != len(encoded_cols):
        print("The unique values that present in the original columns are not equal to encoded columns")
    for original,encoded in zip(original_cols,encoded_cols):
        cols_dic[original]=encoded
    return cols_dic
fuel_type = encoders('fuel_type')   
body_type = encoders('body_type') 
transmission_type = encoders('transmission_type')
number_of_owners = encoders('number_of_owners')
manufacturer_company = encoders('manufacturer')
model = encoders('model')
model_year = encoders('model_year')
registration_year = encoders('registration_year')
insurance_validity =  encoders('insurance_validity')
seats = encoders('seats')
city = encoders('City')

st.sidebar.header("CAR FEATURES")
col1,col2 = st.columns(2)
with col1:
    
    Fueltype = st.sidebar.selectbox('fuel type',options=list(fuel_type.keys()))
    fueltype1 = fuel_type[Fueltype]
    Bodytype = st.sidebar.selectbox('body type',options=list(body_type.keys()))
    bodytype1 = body_type[Bodytype]
    kilometers_runned = st.sidebar.slider('kilometers runned',min_value=101,max_value=149973,step=100)
    
    Transmissiontype = st.sidebar.selectbox('transmission type',options=list(transmission_type.keys()))
    transmissiontype1 = transmission_type[Transmissiontype]
    No_owners = st.sidebar.selectbox('No.of.owners',options= list(number_of_owners.keys()))
    no_owners1 = number_of_owners[No_owners]
    Manufacturercompany = st.sidebar.selectbox('manufacturer company',options= list(manufacturer_company.keys()))
    manufacturercompany1 = manufacturer_company[Manufacturercompany]
    Model = st.sidebar.selectbox('model',options=list(model.keys()))
    model1 = model[Model]
    Model_year = st.sidebar.selectbox('model year',options= list(model_year.keys()))
    model_year1 = model_year[Model_year]
with col2:
    Registration_year = st.sidebar.selectbox('Registration year',options=list(registration_year.keys()))
    registration_year1 = registration_year[Registration_year]
    Insurancevalidity = st.sidebar.selectbox('insurance validity',options= list(insurance_validity.keys()))  
    insurancevalidity1 = insurance_validity[Insurancevalidity]
    Seats = st.sidebar.selectbox('seats',options=list(seats.keys()))
    seat1 = seats[Seats]
    Engine_displacement = st.sidebar.slider('engine displacement',min_value=745.5,max_value=1949.5,step=10.5)
    
    mileage = st.sidebar.slider('mileage',min_value=10.00,max_value=29.00,step=1.5)
    max_power = st.sidebar.slider('max power(bhp)',min_value=34,max_value=178,step=4)
    City = st.sidebar.selectbox('City',options= list(city.keys()))
    city1 = city[City]
numerical_value=[[fueltype1,bodytype1,kilometers_runned,transmissiontype1,no_owners1,manufacturercompany1,model1,
                  model_year1,registration_year1,insurancevalidity1,seat1,Engine_displacement,mileage,max_power,city1]] 
button = st.button("PREDICT PRICE") 
if button:
    price = ml.predict(np.array(numerical_value))[0]
    price_r = round(price,2)
    
    st.markdown(f'<h2 style="text-align: center;color:brown;">Predicted Car Price : ₹ {price_r} </h2>', unsafe_allow_html=True)





