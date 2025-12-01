import joblib
# load model sekali saja (bukan di dalam fungsi)
model = joblib.load("rf_model.sav")

def predict(data):
    return model.predict(data)
