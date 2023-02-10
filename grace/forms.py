# Developed by Surfa
from django import forms
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Contact



# class ImageForm(forms.ModelForm):
#     """Form for the image model"""
#     class Meta:
#         model = Galary
#         fields = ('title', 'image2')





class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('name','email','message')
    
    Widgets  = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'message': forms.TextInput(attrs={'class': 'form-control'}),
    }