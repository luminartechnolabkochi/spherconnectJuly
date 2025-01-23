
from django.urls import path

from blog import views

from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns=[

    path("signup/",views.UserCreateView.as_view()),

    path("token/",ObtainAuthToken.as_view()),

    path("profile/",views.ProfileUpdateView.as_view()),
    
    
]