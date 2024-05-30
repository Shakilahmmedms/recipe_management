from django.shortcuts import render
from .import serializers
from .import models
from rest_framework import viewsets
# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializers


class RecipeViewset(viewsets.ModelViewSet):
    queryset = models.recipe.objects.all()
    serializer_class = serializers.RecipeSerializers


class RattingViewset(viewsets.ModelViewSet):
    queryset = models.rating.objects.all()
    serializer_class = serializers.RatingSerializers

class CommentsViewsets(viewsets.ModelViewSet):
    queryset = models.rating.objects.all()
    serializer_class = serializers.CommentSerializers
