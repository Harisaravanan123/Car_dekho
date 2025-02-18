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
