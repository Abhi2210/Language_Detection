import pickle
from http.client import error

from sklearn.feature_extraction.text import CountVectorizer
from constants.constants import Constants

class ModelServing:
    def __init__(self):
        # self.model = Constants.PATH
        try:
            self.model = pickle.load(open(Constants.MODEL_PATH, 'rb'))
            self.vector = pickle.load(open(Constants.VECTOR_PATH, 'rb'))
        except:
            return "Unable to Load Model"

    def predict(self, text):
        try:
            data = self.vector.transform([text]).toarray()
            print(data)
            out =  self.model.predict(data)
            predictions = max(self.model.predict_proba(data)[0])
            print(out[0],predictions, round(predictions, 2))
            return out[0], round(predictions, 2)
        except:
            return "Language Not Supported"

