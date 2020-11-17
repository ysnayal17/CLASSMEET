from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.home),
    path("contact", views.contact),
    path("about", views.about),
    path("faq", views.faq),
    path("study_materials", views.academics_sm),
    path("video_recordings", views.academics_vr),
    path("questions", views.academics_q),
    path("answers", views.academics_a)
]
