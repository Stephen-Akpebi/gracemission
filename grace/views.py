from django.shortcuts import render
from django.views import generic
from telnetlib import GA
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views import generic
from .models import Gallery, PodcastSerializer, Sermon , Event , Gallery2, Charity , Pastors, Event_Gallery
from .forms import ContactForm, CharityForm
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from .convert_audio_file import convert_to_mp3
from rest_framework.generics import (UpdateAPIView)
from rest_framework.response import Response
from rest_framework import status
from .models import Podcasts
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser


# Create your views here.

# class Home(generic.ListView):
#     queryset = Charity.objects.all()
#     template_name = 'grace/index.html'


class Sermonn(generic.TemplateView):
    
    template_name = 'grace/m-index.html'



class Give(generic.TemplateView):
    template_name = 'grace/give.html'


class Sermon(generic.ListView):
    queryset = Sermon.objects.all()
    template_name = 'grace/sermon.html'

class Policy(generic.TemplateView):
    template_name = 'novel/policy.html'

class Live(generic.TemplateView):
    #queryset = Gallery.objects.all()
    template_name = 'grace/live.html'



# class Bod(generic.ListView):
#     queryset = Bod.objects.all()
#     template_name = 'novel/team.html'

class Community(generic.TemplateView):
    template_name = 'grace/community.html'

class Gallery(generic.ListView):
    queryset = Gallery.objects.all()
    template_name = 'grace/gallery.html'


class Events(generic.ListView):
    queryset = Event.objects.all()
    template_name = 'grace/events.html'


class Calendar(generic.TemplateView):
    template_name = 'grace/calendar.html'


class Event_gallery(generic.ListView):
    queryset = Event_Gallery.objects.all()
    template_name = 'grace/gallery2.html'


class Pastor(generic.ListView):
    queryset = Pastors.objects.all()
    template_name = 'grace/team.html'


class Mission(generic.TemplateView):
    template_name = 'grace/mission.html'


class Donation(generic.TemplateView):
    template_name = 'grace/donation.html'

class Track(generic.ListView):
    queryset = Podcasts.objects.all()
    template_name  = 'grace/podcast.html'



class PodcastAPIView(UpdateAPIView):
    serializer_class = PodcastSerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = [MultiPartParser, ]
    queryset = Podcasts.objects.all()
    lookup_field = 'id'
    
    def put(self, request, *args, **kwargs):
            file_obj = request.data
            temp_audio_file = request.FILES.get('file')

            # Using our custom convert_to_mp3 function to obtain converted file
            converted_temp_audio_file = convert_to_mp3(temp_audio_file)

            # Adding this file to the serializer
            file_obj['file'] = converted_temp_audio_file
            serializer = PodcastSerializer(data=file_obj)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Actual place where we save it to the MEDIA_ROOT (cloud or other)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
#class Blog(DetailView):
    #queryset = Post.objects.filter(status=1).order_by('-created_on')
    #def get_queryset(self):
        #return super().get_queryset()
    
    #template_name = 'blog.html'


#class BlogDetail(DetailView):
    #template_name = 'blog-details.html'


class About(generic.TemplateView):
    template_name = 'grace/about.html'
    


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact request submitted successfully.')
            return render(request, 'grace/contact.html', {'form': ContactForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    form = ContactForm()
    context = {'form': form}
    return render(request, 'grace/contact.html', context)

def Home_view(request):
    if request.method == 'POST':
        form = CharityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Donation request submitted successfully.')
            return render(request, 'grace/index.html', {'form': CharityForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    form = CharityForm()
    context = {'form': form}
    return render(request, 'grace/index.html', context)


def Donate_view(request):
    if request.method == 'POST':
        form = CharityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Donation request submitted successfully.')
            return render(request, 'grace/donate.html', {'form': CharityForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    form = CharityForm()
    context = {'form': form}
    return render(request, 'grace/donate.html', context)

# def Audio_store(request):
#     if request.method == 'POST':
#         form = AudioForm(request.POST,request.FILES or None)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Audio  uploaded successfully.')
#             return render(request, 'grace/sermon.html', {'form': ContactForm(request.GET)})
#         else:
#             messages.error(request, 'Invalid form submission.')
#             messages.error(request, form.errors)
#     form = ContactForm()
#     context = {'form': form}
#     return render(request, 'grace/sermon.html', context)

