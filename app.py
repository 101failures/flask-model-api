from flask import Flask, request, jsonify
app = Flask(__name__)

class DummyModel:
    def predict(self, X):
        return [sum(row) for row in X]

MODEL = DummyModel()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    X = data["X"]
    y = MODEL.predict(X)
    return jsonify({"y": y}), 200