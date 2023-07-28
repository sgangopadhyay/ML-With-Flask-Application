# app.py
# Main Flask file

from flask import Flask
from flask import request
from flask import render_template
import pickle
import numpy as np

# create an object of the class Flask
app = Flask(__name__)

# read the model from the pickle file
model = pickle.load(open('suman_test_model.pkl', 'rb'))

# URL for home-page/index web page
@app.route("/")
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    # extract all the information from the HTML form
    blood_sugar_features = [int(x) for x in request.form.values()]
    print(blood_sugar_features)
    final_result = [np.array(blood_sugar_features)]
    prediction = model.predict(final_result)
    output = round(prediction[0], 2)
    return render_template('index.html', output=output)


# Flask server

if __name__ == "__main__":
    app.run(port=5000, debug=True)
