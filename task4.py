import pandas
import os


ds=pandas.read_csv('salaryData.csv')

x=ds['YearsExperience'].values.reshape(-1,1)
y=ds['Salary']

from sklearn.linear_model import LinearRegression

#train the model
model=LinearRegression()
model.fit(x,y)

while True:
    user_data=input( "Enter your years of experience = \n" )
    exp=float(user_data)
    predicted_value=model.predict([[exp]])
    print("Predicted Salary {} yrs ".format(exp)+" {}".format(predicted_value[0]) + " INR\n")
