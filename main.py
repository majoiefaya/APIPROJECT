from ast import Str
from tokenize import StringPrefix
from fastapi import FastAPI
from typing import Union
import cv2
from cvzone.HandTrackingModule import HandDetector
from models import Student
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app=FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



@app.get('/')
def  read_root():
    return {
        "hello" : "world"
        }
    
@app.get('/Students/ReadAllstudents')    
def  read_students(token: str = Depends(oauth2_scheme)):
  return {"token": token}

@app.get('/Students/ReadStudentById/{student_id}')    
def  read_student(token: str = Depends(oauth2_scheme)):
    return {
        "token": token
    }
    
@app.get('/Students/GetStudentById/{student_id}')    
async def get_student(student:int,token: str = Depends(oauth2_scheme)):
    return{"student_id":student,
           "token": token}
    
@app.get('/Students/GetStudentById/{student_id}')    
async def get_student(student:int,token: str = Depends(oauth2_scheme)):
    return{"student_id":student,
           "token": token}
    
@app.post('/Students/AjouterStudent/,response_model=StudentMatri')    
async def create_student(student:Student,token: str = Depends(oauth2_scheme)):
    matricule=student.filiere+ "/"+ student.nom
    student_dict=student.dict()
    student_dict.update({"matricule":matricule})
    return student_dict
    return {"token": token}
    

@app.post('/Students/UpdateStudent/{student_id},response_model=StudentMatri')    
async def Update_student(student:Student,token: str = Depends(oauth2_scheme)):
    matricule=student.filiere+ "/"+ student.nom
    student_dict=student.dict()
    student_dict.update({"matricule":matricule})
    return student_dict
    return {"token": token}
    
    

@app.post('/Students/DeleteStudent/{student_id},response_model=StudentMatri')    
async def Update_student(student:Student,token: str = Depends(oauth2_scheme)):
    matricule=student.filiere+ "/"+ student.nom
    student_dict=student.dict()
    student_dict.delete({"matricule":matricule})
    return student_dict
    return {"token": token}
    
    

@app.get('/HandManip')
def HandManip():
    cap=cv2.VideoCapture(0)
    detector=HandDetector(detectionCon=0.0,maxHands=2)

    while True:
        succes,img=cap.read()
        hands,img=detector.findHands(img,1)
        hands,img=detector.findHands(img,draw=True)

        #Hand-dict(lmlist-bbox-center-type)
        if hands:
            #Hand1
            hand1=hands[0]
            lmlist1=hand1["lmList"]
            bbox1=hand1["bbox"]#bounding box info x,y,w,h
            centerPoint1=hand1["center"]#center of the hand cx cy
            handType1=hand1["type"]#hand type left right

    ##        print(len(lmlist1),lmlist1)
    ##        print(bbox1)
    ##        print(centerPoint1)
    ##        print(handType1)
            fingers1=detector.fingersUp(hand1)
            #length,info,img=detector.findDistance(lmlist1[8],lmlist1[12],img)
            #length,info=detector.findDistance(lmlist1[8],lmlist1[12])

            if len(hands)==2:
                hand2=hands[0]
                lmlist2=hand2["lmList"]
                bbox2=hand2["bbox"]#bounding box info x,y,w,h
                centerPoint2=hand2["center"]#center of the hand cx cy
                handType2=hand2["type"]#hand type left right
                fingers2=detector.fingersUp(hand2)
                print(fingers1,fingers2)
                length,info,img=detector.findDistance(lmlist1[8],lmlist2[8],img)
                length,info,img=detector.findDistance(centerPoint1,centerPoint2,img)     
        
        cv2.imshow("Image",img)
        
        return cv2.waitKey(1)
        
