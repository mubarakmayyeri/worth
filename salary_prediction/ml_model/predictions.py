import pickle
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'rf_model.pkl')

with open(model_path, 'rb') as file:
    rf_model = pickle.load(file)


def make_perdiction(input):
    pred = rf_model.predict(input)

    return pred