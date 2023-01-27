import cv2
import numpy as np
import os


class FaceRecognizer:
    def __init__(self, image_dir, cascade_path):
        self.image_dir = image_dir
        self.cascade_path = cascade_path
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        self.template = self.create_template()

    def create_template(self):
        images = []
        for filename in os.listdir(self.image_dir):
            image = cv2.imread(os.path.join(self.image_dir, filename))
            images.append(image)

        face_images = []
        for image in images:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                face_images.append(gray[y:y+h, x:x+w])

        face_features = []
        for face_image in face_images:
            face_features.append(np.mean(face_image))

        template = np.mean(face_features, axis=0)
        return template

    def recognize(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                new_face = gray[y:y+h, x:x+w]
                new_face_feature = np.mean(new_face)
                if np.linalg.norm(new_face_feature - self.template) < 100:
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


recognizer = FaceRecognizer('images/', 'haarcascade_frontalface_default.xml')
recognizer.recognize()
