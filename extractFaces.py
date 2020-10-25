import cv2
import glob
import dlib
import numpy as np
import os,sys

inputfolder=(r'C:\opencv\inpu')       #your input folder on your workspace.
list = os.listdir(inputfolder)
number_files = len(list)
print(" number of files at input folder: ",number_files,)


if not os.path.exists("output"):  #your output file' name. If you'd change it to another, don't forget to change cv2.imwrite function.
    os.mkdir('output')
else:
    print("Processing stopped. 'Output' file already exists at the current workspace. You need to delete it or move to another directory. " )
i=0

for img in glob.glob(inputfolder + "/*.jpg"):  #images in the input file must be in jpg format, otherwise you need to change 'jpg' as your wish.

    target=cv2.imread(img)


    target_gray=cv2.cvtColor(target,cv2.COLOR_RGB2GRAY)
    mask=np.zeros_like(target_gray)

    predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    detector=dlib.get_frontal_face_detector()

    faces=detector(target_gray)
    for face in faces:
        landmarks=predictor(target_gray,face)
        landmarks_points=[]
        for n in range(0,68):
            x=landmarks.part(n).x
            y=landmarks.part(n).y
            landmarks_points.append((x,y))

        #cv2.circle(target,(x,y),3,(0,255,0),-1)
        points=np.array(landmarks_points,np.int32)
        convexhull=cv2.convexHull(points)
        #cv2.polylines(target,[convexhull],True,(255,0,0),3)
        cv2.fillConvexPoly(mask,convexhull,255)

        target_face_1=cv2.bitwise_and(target,target,mask=mask)
        cv2.imwrite("output/image%04i.jpg" % i, target_face_1)
        i += 1
print('process has been successfully completed')
