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
    path('',views.Home.as_view(),name='home'),
    path('about/',views.About.as_view(),name='about'),
    path('gallery/',views.Gallery.as_view(),name='gallery'),
    path('blog/',views.Blog.as_view(),name='blog'),
    path('courses/',views.Courses.as_view(),name='courses'),
    path('sermon/',views.Sermon.as_view(),name='sermon'),
    path('preschool/',views.Preschool.as_view(),name='preschool'),
    path('mess/',views.Mess.as_view(),name='mess'),
    path('secondary/',views.Secondary.as_view(),name='secondary'),
    path('boarding/',views.Boarding.as_view(),name='boarding'),
    path('admission/',views.Admission.as_view(),name='admission'),
    # path('bod/',views.Bod.as_view(),name='bod'),
    path('policy/',views.Policy.as_view(),name='policy'),
    #path('calendar/',views.Calendar.as_view(),name='calendar'),
    path('contact/', views.contact_view, name='contact'),
    #path('arts/',views.Arts.as_view(),name='arts'),
    path('music/',views.Music.as_view(),name='music'),
    path('language/',views.Languge.as_view(),name='language'),
    path('sports/',views.Sports.as_view(),name='sports'),
    path('experiment/',views.Eperiment.as_view(),name='experiment'),
    path('swimming/',views.Swimming.as_view(),name='swimming'),
]
