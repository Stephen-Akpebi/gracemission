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
from .models import Contact, Charity



# class ImageForm(forms.ModelForm):
#     """Form for the image model"""
#     class Meta:
#         model = Galary
#         fields = ('title', 'image2')
class CharityForm(forms.ModelForm):
    
    class Meta:
        model = Charity
        fields = ('name','phone','email','amount')
    
    Widgets  = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'phone': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'amount': forms.TextInput(attrs={'class': 'form-control'}),
    }


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('name','email','message')
    
    Widgets  = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'message': forms.TextInput(attrs={'class': 'form-control'}),
    }