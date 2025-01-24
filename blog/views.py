from django.shortcuts import render

from rest_framework import authentication,permissions

from rest_framework.response import Response

from django.contrib.auth.models import User

# Create your views here.

from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveAPIView

from blog.serializers import UserSerializer,ProfileSerializer

from rest_framework.views import APIView

from blog.models import Profile

class UserCreateView(CreateAPIView):

    serializer_class=UserSerializer


# url:loclhost:8000/api/profile/
# method:put
# data:{}
class ProfileUpdateView(
                        UpdateAPIView,
                        RetrieveAPIView
                        ):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    serializer_class=ProfileSerializer

    def get_object(self):
        
        profile_instance=Profile.objects.get(owner=self.request.user)
        
        return profile_instance
    

class UserDetailView(RetrieveAPIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    serializer_class=UserSerializer

    def get_object(self):
        
        user_instance=User.objects.get(username=self.request.user.username)

        return user_instance
