from django.shortcuts import render

from rest_framework import authentication,permissions

from rest_framework.response import Response

from django.contrib.auth.models import User

# Create your views here.

from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView

from blog.serializers import UserSerializer,ProfileSerializer,PostSerializer

from rest_framework.views import APIView

from blog.models import Profile,Post

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


class PostListCreateView(ListCreateAPIView):

    queryset=Post.objects.all()

    serializer_class=PostSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        
        serializer.save(owner=self.request.user)



class PostRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    serializer_class=PostSerializer

    queryset=Post.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]





    




    

