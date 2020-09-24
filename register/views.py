from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import response
# Create your views here.
def register(responce):
    if response.method == "POST":
	    form = UserCreationForm(response.POST)
	    if form.is_valid():
	        form.save()

	    return redirect("/home")
    else:
	    form = UserCreationForm()
    return render(responce, 'register/register.html',{'form':form})