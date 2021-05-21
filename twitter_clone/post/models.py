from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    def __str__(self):
        return self.text


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(to=Post, related_name='comments', on_delete=models.CASCADE)
    def __str__(self):
        return self.comment

class Profile(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)
    bio = models.TextField()
    #icon = models.ImageField(upload_to='images/')