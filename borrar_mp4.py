#Code by Omar Moya Romero :)
#Use this script in order to delete any mp4 video file of a directory that is shorter than an stipulated duration

import cv2
import os
dir_path = os.getcwd() # Ruta actual
file_extension = ".mp4"
minimum_duration = 4
files = os.listdir(dir_path)
for filename in files:
    if file_extension in filename.lower():
        print(str(filename))
        cap = cv2.VideoCapture(filename)
        fps = cap.get(cv2.CAP_PROP_FPS)      # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count/fps
        print('duration (S) = ' + str(duration))
        cap.release()
        if duration <= minimum_duration:
            print("This video has been deleted.")
            file_path = dir_path + '\\' + filename
            print(file_path)
            os.remove(file_path)
        continue

