import joblib

loaded_model = joblib.load('model/trained_model.pkl')
loaded_oe = joblib.load('model/ordinal_encoder.pkl')
loaded_le = joblib.load('model/label_encoder.pkl')

sample_data = ["a","b","b","a","a","a","a","a","b","a","b","b","b","a","b","b","a","b","b","b","b","b","b","b","c","b","a","b","b","b","a","a","a","a","b","a","a","b","b","a","b","a","b","b","b","a","a","a","b","b"]


def predict(input):
    input_encoded = loaded_oe.transform([input])
    predict = loaded_model.predict(input_encoded)
    decoded_output = loaded_le.inverse_transform(predict)
    return decoded_output[0]
    

# Just for testing
if __name__ == "__main__":
    print(predict(sample_data))    