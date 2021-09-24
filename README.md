# Extract-Faces

When you need to extract faces from their bodies or heads with photoshop or other apps manually, it's a great amount waste of time.This basic script can extract all faces separately from the input folder and write them into an output folder. Just put your all images into the input folder and let the script process all images that you've put on.

Before the run script, you need to download http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 file or use "shape_predictor_81_face_landmarks.dat" and paste it into your working directory.

With extractFaces script, you can extract all faces from an image but this script doesn't provide you to save faces as jpg individually.   If you want to extract all faces and save them separately you need to use "Extract.Individually.py" script. This script provides you better results than OPENCV's haar cascade models.



An example iamge that processed by the "extractFaces.py" script:

![1200px-STS-106_crew](https://user-images.githubusercontent.com/54986652/97113612-ae7e1400-16fc-11eb-9cf4-0043f83f2aa4.jpg)

![image0006](https://user-images.githubusercontent.com/54986652/97113618-b63db880-16fc-11eb-98eb-5ba7aeec0547.jpg)


The same image that processed by the "Extract.Individually.py":

![image](https://user-images.githubusercontent.com/54986652/134653947-ada0856c-9e5d-4c2a-a26f-a598dcc800af.png)
