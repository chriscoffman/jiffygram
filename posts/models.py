from django.conf import settings 
from django.db import models 
from django.urls import reverse 
from accounts.models import CustomUser 

class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True) 
    author = models.ForeignKey( 
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    pet_image = models.ImageField(null = True, blank=True, upload_to="images/") 
    pet_name = models.CharField(max_length= 250, null=True, blank=True)
    likes = models.ManyToManyField(CustomUser, related_name='jiffygram_post')

    def total_likes(self):
        return self.likes.count() 
    

    class Meta:
        ordering = ['-date'] 

    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk}) 


class Comment(models.Model): 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140) 
    author = models.ForeignKey( 
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment 

    def get_absolute_url(self): 
        return reverse('post_list') 