from rest_framework import serializers
from .import models

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = '__all__'


class RecipeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.recipe
        fields = '__all__'


class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.rating
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.comment
        fields = '__all__'

        
