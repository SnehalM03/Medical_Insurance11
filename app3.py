from flask import Flask,request,render_template,jsonify
from utils import MedicalInsurance
import config
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/prediction',methods=['POST'])
def prediction():
    data=request.form
    print(data)
    age=data['age']
    gender=data['gender']
    bmi=data['bmi']
    children=data['children']
    smoker=data['smoker']
    region=data['region']

    med_ins=MedicalInsurance()
    pred_charges=med_ins.get_predicted_charges(age,gender,bmi,children,smoker,region)
    return jsonify ({
        'Prediction of Medical Insurance Charges':pred_charges
        })

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)
