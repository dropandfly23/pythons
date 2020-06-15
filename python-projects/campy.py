#pip install opencv-python==3.4.2.17
import cv2
import logging as log
import datetime as dt
from time import sleep
import mailsender
# Author: dropnfly23

import sched, time
cascPath = "config_face_track.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)
video_capture = cv2.VideoCapture(0)
anterior = 0
while True:
    if not video_capture.isOpened():
        print('camera iz kaput :) ')
        sleep(5)
        pass
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if anterior != len(faces):
        anterior = len(faces)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))



    # Display the resulting frame
    #cv2.imshow('Video', frame)
    for x in range(0, 1):
        #print("We're on time %d" % (x))
        check, frame = video_capture.read()
        #cv2.imshow("Capturing", frame)
        ts = str(dt.datetime.now())
        #time.sleep(1)
        #cv2.imwrite('saved_img' + str(dt.datetime.now()) + '.jpg', img=frame)
        cv2.imwrite('ImgFileName.jpg', img=frame)
        #video_capture.release()
        #img_new = cv2.imread('saved_img' + ts + '.jpg', cv2.IMREAD_GRAYSCALE)
        #img_new = cv2.imshow("Captured Image", img_new)
        #cv2.waitKey(1650)

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     print("Turning off camera.")
        #     video_capture.release()
        #     print("Camera off.")
        #     print("Program ended.")
        #     cv2.destroyAllWindows()
        #     break
    break
    # check, frame = video_capture.read()
    # cv2.imshow("Capturing", frame)
    # ts = str(dt.datetime.now())
    # cv2.imwrite('saved_img' + ts + '.jpg', img=frame)
    # video_capture.release()
    # img_new = cv2.imread('saved_img' + ts + '.jpg', cv2.IMREAD_GRAYSCALE)
    # img_new = cv2.imshow("Captured Image", img_new)
    # cv2.waitKey(1650)
    # print("Image Saved")
    # print("Program End")
    #
    #
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     print("Turning off camera.")
    #     video_capture.release()
    #     print("Camera off.")
    #     print("Program ended.")
    #     cv2.destroyAllWindows()
    #     break

    # if cv2.waitKey(1) & 0xFF == ord('s'):
    #
    #     check, frame = video_capture.read()
    #     cv2.imshow("Capturing", frame)
    #     ts=str(dt.datetime.now())
    #     cv2.imwrite('saved_img'+ts+'.jpg', img=frame)
    #     video_capture.release()
    #     img_new = cv2.imread('saved_img'+ts+'.jpg', cv2.IMREAD_GRAYSCALE)
    #     img_new = cv2.imshow("Captured Image", img_new)
    #     cv2.waitKey(1650)
    #     print("Image Saved")
    #     print("Program End")
    #     #cv2.destroyAllWindows()
    #
    #     break
    # elif cv2.waitKey(1) & 0xFF == ord('q'):
    #     print("Turning off camera.")
    #     video_capture.release()
    #     print("Camera off.")
    #     print("Program ended.")
    #     cv2.destroyAllWindows()
    #     break

    # Display the resulting frame
    #cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
mailsender.function_send_mail()
#cv2.destroyAllWindows()