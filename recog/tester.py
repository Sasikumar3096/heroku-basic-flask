import cv2
import os
import numpy as np


def main():
    path = os.getcwd()
    path = path.replace("\\","/")
    if "recog" in path:
        path.replace("recog", "temp/images.png")
    else:
        path = path + "/temp/images.png"
    #test_img = cv2.imread('C:/Users/Fokal/Documents/college project/heroku-basic-flask/temp/images.png')
    test_img = cv2.imread(path)

    faces_detected, gray_img = faceDetection(test_img)
    if len(faces_detected) == 0:
        print("No face Detected")
        return 1000, 0
    else:
        print("FaceDetected")

    for (x, y, w, h) in faces_detected:
        cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=10)
    #
    # resized_img = cv2.resize(test_img, (750,700))
    # cv2.imshow("face-Detected",resized_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows

    # faces,faceId = fr.labels_for_training_data("test-img")
    # face_recognizer = fr.train_classifier(faces,faceId)
    # face_recognizer.save('trainingData.xml')

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    # face_recognizer.read('trainingData.xml')
    face_recognizer.read('Video-to-data_1.xml')
    name = {1: "Sasi", 2: 'Santhosh', 3: 'Dharun', 4: "Dharun"}

    for face in faces_detected:
        x, y, w, h = face
        roi_gray = gray_img[y:y + h, x:x + h]
        label, confidence = face_recognizer.predict(roi_gray)
        print("Confidence {} \n Label: {}".format(confidence, label))
        draw_rect(test_img, face)
        predicted_name = name[label]
        cv2.destroyAllWindows
        return confidence,label
        if confidence > 37:
            continue

        put_text(test_img, predicted_name, x, y)

    # resized_img = cv2.resize(test_img, (500, 500))
    # cv2.imshow("face-Detected", resized_img)
    # cv2.waitKey(10)
    # cv2.destroyAllWindows

    #
    # for(x,y,w,h) in faces_detected:
    #     cv2.rectangle(test_img, (x,y), (x+w, y+h), (255,0,0), thickness = 10)
    #
    # resized_img = cv2.resize(test_img, (750,700))
    # cv2.imshow("face-Detected",resized_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows


def faceDetection(test_img):
    gray_img = cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)

    face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = face_haar_cascade.detectMultiScale(gray_img,scaleFactor = 1.32, minNeighbors = 5)

    for(x,y,w,h) in faces:
        cv2.rectangle(test_img, (x,y), (x+w, y+h), (255,0,0), thickness = 10)

    # resized_img = cv2.resize(test_img, (750,700))
    # cv2.imshow("face-Detected",resized_img)
    # cv2.waitKey(100)
    # cv2.destroyAllWindows


    return faces, gray_img

def labels_for_training_data(directory):
    faces=[]
    faceID=[]

    for path,subdirnames,filenames in os.walk(directory):
        for filename in filenames:
            id = os.path.basename(path)
            img_path = os.path.join(path,filename)
            print("Path",img_path)

            test_img = cv2.imread(img_path)
            if test_img is None:
                print("Image Not Loaded Properly")
                continue
            faces_rect,gray_img = faceDetection(test_img)
            if len(faces_rect)!=1: #More tha oe face is detected
                print("Not Processed")
                continue
            (x,y,w,h) = faces_rect[0]
            #RegionOfIntrest
            roi_gray = gray_img[y:y+w, x:x+h]
            faces.append(roi_gray)
            faceID.append(int(id))
    return faces,faceID


def train_classifier(faces,faceId):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces, np.array(faceId))

    return face_recognizer

def draw_rect(test_img, face):
    x,y,w,h = face
    cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=10)

def put_text(test_img, text , x,y):
    cv2.putText(test_img, text, (x,y), cv2.FONT_HERSHEY_DUPLEX,3,(255,0,0), 6)



if __name__ == "__main__":
    print(main())
