

from django.contrib.auth.models import User

from rest_framework import serializers

from blog.models import Profile,Post

from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):

    profile=serializers.SerializerMethodField(read_only=True)    
   
    # serializerMethodField
    class Meta:

        model=User

        fields=["id","username","email","password","profile"]

    def create(self, validated_data):
        
        return User.objects.create_user(**validated_data)
    
    def get_profile(self,obj):

        profile_instance=Profile.objects.get(owner=obj)

        serializer_instance=ProfileSerializer(profile_instance)

        return serializer_instance.data
   



class ProfileSerializer(serializers.ModelSerializer):

    owner=serializers.StringRelatedField(read_only=True)

    greetings=serializers.SerializerMethodField(read_only=True)

    class Meta:

        model=Profile

        fields="__all__"

        read_only_fields=["id","owner"]
    
    def get_greetings(self,obj):

        return "Good afternoon"


class PostSerializer(serializers.ModelSerializer):

    owner=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Post
        
        fields="__all__"
        
        read_only_fields=["id","owner","created_at","updated_at"]

