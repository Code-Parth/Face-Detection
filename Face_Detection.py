import cv2
import numpy as np
import os

image_dir = 'images/'
images = []
for filename in os.listdir(image_dir):
    image = cv2.imread(os.path.join(image_dir, filename))
    images.append(image)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_images = []
for image in images:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        face_images.append(gray[y:y+h, x:x+w])

face_features = []
for face_image in face_images:
    face_features.append(np.mean(face_image))

template = np.mean(face_features, axis=0)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        new_face = gray[y:y+h, x:x+w]
        new_face_feature = np.mean(new_face)
        if np.linalg.norm(new_face_feature - template) < 100:
            cv2.putText(frame, "Match found!", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            cv2.putText(frame, "No match found.", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('face recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
