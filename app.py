import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
model=pickle.load(open('water_quality_model.pkl','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))

# app.route will re-direct to the web page
@app.route('/')
def home():
    return render_template('home_page.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data'] # this mean the given data will stored in the data variable that is been captured.
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=model.predict_proba(new_data)[0,1] 
    output=round(output, 2)
    print(output*100)
    return jsonify(output*100)

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    input_values=scalar.transform(np.array(data).reshape(1,-1))
    print(input_values)
    output=model.predict_proba(input_values)[0,1] 
    output=round(output, 2)
    return render_template("home_page.html",predicted_text="It is {} % safe to drink".format(output*100))


if __name__=="__main__":
    app.run(debug=True)



