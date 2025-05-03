from flask import Flask, render_template, request, jsonify, send_from_directory
import json
import random
import os

app = Flask(__name__)

with open('labels.json') as f:
    LABELS = json.load(f)

CURRENT_IMAGE = "kitchen.jpg"  # you can randomize if needed
OBJECTS = LABELS[CURRENT_IMAGE]

@app.route('/')
def home():
    return render_template('index.html', image=CURRENT_IMAGE)

@app.route('/get_prompt', methods=['GET'])
def get_prompt():
    obj = random.choice(OBJECTS)
    return jsonify({"target": obj["label"]})

@app.route('/check_click', methods=['POST'])
def check_click():
    data = request.json
    x = data['x']
    y = data['y']
    target_label = data['target']

    for obj in OBJECTS:
        if obj["label"] == target_label:
            x1, y1, x2, y2 = obj["bbox"]
            inside = (x1 <= x <= x2) and (y1 <= y <= y2)
            return jsonify({
                "correct": inside,
                "bbox": obj["bbox"]
            })
    return jsonify({"error": "Object not found"})

@app.route('/static/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)

if __name__ == '__main__':
    app.run(debug=True)
