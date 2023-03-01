from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path
from grace import views

app_name = 'grace'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home_view,name='home'),
    path('about/',views.About.as_view(),name='about'),
    path('gallery/',views.Gallery.as_view(),name='gallery'),
    path('charity/',views.Donation.as_view(),name='charity'),
    path('sermon/',views.Sermon.as_view(),name='sermon'),
    path('donate/',views.Donate_view,name='donate'),
    path('track/',views.Track.as_view(),name='track'),
    path('policy/',views.Policy.as_view(),name='policy'),
    path('calendar/',views.Calendar.as_view(),name='calendar'),
    path('contact/', views.contact_view, name='contact'),
    path('event/',views.Events.as_view(),name='event'),
    path('event_gallery/',views.Event_gallery.as_view(),name='event_gallery'),
    path('mission/',views.Mission.as_view(),name='mission'),
    path('live/',views.Live.as_view(),name='live'),
    path('pastors/',views.Pastor.as_view(),name='pastors'),
    path('community/',views.Community.as_view(),name='community'),
    path('podcast',views.PodcastAPIView.as_view(), name="upload-podcast"),
]
