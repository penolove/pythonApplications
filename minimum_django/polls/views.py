from django.shortcuts import render
from django.conf import settings
import cv2
import sqlite3
import glob
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def index(request):
    #pass parameter to template
    #return render(request, 'polls/index2.html',{'post':"kerker"})
    
    #pass parameter to template
    return render(request, 'polls/index1.html',{'post':"kerkerman"})
    
    #using template
    #return render(request, 'polls/index.html')

    #using some web technique    
    #return render(request, 'bootstrap/tutorial/DynamicTabs.html')


def index3(request):
    #pass list and loops in the template
    return render(request, 'polls/index3.html',{'posts':["kerker","look3","zhow Anan"]})

def imshow(request):
    #pass list and loops in the template
    return render(request, 'polls/imshow.html',{'pic_path':"target_pics/test_baseketball.jpg"})

def imshow2(request,id):
    ######################################################################
    dirPath="/home/stream/pythonApplications/minimum_django/polls/static/"
    ######################################################################
    imgdir="target_pics"
    fileID=glob.glob(dirPath+imgdir+"/*.jpg")
    print "there are "+str(len(fileID)) +" in side target_pics"
    #pass list and loops in the template
    return render(request, 'polls/imshow.html',{'pic_path':fileID[int(id)].replace(dirPath,'')})

#############################################
##############HomeWork times###############
#############################################

############load the FaceDetection model###########
#http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
#http://www.pyimagesearch.com/2015/05/11/creating-a-face-detection-api-with-python-and-opencv-in-just-5-minutes/
cascPath = settings.BASE_DIR+"/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

def imFD(request,id):
    print "[debug]: for imFD"

    # this function will read a image, and face detect , write with retangle
    # thus , render the page with the image with face retangle to web 

    ###you need to change path here#####
    dirPath="/home/stream/pythonApplications/minimum_django/polls/static/"
    ###you need to change path here#####

    imgdir="target_pics/"
    outdir="out_pics/"

    #the file list
    fileID=glob.glob(dirPath+imgdir+"*.jpg")
    if(int(id)>=len(fileID)):
        id=str(0)
    print settings.BASE_DIR
    #read the image
    img = cv2.imread(fileID[int(id)])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    print "found :"+str(len(faces))+"faces"

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #######################################################
        #(A) write your code here add unmber upto the boxes####
        ########################################################
        # font = cv2.FONT_HERSHEY_SIMPLEX 
        # cv2.putText(img,str(add_number),(oo,xx), font,\
        # 1,(255,255,255),2)
        ########################################################


    outfileID=glob.glob(dirPath+outdir+"*.jpg")
    cv2.imwrite(dirPath+outdir+str(len(outfileID))+".jpg", img)

    face_list=[[int(j) for j in i] for i in faces]
    #a string that can be passed to browser
    faceboxes=json.dumps(dict(zip(range(len(faces)),face_list)))
    #print json.dumps()


    return render(request, 'polls/index_FD.html',{'pic_path':outdir+str(len(outfileID))+".jpg",
                "faceboxes":faceboxes,'pic_ori_path':fileID[int(id)],'id':id})
import time

@csrf_exempt
def post_example(request):
    print "[debug]: for post_example"
    # this function used to show post mechanism
    # and is the template of hw
    if request.method == 'POST':
        time.sleep(1)
        # here are some help message
        #print("==========requestBody=================")
        #print(request.body);
        #print("==========request.POST=================")
        #print(request.POST);

        #print("==========request.Hw=================")
        # you should try to uncommand this four data
        #print(request.POST['friend'])
        #print(request.POST['nothuman'])
        #print(request.POST['facebox'])
        #print(request.POST['pic_path'])
        # what you need to do is parse the data and write it to DB
        
        ###############################################################
        # (B) Create table:FaceBoxes !!OUTSIDE(not in this function)!!
        # with col :
        # (image_id(text),friend(bool),human(bool),x(real),y(real),w(real),h(real))
        ###############################################################
        
        ###########################################################
        # (C)
        #1.create list of tuples(length is 7) from :
        #request.POST['friend'],request.POST['nothuman'],request.POST['pic_path']
        #2.inser rows into the Table FaceBoxes you create
        ###################Write your code here####################
        #pushMessages=xxxxxxxxx
        #import sqlite3 #acctually have been import upside
        #con=sqlite.connect('xxxx.sqlite')
        #cursor=con.cursor()
        #cursor.executemany("",pushMessages)
        #con.commit()
        ###########################################################
        
        ###################################################################
        # (D) using cv2.imread to read pic_path again, and saves the region of\
        # face( treat as sub array) to  three directory (yourFriend,notYourFriend,notHuman)
        ################## Write your code Here ###########################
        # path from request.POST['pic_path']
        # img=cv2.imread(path) 
        # for (x,y,w,h) in faceboxes:
        #    subimg=img[oo:xx,oo:xx]
        #    if(friend):
        #        cv2.imwrite("friend/picxx.jpg",subimg)
        #    elif(nothuman):
        #        cv2.imwrite("nothuman/picxx.jpg",subimg)
        #    else:
        #        cv2.imwrite("human/picxx.jpg",subimg)
        ###########################################################
        return HttpResponse(json.dumps({"689":123,"426":92}), content_type='application/json')

