"""
https://www.youtube.com/watch?v=mrExsjcvF4o
"""

import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('regressor.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    print(final_features)
    #prediction = model.predict(final_features)
    prediction = np.expm1(reg.predict([[0, 0, 1, np.log1p(2), np.log1p(120)]]))
    output = round(prediction[0], 2)

    return render_template('index.html',
            prediction_text=f'Preço do Aluguel R$ {output}')

if __name__ == '__main__':
    app.run(debug=True)
