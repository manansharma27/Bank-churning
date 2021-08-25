# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('classifier.pkl', 'rb'))

@app.route('/')
def hello():
    return render_template('index.html')
    
@app.route('/predict',methods=['GET','POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == "POST":
        myDict = request.form
        CreditScore= int(myDict['credit'])
        Age = int(myDict['age'])
        Tenure = int(myDict['tenure'])
        Balance = float(myDict['balance'])
        NoOfProducts = int(myDict['noproducts'])
        IsActiveMember = int(myDict['isactive'])
        HasCrCard = int(myDict['crcard'])
        EstimatedSalary = float(myDict['estimatedsalary'])
        CreditScoreGivenAge = float(myDict['creditperage'])
        Geography = int(myDict['country'])
        Gender = int(myDict['gender'])
        int_features = [[CreditScore,Age,Tenure,Balance,NoOfProducts,IsActiveMember,HasCrCard,EstimatedSalary,CreditScoreGivenAge,Geography,Gender]]
        prediction = model.predict(int_features)

    if(prediction == 0):
        return render_template('index.html',output="Congratulations! This Customer will be loyal to bank, will not leave the bank.")
    else:
        return render_template('index.html',output="It is predicted that this Customer will leave the Bank. Steps below mentioned can be helpful to retain customer. \nThe bank can reward the customer with benefits,increase in interest rate,can give the customers new features in credit card and givings some perks, offers and premium plans to make customer happy.")

    
    
if __name__ == "__main__":
    app.run(debug=True)