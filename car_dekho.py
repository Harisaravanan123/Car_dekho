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

with open("encoders_file.pkl",'rb')as encoder_file:
    encode = pickle.load(encoder_file)
with open("rfr_b.pkl",'rb')as model_file:
    ml = pickle.load(model_file) 
data = pd.read_csv("preprocessed_data.csv")    
df = pd.read_csv("E:\projects\car dekho\car_dekho.csv")
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
manufacturer_company = encoders('manufacturer')
model = encoders('model')
insurance_validity =  encoders('insurance_validity')
city = encoders('City')
st.sidebar.header("CAR FEATURES")
col1,col2 = st.columns(2)
with col1:
    City = st.sidebar.selectbox('City',options= list(city.keys()))
    city1 = city[City]
    fueltype = st.sidebar.selectbox('fuel type',options=list(fuel_type.keys()))
    fueltype1 = fuel_type[fueltype]
    bodytype = st.sidebar.selectbox('body type',options=list(body_type.keys()))
    bodytype1 = body_type[bodytype]
    transmissiontype = st.sidebar.selectbox('transmission type',options=list(transmission_type.keys()))
    transmissiontype1 = transmission_type[transmissiontype]
    manufacturercompany = st.sidebar.selectbox('manufacturer company',options= list(manufacturer_company.keys()))
    manufacturercompany1 = manufacturer_company[manufacturercompany]
    engine_displacement = st.sidebar.slider('engine displacement',min_value=72,max_value=4806,step=72)
    engine_displacement1 = round(np.cbrt(engine_displacement),2)
    model_year = st.sidebar.selectbox('model year',options=[2015, 2018, 2014, 2020, 2017, 2021, 2019, 2022, 2016, 2011, 2013,
       2010, 2006, 2012, 2008, 2009, 2023, 2005, 2007, 2004, 2003, 2002])
with col2:
    insurancevalidity = st.sidebar.selectbox('insurance validity',options= list(insurance_validity.keys()))  
    insurancevalidity1 = insurance_validity[insurancevalidity]
    mod = st.sidebar.selectbox('model',options=list(model.keys()))
    model1 = model[mod]
    kiloometers_runned = st.sidebar.slider('kilometers runned',min_value=0,max_value=5500000,step=10)
    kiloometers_runned1 =round(np.cbrt(kiloometers_runned),2)
    seats = st.sidebar.selectbox('seats',options=[5,7,4,6,8,10,9,2])
    max_power = st.sidebar.slider('max power(bhp)',min_value=34,max_value=510,step=34)
    max_power1 = round(np.cbrt(max_power),2)
    mileage = st.sidebar.slider('mileage',min_value=7,max_value=140,step=7)
    mileage1 = round(np.cbrt(mileage),2)
    registration_year = st.sidebar.selectbox('Registration year',options=[2015, 2018, 2014, 2020, 2017, 2021, 2019, 2022, 2016, 2011, 2013,
       2010, 2006, 2012, 2008, 2009, 2023, 2005, 2007, 2004, 2003, 2002])
    No_owners = st.sidebar.selectbox('No.of.owners',options=[1,2,3,4,5])
numerical_value=[[city1,fueltype1,bodytype1,transmissiontype1,manufacturercompany1,engine_displacement1,model_year,
                  insurancevalidity1,model1,kiloometers_runned1,seats,max_power1,mileage1,registration_year,No_owners]] 
button = st.button("PREDICT PRICE") 
if button:
    price = ml.predict(np.array(numerical_value))[0] 
    price_r = round(price,2)
    
    st.markdown(f'<h2 style="text-align: center;color:brown;">Predicted Car Price : ₹ {price_r} </h2>', unsafe_allow_html=True)





