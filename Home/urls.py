from django.contrib import admin
from django.urls import path
from Home import views


urlpatterns = [
    path("", views.home),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("faq", views.faq, name="faq"),
    path("study_materials/", views.academics_sm, name="study_materials"),
    path("video_recordings", views.academics_vr, name="video_recordings"),
    path("home", views.home, name="home"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("signup", views.signup_user, name="signup"),
    # path("your_name", views.get_name, name="your_name")
]
