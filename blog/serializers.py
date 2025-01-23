

from django.contrib.auth.models import User

from rest_framework import serializers

from blog.models import Profile

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=["id","username","email","password"]

    def create(self, validated_data):
        
        return User.objects.create_user(**validated_data)



class ProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model=Profile

        fields="__all__"

        read_only_fields=["id","owner"]