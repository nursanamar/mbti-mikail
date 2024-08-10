import joblib
import os

dirname = os.path.dirname(__file__)

model_file_path = os.path.join(dirname,"model/trained_model.pkl")
oe_file_path = os.path.join(dirname,"model/ordinal_encoder.pkl")
le_file_path = os.path.join(dirname,"model/label_encoder.pkl")

loaded_model = joblib.load(model_file_path)
loaded_oe = joblib.load(oe_file_path)
loaded_le = joblib.load(le_file_path)

sample_data = ["a","b","b","a","a","a","a","a","b","a","b","b","b","a","b","b","a","b","b","b","b","b","b","b","c","b","a","b","b","b","a","a","a","a","b","a","a","b","b","a","b","a","b","b","b","a","a","a","b","b"]


def predict(input):
    input_encoded = loaded_oe.transform([input])
    predict = loaded_model.predict(input_encoded)
    decoded_output = loaded_le.inverse_transform(predict)
    return decoded_output[0]
    

# Just for testing
if __name__ == "__main__":
    print(predict(sample_data))    