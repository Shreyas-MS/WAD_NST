from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [

    # Auth
    path("login/", views.loginuser, name="loginuser"),
    path("logout/", views.logoutuser, name="logoutuser"),
    path("signup/", views.signupuser, name="signupuser"),


    # Features 
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("profile/", views.profile, name="profile"),
    path("gallery/", views.gallery, name="gallery"),
    path("upload/", views.upload, name="upload"),
    path('feedback/',views.feedback,name = 'feedback'),
    path('profileupdate/',views.profileUpdate,name = 'profileUpdate'),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)