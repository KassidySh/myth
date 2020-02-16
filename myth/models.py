from django.db import models

# Create your models here.
class Region(models.Model):
    genre =  models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    intro = models.TextField()
    
    def __str__(self):
        return self.genre

class Type(models.Model):
    genre = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='types')
    title = models.CharField(max_length=100)
    img = models.TextField()
    info = models.TextField()
    
    def __str__(self):
        return self.title
    
class Being(models.Model):
    genre = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='beings')
    myth_type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='myth_types')
    title = models.CharField(max_length=500)
    image = models.TextField()
    origin=models.TextField()
    associated_city = models.TextField()
    
    
    def __str__(self):
        return self.title
    
