import pickle
import json
import pandas as pd
import numpy as np
import config


class Customerchurn(): 
    def __init__(self, CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Gender, Geography):
        self.CreditScore = CreditScore 
        self.Age = Age 
        self.Tenure = Tenure 
        self.Balance = Balance 
        self.NumOfProducts = NumOfProducts
        self.HasCrCard = HasCrCard
        self.IsActiveMember = IsActiveMember
        self.EstimatedSalary = EstimatedSalary
        self.Gender = "Gender_" + Gender
        self.Geography = "Geography_" + Geography

    def load_model(self):
        # with open(config.MODEL_FILE_PATH, "rb") as f:
        with open("best_model.pkl", "rb") as f:

            self.model = pickle.load(f)

        #with open(config.JSON_FILE_PATH, "r") as f:
        with open("project_data.json") as f:

            self.json_data = json.load(f)

    def get_prediction(self):

        self.load_model() # We have to call method >> load_model >> so that we can use their instance variables
        
        Gender_index = self.json_data["columns"].index(self.Gender)
        Geography_index = self.json_data["columns"].index(self.Geography)

        array = np.zeros(len(self.json_data["columns"]))
        array[0]=self.CreditScore
        array[1]=self.Age
        array[2]=self.Tenure
        array[3]=self.Balance
        array[4]=self.NumOfProducts
        array[5]=self.HasCrCard
        array[6]=self.IsActiveMember
        array[7]=self.EstimatedSalary

        array[Geography_index]=1
        array[Gender_index]=1

        
        predicted_churn= self.model.predict([array])[0]
        print(predicted_churn)
    
        if predicted_churn == 0:
            return 'The customers are unlikely to leave'
        else:
            return 'The customers are likely to leave.'


if __name__ == "__main__":
    CreditScore = 600
    Age= 55
    Tenure = 2
    Balance =1
    NumOfProducts = 1
    HasCrCard = 1
    IsActiveMember = 0  
    EstimatedSalary = 88000
    Gender =  'Male'
    Geography =  'France'

    obj = Customerchurn(CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Gender, Geography)
    charges = obj.get_prediction()
    