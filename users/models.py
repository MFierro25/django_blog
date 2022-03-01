from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile-pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    #making own save method to be able to resize img
    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
        
        if img.height > 250 or img.width > 2500:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)