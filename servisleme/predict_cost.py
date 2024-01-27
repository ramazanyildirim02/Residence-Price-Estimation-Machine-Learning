import joblib

def predict(value):
    model = joblib.load("model_last.sav")
    return model.predict(value)