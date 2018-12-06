from rest_framework import serializers
from . import models


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = '__all__'  # model의 모든 속성을 필드값으로 가져오겠다는 뜻임.


class CommentSerializer(serializers.ModelSerializer):
    
    # 이렇게 하면 원래 image의 ForeignKey인 숫자 대신에 ImageSerializer 전체를 불러옴.
    # 다시 말해서 object 안에 또 다른 object를 불러 올 수 있는 것임.
    image = ImageSerializer()

    class Meta:
        model = models.Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    
    image = ImageSerializer()

    class Meta:
        model = models.Like
        fields = '__all__'
        