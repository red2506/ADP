import cv2
import webbrowser
import pyzbar.pyzbar as pyzbar




  
'''
cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

a="https://www.youtube.com/watch?v=dQw4w9WgXcQ"

while True:
    _, img = cap.read()

    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    # check if there is a QRCode in the image
    if data:
        a=data
        break
    '''
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
        current_file = open(path, "r")
        print(current_file.read())
        current_file.close()
    # cv2.imshow("QRCODEscanner", frame)    
    key = cv2.waitKey(1)
    if key == 27:
        break
    #if cv2.waitKey(1) == ord("q"):
     #       break
    
    #b=webbrowser.open(str(a))
    #cap.release()
   # cv2.destroyAllWindows()
decodedObjects = pyzbar.decode(frame)
for obj in decodedObjects:
    print("Type:", obj.type)
    print("Data: ", obj.data, "\n")
    path = "C:\\Users\\hpadmin\\Desktop\\New folder"+str(obj.data)
    webbrowser.open(path) # Opens 'PycharmProjects' folder
    current_file = open(path, "r")
    print(current_file.read())
    current_file.close()