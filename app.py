
from flask import Flask, request, jsonify, render_template
from json_parse import *

import json

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    try:
        int_features = [int(x) for x in request.form.values()]

        dump_values(int_features)
        int_features = load_jsonFile("test.json")
        sum_1 = sum(int_features)

        def sum_digits(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        output1 = {'result': sum_digits(sum_1)}
        output = json.dumps(output1)
        return render_template('index.html', prediction_text='Digit sum of final result is {}'.format(output))
    except:
        return render_template('index.html', prediction_text='Invalid Input: Note=>only integer value can be accepted')



if __name__ == "__main__":
    app.run(debug=True)

