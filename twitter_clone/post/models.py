from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
