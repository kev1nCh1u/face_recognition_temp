import face_recognition
import cv2
import numpy as np

import serial
import threading

import os

# 串接口設定
try:
    serialProtocol = serial.Serial('COM10', 9600, timeout=1)
except:
    print('comport not right check line 12')
    exit()

# 溫度紀錄 [0]:環境溫度 [1]:物體溫度
serialArray = np.zeros(2)

# 讀取arduino溫度
def tempCatch():
    global serialArray
    while 1:
        serialRead = serialProtocol.readline()
        serialDecode = serialRead.decode('utf-8')
        serialArray = serialDecode.split()
        #print(serialArray)

# 建立一個子執行緒
t = threading.Thread(target = tempCatch)
# 保護
t.daemon = True
# 執行該子執行緒
t.start()

# 查看有哪些照片
imgDirectory = 'img/face_recognition_known/'
nowDirectory = os.getcwd() + '/' + imgDirectory
imgFiles = os.listdir(nowDirectory)

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# 匯入所有照片來訓練辨識
recognition_face_encoding = np.empty((len(imgFiles),128))
for i in range(len(imgFiles)):
    recognitionImage = face_recognition.load_image_file(imgDirectory + imgFiles[i])
    recognition_face_encoding[i] = face_recognition.face_encodings(recognitionImage)[0]

# 檔名轉人名處理
imgFilesName = imgFiles
for i in range(len(imgFiles)):
    imgFilesName[i] = str.split(imgFiles[i],".")[0]

# Create arrays of known face encodings and their names
known_face_encodings = recognition_face_encoding
known_face_names = imgFilesName

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:

    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        
        # 發燒時換顏色
        if (float(serialArray[1]) <= 37.):
            cv2Color = (0, 255, 0)
        else:
            cv2Color = (0, 0, 255)

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), cv2Color, 2)

        # Draw a label with a name below the face + temp
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), cv2Color, cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # 溫度顯示
    try:
        cv2.putText(frame, serialArray[0] +"*C", (10, 50), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 0, 0), 1)
    except:
        cv2.putText(frame, 'None', (10, 50), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 0, 0), 1)
        print('Ambient temp error!')
    try:
        cv2.putText(frame, serialArray[1] +"*C", (10, 100), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 0, 255), 1)
    except:
        cv2.putText(frame, 'None', (10, 100), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 0, 0), 1)
        print('Object temp error!')

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
