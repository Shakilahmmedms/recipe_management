from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)


class recipe(models.Model):
    title = models.CharField(max_length=150)
    chef = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


class rating(models.Model):
    rating = models.IntegerField()
    recipe = models.ForeignKey(recipe, on_delete=models.CASCADE)

class comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField()
    recipe = models.ForeignKey(recipe, on_delete=models.CASCADE)

