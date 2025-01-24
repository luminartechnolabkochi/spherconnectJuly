from django.db import models


# User
# user=>Profile 
    #owner=>OneToOne(User)
    #bio
    # address
    # phone
    # picture
    # gender

from django.contrib.auth.models import User

class Profile(models.Model):

    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="userprofile")

    adress=models.TextField(null=True)

    phone=models.CharField(max_length=15,null=True)

    GENDER_CHOICES=(
        ("male","male"),
        ("female","female")
    )

    gender=models.CharField(max_length=20,choices=GENDER_CHOICES,default="male")

    picture=models.ImageField(upload_to="profilepics",null=True,blank=True,default="profilepics/default.png")

    bio=models.CharField(max_length=100,null=True)

# user object create => Profile

# signals => post_save(),pre_save(),pre_init(),post_init(),pre_delete(),post_delete()
# Profile.objects.create(owner)

# instance=user_object
# created=boolean True,False

def create_profile(sender,instance,created,**kwargs):

    if created:

        Profile.objects.create(owner=instance)


from django.db.models.signals import post_save

post_save.connect(create_profile,User)



class Post(models.Model):

    caption=models.CharField(max_length=200)

    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="blogs")
    
    picture=models.ImageField(upload_to="postpictures",null=True,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)

    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return self.caption




   








