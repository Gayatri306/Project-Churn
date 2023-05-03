from flask import Flask ,jsonify,render_template,request
from utils import Customerchurn
import config

app = Flask(__name__)


@app.route("/")
def welcome():
    print("Welcome to the Customer Churn prediction")
    return render_template("index.html")

@app.route("/Customer_churn")
def predicted_class():
        if request.method == "GET":
            print("We are using GET Method")
            #print("Printing Data here :",request.form)
    
    
            # data = request.form
        
            CreditScore = eval(request.args.get("CreditScore"))
            Age = eval(request.args.get("Age"))
            Tenure = eval(request.args.get("Tenure"))
            Balance = eval(request.args.get("Balance"))
            NumOfProducts = eval(request.args.get("NumOfProducts"))
            HasCrCard = eval(request.args.get("HasCrCard"))
            IsActiveMember = eval(request.args.get("IsActiveMember"))
            EstimatedSalary = eval(request.args.get("EstimatedSalary"))
            #Gender = request.args.get("Gender")
            Gender =request.args.get("GenderVal", default="", type=str)
            print("#####Gender :",Gender)
           #Geography = request.args.get("Geography")
            Geography =request.args.get("Geography", default="", type=str)
            print("#####Geography :",Geography)
           
            col = Customerchurn(CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Gender, Geography)
            pred = col.get_prediction()
            return render_template("index.html", prediction = pred)
            

        else:
            print("We are using POST Method")

            CreditScore = eval(request.form.get("CreditScore"))
            Age = eval(request.form.get("Age"))
            Tenure = eval(request.form.get("Tenure"))
            Balance = eval(request.form.get("Balance"))
            NumOfProducts = eval(request.form.get("NumOfProducts"))
            HasCrCard = eval(request.form.get("HasCrCard"))
            IsActiveMember = eval(request.form.get("IsActiveMember"))
            EstimatedSalary = eval(request.form.get("EstimatedSalary"))
            Gender = request.form.get("Gender")
            Geography = request.form.get("Geography")


            col = Customerchurn(CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Gender, Geography)
            pred = col.get_prediction()
            return render_template("index.html", prediction = pred)
      

    

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=config.PORT_NUMBER, debug=True)