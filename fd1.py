import deepface
from deepface import DeepFace
from flask import Flask, request, jsonify, make_response
import cv2
import numpy as np
app = Flask(__name__)
@app.route('/facematch',methods=["POST"])
def facematch():
    try:
        liv = request.files.get('liv')
        card = request.files.get('card')
    except:
        return make_response(jsonify(
            {
                'status' : 'fail',
                'desc':'Error in getting images',
                'result' : {}
            }
        ), 207)
    try:
        liv.save('liv.jpg')
        card.save('card.jpg')
    except:
        return make_response(jsonify(
            {
                'status' : 'fail',
                'desc':'Error in saving images',
                'result' : {}
            }
        ), 207)
    # liv_img = cv2.imread('liv.jpg')
    # card_img = cv2.imread('card.jpg')
    # liv_gray = cv2.cvtColor(liv_img, cv2.COLOR_BGR2GRAY)
    # card_grey = cv2.cvtColor(card_img, cv2.COLOR_BGR2GRAY)
    # faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    # liv_faces = faceCascade.detectMultiScale(
    #         liv_gray,
    #         scaleFactor=1.3,
    #         minNeighbors=3,
    #         minSize=(30, 30)
    # )
    # card_faces = faceCascade.detectMultiScale(
    #         card_grey,
    #         scaleFactor=1.3,
    #         minNeighbors=3,
    #         minSize=(30, 30)
    # )
    # print("Found {0} Faces!".format(len(liv_faces)))
    # print("Found {0} Faces!".format(len(card_faces)))
    # # for (x, y, w, h) in liv_faces:
    # #     cv2.rectangle(liv_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # for (x, y, w, h) in liv_faces:
    #     cv2.rectangle(liv_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #     roi_color = liv_img[y:y + h, x:x + w]
    #     print("[INFO] Object found. Saving locally.")
    #     cv2.imwrite('liv.jpg', roi_color)

    # for (x, y, w, h) in card_faces:
    #     cv2.rectangle(card_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # #cv2.imwrite('liv.jpg', liv_img)
    # cv2.imwrite('card.jpg',card_img)


    try:
        key_list=[]
        resultdic={}
        #
        metrics = ["cosine", "euclidean", "euclidean_l2"]
        models = ["VGG-Face","OpenFace","DeepFace", "Dlib","Facenet"]
        for model in models:
            for metric in metrics:
                result  = DeepFace.verify("liv.jpg","card.jpg",model_name = model, distance_metric = metric)
                resultdic[model+','+metric]=result
                
                
          
            
    except:
        return make_response(jsonify(
            {
                'status' : 'fail',
                'desc':'Error in finding face and matching',
                'result' : resultdic
            }
        ), 207)
    print()
    res = resultdic
    return res

