import cv2 as cv 
import numpy as np 
import os 


people=['ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']
DIR=r'../Resources/Faces/train'
haar_cascade=cv.CascadeClassifier('haar_face.xml')

features=[]
labels=[]

def create_train():
    #search every person in people vector
    for person in people:
        #for every person find the path located at the DIR and assign 
        #that person number label 
        path=os.path.join(DIR,person)
        label=people.index(person)

        #for every image located at the path of the person
        #read the image , convert to gray for cascading
        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            #save only the necessary parts of the image 
            #and append to the features and labels vector
            for(x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print(f'length of features = {len(features)} ')
print(f'length of labels = {len(labels)} ')


face_recognizer=cv.face.LBPHFaceRecognizer_create()
features=np.array(features,dtype='object')
labels=np.array(labels)

#train recognizer on the features and labels vector 
face_recognizer.train(features,labels)
np.save('features.npy',features)
np.save('labels.npy',labels)
face_recognizer.save('face_trained.ym')
cv.waitKey(0)