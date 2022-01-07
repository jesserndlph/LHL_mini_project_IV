## Python test file for flask to test locally
import requests as r
import pandas as pd
import json


# base_url = 'http://127.0.0.1:5000/' #base url local host
base_url = 'ec2-18-223-135-49.us-east-2.compute.amazonaws.com:8888/'



json_data = {
"ApplicantIncome":3273,
"CoapplicantIncome":1820,
"Credit_History":1.0,
"Dependents":2,
"Education_Not Graduate":1,
"Gender_Male":1,
"LoanAmount_log":4.394449,
"Loan_Amount_Term":360,
"Married_Yes":1,
"Property_Area_Semiurban":0,
"Property_Area_Urban":1,
"Self_Employed_No":1,
"Self_Employed_Yes":0,
"Total_Income_log":8.535622
}


test = pd.read_csv("test.csv", index_col=0)
test = test.to_json(orient='records')
test = json.loads(test)


# Get Response
# response = r.get(base_url + 'helloworld')
#response = r.post(base_url + "predict", json = json_data)
response = r.post(base_url + "predict", json = test)

if response.status_code == 200:
    print('...')
    print('request successful')
    print('...')
    print(response.json())
else:
    print('request failed')