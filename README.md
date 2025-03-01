CAR DEKHO - USED CAR PRICE PREDICTIONS:

The main objective of the project is to create a machine learning model, which is used to predict the prices of the used car based on the features selected by the user.

TOOLS:

* python
* pandas,numpy
* seaborn
* matplotlib
* Scikit-learn: 1.Random Forest Regressor 2.linear Regression 3.Gradient Boosting Regression 4.Decision Tree Regression 5.RandomizedSearchCV
* Streamlit

  
DATA PREPROCESSING: 
* The data are in JSON format , first I structured the data into tabular schema.
* I remove the null values that present in the Dataframe and also changed the datatypes to their respective datatypes.
* Then by using regular expression , I removed all the symbols and commas. I also did the conversion of bhp to numerical value in the max power(bhp) column. By which we can
 able to use the numerical value in the model training.
* I did label encoding  for the categorical columns in the dataframe.
* I Used the IQR(Inter Quartile Range) method to remove the outliers that present in the data

EXPLORATORY DATA ANALYSIS:


![Image](https://github.com/user-attachments/assets/cac5c1d8-4295-4cfd-b145-a04c70e44b6f)
* This image shows the outlying data that present in the numerical columns.


![Image](https://github.com/user-attachments/assets/c9d59ec5-4820-4572-b9c3-6189b783ff90)
* This image shows the dataset after applying IQR(INTER QUARTILE RANGE) method to remove the outliers.

![Image](https://github.com/user-attachments/assets/10c468a6-460f-4b44-b5ad-3b17d70782ee)
* The CNG fuel type cars have a very good mileage between  26-33(kmpl).
* The LPG fuel type cars have a very bad mileage between  16 -19(kmpl).

![Image](https://github.com/user-attachments/assets/48c8545d-fcbe-4b99-b89d-556aeaef2a7a)
* Most of the cars that present in the dataset are maruthi  and most of their cars are in the body type of hatchbacks.
* The least number of cars manufactured by mercedez-benz and most of their cars are in the bodytype of sedan.

MACHINE LEARNING:

* I did four machine learning algorithms( Linear regression, Decision Tree Regressor, Random Forest Regression, Gradient Boosting Regressor).
* I did hyper parameter tuning by using Randomized search CV method for Random Forest Regressor and get the best R2 SCORE OF 0.92.
* I also measure the error metrics of the models with mean absolute error, mean squared error , Root mean squared error.

![Image](https://github.com/user-attachments/assets/5162441c-625e-4337-ad5b-2f6a4e82b43f)

STREAMLIT:
* In the streamlit , based on the features given by the Users , the model will predict the price of the car.

CONCLUSION:
* We build a web browser from the machine learning model. The  customer will select  the features  based on their needs and budget. The model predicts the price of the used car based on the input given by the customers . It is very useful for the customer to select the features of the cars that they want and under their budget also. It is very helpful for the sales team in the car Dekho to sell their cars very  quickly and they also achieve their sales target.


  










