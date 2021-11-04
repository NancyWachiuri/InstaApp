from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='profile_pics')


class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE,related_name='author')
    image = models.ImageField(blank = True,null=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default= timezone.now)
    updated = models.DateTimeField(auto_now= True)
    liked = models.ManyToManyField(User, default=None,blank= True,related_name='liked')

    def __str__(self):
        return f'{self.author.username}'

    @property
    def num_likes(self):
        return self.liked.all().count

    @classmethod
    def search_category(cls,search):
        searches = cls.objects.filter(author__username__icontains = search)
        return searches