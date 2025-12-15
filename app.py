import os
import random
from flask import Flask, jsonify
from truth import truth

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello! The Discipline API is running."

@app.route('/truth', methods=['GET'])
def get_truths():
    item = random.choice(truth)
    return jsonify(item)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)