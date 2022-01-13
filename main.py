import cv2
import webbrowser
import pyzbar.pyzbar as pyzbar
from face_recognition.api import face_locations
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'Attend'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('attendance.csv','r+') as f:
         myDataList = f.readlines()
         nameList = []
         for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
         if name not in nameList:
            now = datetime.now()
            dString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dString}')


cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
while True:
    _, frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    
    for obj in decodedObjects:
        print("Data", obj.data)
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,(255, 0, 0), 3)
    cv2.imshow('Frame',frame)
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        print("Type:", obj.type)
        print("Data: ", obj.data, "\n")
        path = "C:\\Users\\hpadmin\\Desktop\\New folder\\"+str(obj.data)
        webbrowser.open(path) # Opens 'PycharmProjects' folder
        print("Match Found!");
        
        current_file = open(path, "r")
        print(current_file.read())
        print("Running face recognition......");
        encodeListKnown = findEncodings(images)
        print('Encoding Complete')
        success, img = cap.read()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
    
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                # print(name)
                y1,x2,y2,x1 = faceLoc
                y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                markAttendance(name)
                print("Name:"+name)
                print("Access Granted!")
        current_file.close()
    key = cv2.waitKey(1)
    if key == 27:
        break
# decodedObjects = pyzbar.decode(frame)
# for obj in decodedObjects:
#     print("Type:", obj.type)
#     print("Data: ", obj.data, "\n")
#     path = "C:\\Users\\hpadmin\\Desktop\\New folder"+str(obj.data)
#     webbrowser.open(path) # Opens 'PycharmProjects' folder
#     current_file = open(path, "r")
#     print(current_file.read())
#     current_file.close()