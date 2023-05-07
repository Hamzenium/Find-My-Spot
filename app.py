import cv2
import torch
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import os
import io
import yolov5
import numpy as np


app = Flask(__name__)



@app.route('/')
def main():
    return render_template('index.html')

# @app.route('/detect_vehicles')
# def detect_vehicles():
#     car.detect_objects_flask()

#     return render_template('index.html')

# @app.route('/detect_plates')
# def detect_plates():
#     plate.detect()
#     return render_template('index.html')



if __name__ == '__main__':
    app.run()