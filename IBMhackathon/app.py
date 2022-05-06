import os
from flask import Flask, render_template, request
from classifier import ocr_core
import cv2

img=cv2.imread('social.png')

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)

@app.route('/')
def upload_image():
    decoded_text = ocr_core(img)
    print(decoded_text)
