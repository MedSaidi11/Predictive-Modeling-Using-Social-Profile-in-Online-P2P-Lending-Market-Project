import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model  = pickle.load(open('model.pkl', 'rb'))
model2  = pickle.load(open('model2.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/borrower_rate')
def borrower_rate():
    return render_template('borrower_rate.html')   

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]

    return render_template('index.html', prediction_text='Prosper Loan Status is  {}'.format(output))    

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

'''Predict Borrower_rate'''
@app.route('/predict_borrower_rate',methods=['POST'])
def predict_borrower_rate():
    '''
    For rendering results on HTML GUI
    '''
    int_features2 = [float(x) for x in request.form.values()]
    final_features2 = [np.array(int_features2)]
    prediction2 = model2.predict(final_features2)

    output2 = round(prediction2[0],4)

    return render_template('borrower_rate.html', prediction_text2=' {}'.format((output2)))    

@app.route('/predict_borrower_rate_api',methods=['POST'])
def predict_borrower_rate_api():
    '''
    For direct API calls trought request
    '''
    data2 = request.get_json(force=True)
    prediction2 = model2.predict([np.array(list(data2.values()))])

    output2 = prediction2[0]
    return jsonify(output2)


''' Calculate ROI'''
@app.route('/calculate',methods=['POST' , 'GET'])
def calculate():
    '''
    For rendering results on HTML GUI
    '''
    roi=''
    if request.method == 'POST' and 'Money Gain' in request.form and 'Cost of Investment' in request.form:

        Money_Gain = float(request.form.get('Money Gain'))
        Cost_of_Investment = float(request.form.get('Cost of Investment'))
        roi = round( ((Money_Gain - Cost_of_Investment )/Cost_of_Investment) * 100,3)
    return render_template('index.html', roi=roi)  

if __name__ == "__main__":
    app.run(debug=True)