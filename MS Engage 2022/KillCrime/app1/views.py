 #importing modules
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from numpy import meshgrid
from .models import *
import face_recognition
import cv2
import urllib.request
import math
from django.contrib import messages



#  findings face_encodings of all images in database and their respective crim_id
encodings = []

def findEncodings():
    criminals = Criminal.objects.all()
    for criminal in criminals:
        imagePath = f'media/{criminal.image}'
        image = face_recognition.load_image_file(imagePath)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        imageEncod = face_recognition.face_encodings(image)[0]
        encodings.append([imageEncod,criminal.crim_id])

findEncodings()         # calling findEcnodings function


# home page
def Home(request):
    try:
        #  getting criminals data
        criminals = Criminal.objects.all()
        wantedByIndia = Criminal.objects.filter(wantedInCountry="India")
        wantedByIndia = wantedByIndia[:12]
        wantedByFBI = Criminal.objects.filter(wantedInCountry="FBI")
        wantedByFBI = wantedByFBI[:12]

        # checking request method 
        if(request.method=='GET'):        
            return render(request, "app.html",{'wantedByIndia':wantedByIndia,'wantedByFBI':wantedByFBI})

        elif(request.method=='POST'):

            # fetching image data from front end
            imageURL = request.POST["imageURL"]
            imageURL = urllib.request.urlopen(request.POST["imageURL"])
            image = face_recognition.load_image_file(imageURL)
            image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            imgEod = face_recognition.face_encodings(image)[0]

            # finding face in the database which has minimum face distance 
            minFaceDis = math.inf
            minFaceDisId=-1
            for encoding in encodings:
                faceDis = face_recognition.face_distance([encoding[0]],imgEod)
                if(faceDis<minFaceDis):
                    minFaceDis=faceDis;
                    minFaceDisId=encoding[1]
            return redirect(f'viewCriminal/{minFaceDisId}')

    except:
        return render(request,"error.html")


# viewing a particular criminal

def viewCriminal(request,crim_id):
    try:
        criminal = Criminal.objects.filter(crim_id = crim_id)       # getting criminal data by 'id'
        return render(request,'viewCriminal.html',{'criminal':criminal[0]})
    except:
        return render(request,"error.html")




# deleting a particular criminal
def deleteCriminal(request,crim_id):
    try:
        if request.method =='POST':
            criminal = Criminal.objects.get(crim_id = crim_id)
            criminal.delete()
            messages.warning(request,"Deleted successfully")
            return redirect('/')
    except:
        return render(request,"error.html")



#  editing a particular criminal data
def edit(request,crim_id):

        criminal = Criminal.objects.get(crim_id=crim_id)
        if request.method =='GET':
            return render(request,'edit.html',{'criminal':criminal})
        if request.method=='POST':
            name = request.POST['name']
            age = request.POST['age']
            nationality = request.POST['nationality']
            gender = request.POST['gender']
            weight = request.POST['weight']
            height = request.POST['height']
            wantedInCountry=request.POST['wantedBy']
            charges = request.POST['charges']
            about = request.POST['about']

            criminal.name = name
            criminal.age = age
            criminal.nationality  = nationality 
            criminal.gender = gender
            criminal.weight =weight
            criminal.height = height
            criminal.wantedInCountry = wantedInCountry
            criminal.charges = charges
            criminal.about = about

            criminal.save()
            messages.warning(request,"Edited successfully")
            return redirect(f'/viewCriminal/{criminal.crim_id}')




# Viewing all criminals at one page
def allCriminals(request):
    try:
        criminals = Criminal.objects.all()
        return render(request,'allCriminals.html',{'criminals':criminals})
    except:
        return render(request,"error.html")



# signup page      
def signup(request):
    try:
        if request.method=='GET':
            return render (request,"signup.html")

        if request.method=='POST':
            # fetching user data from fron end
            username=request.POST['username']
            firstName=request.POST['firstName']
            lastName=request.POST['lastName']
            email=request.POST['email']
            password=request.POST['password']
            confrimPassword=request.POST['confrimPassword']

            # confriming password
            if (password!=confrimPassword):
                messages.warning(request,"passwords are not same")
                return redirect('/')
            
            # Create the user
            user = User.objects.create_user(username, email, password)
            user.firstName= firstName
            user.lastName= lastName
            user.save()
            messages.warning(request,"Account has been created successfully")
            return redirect('/')
    except:
        return render(request,"error.html")



# About us
def about(request):
    return render(request,"about.html")



# login page
def handleLogin(request):
    try:
        if request.method=='GET':
            return render (request,"login.html")
        if request.method=="POST":
            # Get the post parameters
            username=request.POST['username']
            password=request.POST['password']

            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                messages.warning(request,"Logged in successfully")
                return redirect('/')
    except:
        return render(request,"error.html")


#logout page
def handleLogout(request):
    try:
        logout(request)
        messages.warning(request,"logged out successfully")
        return redirect('/')
    except:
        return render(request,"error.html")


# other urls which is not defined
def notFound(request,slug):
    return render(request,"error.html")
