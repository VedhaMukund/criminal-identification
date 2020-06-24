# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:01:12 2019

@author: vu
"""

import numpy as np
import cv2
from datetime import datetime  
import tkinter
from tkinter import * 
import smtplib

#code fot timestamp
now = datetime.now()
timestamp = datetime.timestamp(now)


#code for face_reco
face_cascade = cv2.CascadeClassifier(r'F:\Documents\miniproject\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create();
rec.read(r"F:\Documents\miniproject\trainingdata.yml")
id=0
i=0
font = cv2.FONT_HERSHEY_SIMPLEX
#font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(id==57):
            id="vidul"    
        if id==55:
            id="CRIMINAL"
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            i=i+1
            
            
        else:
            id="unknown" 
            
        #cv2.PutText(img,str(id),(x,y+h),font,255)
        cv2.putText(img,str(id), (x,y),cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
    cv2.imshow('img',img)
    #cv2.imshow('time',timestamp)
    
    if i==1:
        print("ALERT\n NAME:UTHIRAPATHI ESWARAN \n INDIFICATION:CRIMINAL \n DATE OF BIRTH:28 MAR 2001 \n AGE:18 \n CITY:SALEM-TAMILNADU")
        s = smtplib.SMTP('smtp.gmail.com', 587) 

        s.starttls() 
        s.login("vedhamukund@gmail.com", "9585012123") 
        message = "ALERT\n NAME:UTHIRAPATHI ESWARAN \n INDIFICATION:CRIMINAL \n DATE OF BIRTH:28 MAR 2001 \n AGE:18 \n CITY:SALEM-TAMILNADU"
        s.sendmail("vedhamukund@gmail.com@gmail.com", "vedhamukund.1805155@srec.ac.in", message) 
        s.quit()    
    if cv2.waitKey(1) == ord('q'):
        break
    
       
cap.release()

cv2.destroyAllWindows()