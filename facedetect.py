import cv2
import sys
image = cv2.imread("aadar.jpg")
cv2.imshow("",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
)

print("Found {0} Faces!".format(len(faces)))
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_color = image[y:y + h, x:x + w] 
print("[INFO] Object found. Saving locally.") 
cv2.imwrite('img1.jpg', roi_color) 

image = cv2.imread("liv.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
)

print("Found {0} Faces!".format(len(faces)))
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_color = image[y:y + h, x:x + w] 
print("[INFO] Object found. Saving locally.") 
cv2.imwrite('img2.jpg', roi_color) 
#_______________________________________________________________________________________________________________________
# from deepface import DeepFace
# result  = DeepFace.verify("aadhar.jpg", "liv.png")
# #results = DeepFace.verify([['img1.jpg', 'img2.jpg'], ['img1.jpg', 'img3.jpg']])
# print("Is verified: ", result["verified"])
#_______________________________________________________________________________________________________________________
# import face_recognition 
# known_image = face_recognition.load_image_file("img2.jpg") 
# unknown_image = face_recognition.load_image_file("img1.jpg") 
 
# biden_encoding = face_recognition.face_encodings(known_image)[0] 
# unknown_encoding = face_recognition.face_encodings(unknown_image)[0] 
 
# results = face_recognition.compare_faces([biden_encoding], unknown_encoding)