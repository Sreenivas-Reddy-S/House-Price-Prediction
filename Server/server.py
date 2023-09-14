from flask import Flask, request, jsonify
# It contains all the core logic or routing logic.
import util
app = Flask(__name__)

# Interpreting an http endpoint using @app.route.


@app.route('/get_location_names', methods=['GET', 'POST'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-origin', '*')
    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    response = jsonify({
        'estimated_price' : util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add("Access-control-allow-origin", '*')
    return response


if __name__ == '__main__':
    print("Starting the python flask server for house price prediction")
    util.load_saved_artifacts()
    app.run(host="127.0.0.1", port=5002)