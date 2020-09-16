import flask
from flask import *
import pandas as pd
import numpy as np
import csv
import os
from csv import writer 
import datetime
import random
import json
import io
import sys
import glob
import shutil
import cv2
from pyzbar.pyzbar import decode
import re
from werkzeug.utils import secure_filename
import cv2

__author__ = 'lambert'

app = Flask(__name__)


def create_dir(file):
    if not os.path.exists(file):
        os.mkdir(file)

def show_data(img):
    image = cv2.imread(img)
    detectedBarcodes = decode(image)
    for barcode in detectedBarcodes:
        data = barcode.data
        type_ = barcode.type
        return data, type_

@app.route("/")
def index():
    return "Success"


@app.route("/barcode", methods=['POST'])
def barcode():
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'data_in')
    create_dir(target)

    # global destination, filename, json_file
    if request.method == 'POST':

        for file in request.files.getlist("file"):
            print('file: ')
            filename = file.filename
            print(filename)
            destination = "/".join([target, filename])
            print(destination)
            file.save(destination)

        if destination.endswith(".jpg") or destination.endswith(".JPG") or destination.endswith(".png") or destination.endswith(".PNG") or destination.endswith(".jpeg") or destination.endswith("JPEG"):
            data, type_ = show_data(destination)

            return (data)

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0', port=5000, debug=False)


