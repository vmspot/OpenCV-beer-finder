import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_beercan.xml')

cap = cv2.VideoCapture(0)

while(True):
    # Capture video
    ret, frame = cap.read()
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
        roi_color = frame[y:y+h, x:x+w]
      
        #img_item = "image.png"
        #cv2.imwrite(img_item, roi_gray)

        color = (255, 0, 0) #BGR 0-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    # Display the color frame with surrounding rectangle
    cv2.imshow('beer-hunter',frame)
    #cv2.imshow('gray',gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Close the application
cap.release()
cv2.destroyAllWindows()