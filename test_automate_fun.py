import deepface
from deepface import DeepFace
from flask import Flask, request, jsonify, make_response
import cv2
import numpy as np
app = Flask(__name__)

def facematch(livpath,cardpath):
    key_list=[]
    resultdic={}
    #,"OpenFace","DeepFace","Facenet"
    metrics = ["cosine", "euclidean", "euclidean_l2"]
    models = ["VGG-Face","Dlib"]
    for model in models:
        for metric in metrics:
            result  = DeepFace.verify(livpath,cardpath,model_name = model, distance_metric = metric)
            resultdic[model+','+metric]=result
    res = resultdic
  
    return res
