import joblib
import os

dirname = os.path.dirname(__file__)

d1_model_file_path = os.path.join(dirname,"model/trained_model_d1.pkl")
d2_model_file_path = os.path.join(dirname,"model/trained_model_d2.pkl")
d3_model_file_path = os.path.join(dirname,"model/trained_model_d3.pkl")
d4_model_file_path = os.path.join(dirname,"model/trained_model_d4.pkl")

oe_file_path = os.path.join(dirname,"model/ordinal_encoder.pkl")
le_file_path = os.path.join(dirname,"model/label_encoder.pkl")

d1_model = joblib.load(d1_model_file_path)
d2_model = joblib.load(d2_model_file_path)
d3_model = joblib.load(d3_model_file_path)
d4_model = joblib.load(d4_model_file_path)

loaded_oe = joblib.load(oe_file_path)
loaded_le = joblib.load(le_file_path)

def predict(input):
    input_encoded = loaded_oe.transform([input])
    
    d1_predicted = d1_model.predict(input_encoded)
    d2_predicted = d2_model.predict(input_encoded)
    d3_predicted = d3_model.predict(input_encoded)
    d4_predicted = d4_model.predict(input_encoded)
    
    dimensions = [d1_predicted,d2_predicted,d3_predicted,d4_predicted]
    
    result = []
    
    for dimension in dimensions:
        decoded = loaded_le.inverse_transform(dimension)
        result.append(decoded[0])
    
    return "".join(result)
    

# Just for testing
if __name__ == "__main__":
    sample_data = ["a","b","b","a","a","a","a","a","b","a","b","b","b","a","b","b","a","b","b","b","b","b","b","b","c","b","a","b","b","b","a","a","a","a","b","a","a","b","b","a","b","a","b","b","b","a","a","a","b","b"]
    print(predict(sample_data))    