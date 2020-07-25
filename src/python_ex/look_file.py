import os

nowDirectory = os.getcwd()
print(nowDirectory)

nowDirectory = nowDirectory + '/img/face_recognition_known/'
print(nowDirectory)

files = os.listdir(nowDirectory)
print(files)