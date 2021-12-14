from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Card
from django.views import generic
from django.shortcuts import redirect, render
from django.utils import timezone

import os
import uuid
import tensorflow as tf
import numpy as np
from django.core.files.storage import default_storage
from keras.preprocessing.image import load_img
from pathlib import Path
import openai

# import trained model from a h5 file
CURR_DIR = Path(__file__).resolve().parent
address = os.path.join(CURR_DIR,"model.h5")
model = tf.keras.models.load_model(address)


#this function allows access to openai gpt-3, with the given inputs the machine outputs a cool color HEX code 
def getcolor(color,mood):
    openai.api_key = "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"
    str = "The CSS code for a "+color+" and "+mood+" mood:\n\nbackground-color: #"
    print(str)
    response = openai.Completion.create(
        engine="davinci",
        prompt=str,
        temperature=0.25,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=[";"]
    )
    print(response.choices[0]["text"])
    return response.choices[0].text


def splash(request):
    return render(request,"splash.html",{})

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/cards")
    return render(request, 'login.html', {})

class Page(generic.ListView):
    template_name = 'cards.html'
    context_object_name = 'cards'
    #display mood cards in reverse chronological order
    def get_queryset(self):
        return Card.objects.filter(time__lte=timezone.now()).order_by('-time')


def create_card(request):
    if request.method == 'POST': 
        #load image
        file = request.FILES['imageFile']
        file_name = default_storage.save(file.name,file)
        file_url = default_storage.path(file_name)
        #prepare image for prediction
        image = load_img(file_url,target_size=(48,48),color_mode = "grayscale")
        img =np.array(image)
        img = np.expand_dims(img,axis = 0)
        img = img.reshape(1,48,48,1)
        result = model.predict(img)
        result = list(result[0])
        img_index = result.index(max(result))
        label_dict = {0:'angry',1:'disgusted',2:'fearful',3:'happy',4:'neutral',5:'sad',6:'surprised'}
        #save the predicted result to variable mood
        mood = label_dict[img_index]
        body,color = request.POST['body'],request.POST['color']
        #pass thhe user chosen color to our openai color generator
        spcolor = getcolor(color,mood)
        #create object
        id = uuid.uuid4()
        Card.objects.create(body=body,color = color,author = request.user,mood=mood,spcolor=spcolor,id=id)
        default_storage.delete(file_name)
        return redirect("/cards")
    return render(request, 'cardnew.html',{})

def signup_(request):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST['username'],
                        email=request.POST['email'],
                        password=request.POST['password'])
        login(request, user)
        return redirect('/cards')
    elif request.method == "GET":
        return render(request, 'signup.html', {})

def logout_(request):
    logout(request)
    return redirect("/") 
