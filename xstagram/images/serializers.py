from rest_framework import serializers
from . import models


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = '__all__'  # model의 모든 속성을 필드값으로 가져오겠다는 뜻임.


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Like
        fields = '__all__'
        