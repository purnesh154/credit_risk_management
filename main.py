import pickle
from flask import Flask, request, jsonify
from model_files.ml_model import predict_defaulter
app = Flask('app')
@app.route('/predict', methods=['POST'])
def predict():
    credit = request.get_json()
    print(credit)
    with open('./model_files/model.bin', 'rb') as f_in:
        model = pickle.load(f_in)
        f_in.close()
    predictions = predict_defaulter(credit, model)
    result = {
        'defaulter_prediction': list(predictions)
    }
    return jsonify(result)