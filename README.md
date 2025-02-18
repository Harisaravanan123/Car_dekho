CAR DEKHO - USED CAR PRICE PREDICTIONS:

The main objective of the project is to create a machine learning model, which is used to predict the prices of the used car based on the features selected by the user.

TOOLS:

* python
* pandas,numpy
* seaborn
* matplotlib
* Scikit-learn: 1.Random Forest Regressor 2.linear Regression 3.Gradient Boosting Regression 4.Decision Tree Regression 5.RandomizedSearchCV
* Streamlit
DATA PREPROCESSING
* The data are in JSON format , first I structured the data into tabular schema.
* I remove the null values that present in the Dataframe and also changed the datatypes to their respective datatypes.
* Then by using regular expression , I removed all the symbols and commas. I also did the conversion of bhp to numerical value in the max power(bhp) column. By which we can
 able to use the numerical value in the model training.
* I did label encoding and target encoding for the categorical columns in the dataframe .
* I found that my data was positively skewed. I used the cube root transformation to reduce the skewness and the data was normally distributed.
* I Used the IQR(Inter Quartile Range) method to remove the outliers that present in the data

EXPLORATORY DATA ANALYSIS:
![Image](https://github.com/user-attachments/assets/7c9c9aa2-f686-46ba-afdb-46d7555a62fe)
* The left side image shows the skewness of the column(Kilometer runned) and the right side of the column shows after applying cuberoot transformation, how the data points are normally distributed.


![Image](https://github.com/user-attachments/assets/d82826b6-896c-4560-9380-f29cb353c633)
* This image shows the outlying data that present in the numerical columns.


![Image](https://github.com/user-attachments/assets/d2c293e7-ac11-4d6f-880d-71104e8979ca)  
* This image shows the dataset after applying IQR(INTER QUARTILE RANGE) method to remove the outliers.

![Image](https://github.com/user-attachments/assets/a349d771-cd9e-4a02-a3d5-6522d7b7a3f8)
* The CNG fuel type cars have a very good mileage between  26-33(kmpl).
* The LPG fuel type cars have a very bad mileage between  16 -19(kmpl).

![Image](https://github.com/user-attachments/assets/b1ddd3c2-f0b1-4c39-aa7b-cfdfa7dfeb75)
* Most of the cars that present in the dataset are maruthi  and most of their cars are in the body type of hatchbacks.
* The least number of cars manufactured by mercedez-benz and most of their cars are in the bodytype of sedan.

MACHINE LEARNING:

* I did four machine learning algorithms( Linear regression, Decision Tree Regressor, Random Forest Regression, Gradient Boosting Regressor).
* I did hyper parameter tuning by using Randomized search CV method for Random Forest Regressor and get the best R2 SCORE OF 0.92.
* I also measure the error metrics of the models with mean absolute error, mean squared error , Root mean squared error.

![image](https://github.com/user-attachments/assets/85d6afc7-8d97-439a-80be-4894d701a10f)

STREAMLIT:
* In the streamlit , based on the features given by the Users , the model will predict the price of the car.

CONCLUSION:
* We build a web browser from the machine learning model. The  customer will select  the features  based on their needs and budget. The model predicts the price of the used car based on the input given by the customers . It is very useful for the customer to select the features of the cars that they want and under their budget also. It is very helpful for the sales team in the car Dekho to sell their cars very  quickly and they also achieve their sales target.


  










