"""
# ==========================================================================================================================================================
#                                                                       Author: Enes Altun
                                                  Don't' forget to download detector and add to your working directory to use this script!
                                                                          
# ==========================================================================================================================================================
"""

import cv2
import glob
import dlib
import numpy as np
import os,sys

inputfolder=(r'/content/drive/MyDrive/dlib')       #your input folder on your workspace.
list = os.listdir(inputfolder)
number_files = len(list)
print(" number of files at input folder: ",number_files,)


if not os.path.exists("output"):  #your output file's name. If you'd change it to another, don't forget to change cv2.imwrite function.
    os.mkdir('output')

i=0

for img in glob.glob(inputfolder + "/*.jpg"):  #images in the input file must be in jpg format, otherwise you need to change 'jpg' as your wish.

    target=cv2.imread(img)


    target_gray=cv2.cvtColor(target,cv2.COLOR_RGB2GRAY)
    mask=np.zeros_like(target_gray)


    predictor=dlib.shape_predictor("shape_predictor_81_face_landmarks.dat")  # You can change the predictor with dlib default detector: "shape_predictor_68_face_landmarks.dat"

    detector=dlib.get_frontal_face_detector()

    faces=detector(target_gray)
    for face in faces:
        landmarks=predictor(target_gray,face)
        landmarks_points=[]
        for n in range(0,68):
            x=landmarks.part(n).x
            y=landmarks.part(n).y
            landmarks_points.append((x,y))

        
        points=np.array(landmarks_points,np.int32)
        convexhull=cv2.convexHull(points)
        
        cv2.fillConvexPoly(mask,convexhull,255)
        face_image_1=cv2.bitwise_and(target,target,mask=mask)

        rect=cv2.boundingRect(convexhull)
        (x,y,w,h)=rect
        face_image_2=cv2.rectangle(target,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.imwrite('output/'+str(i)+'.jpg',face_image_1[y:y+h,x:x+w])
        i+=1
print("Done!")
