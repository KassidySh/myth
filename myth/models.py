from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Region(models.Model):
    genre =  models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    intro = models.TextField()
    image = models.TextField(blank=True)
    
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
    associated_city = models.TextField(blank=True)
    favorite_god = models.ManyToManyField(User, related_name='favorite_god', blank=True)
    
    def __str__(self):
        return self.title
    
class Relation(models.Model):
    god1 = models.ForeignKey(Being, on_delete=models.CASCADE, related_name='god1')
    god2 = models.ForeignKey(Being, on_delete=models.CASCADE, related_name='god2')
    detail = models.CharField(max_length=100)
    detail2= models.CharField(max_length=100)
    
    def __str__(self):
        return self.god1.title
    
class God_Of(models.Model):
    god = models.ForeignKey(Being, on_delete=models.CASCADE, related_name='god')
    item = models.CharField(max_length=200)
    
    def __str__(self):
        return self.item
    
class Author(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    image = models.TextField()
    
    def __str__(self):
        return self.author
    
class Story(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='writer')
    god= models.ForeignKey(Being, on_delete=models.CASCADE, related_name='person', default=1)
    title=models.CharField(max_length=500)
    content=models.TextField()
    favorite_story = models.ManyToManyField(User, related_name='favorite_story', blank=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='wrtten_by')
    story= models.ForeignKey(Story, on_delete=models.CASCADE, related_name='related_story')
    comment=models.TextField()


class FaveGod(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='person', blank=True)
    god= models.ForeignKey(Being, on_delete=models.CASCADE, related_name='being', blank=True)
    
class FaveStory(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='loggedon', blank=True)
    story= models.ForeignKey(Story, on_delete=models.CASCADE, related_name='story', blank=True)
