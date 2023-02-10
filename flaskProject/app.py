from flask import Flask, jsonify,request
from utils.modelServing import ModelServing
import jsonpickle

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Welcome the Language Detection host page!'

@app.route('/detect', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        model = ModelServing()
        json = request.json
        print(json["text"])
        res, prob = model.predict(json["text"])
        if prob<0.45:
            return "Unidentified language. Kindly add more words \n" \
                   "NOTE: Currently we support only  'Portugeese', 'Russian', 'Spanish', 'Sweedish', 'Turkish'"                             \
                   " 'Danish', 'Dutch', 'English', 'French', 'German', 'Italian'" \


        data  = {
            "Language": res,
            "Prob" : prob
        }
        return jsonify(data)
    else:
        return 'Content-Type not supported!'

if __name__ == '__main__':
    app.run()
