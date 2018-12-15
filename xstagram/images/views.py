from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models

from . import serializers


class Feed(APIView):

    def get(self, request,  format=None):
        user = request.user
        following_users = user.following.all()
        image_list = []

        for following_user in following_users:
            user_images = following_user.images.all()[:2]
            for image in user_images:
                image_list.append(image)

    # sorted()함수는 3개의 param을 가지는데, 첫번째는 어떤 리스트를 sort 할 것인가? 두번째는 기준(key), 세번째는 방식(ex.reverse)
        sorted_list = sorted(image_list, key=lambda image: image.created_at, reverse=True)

        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)

# lambda를 써서 간단한 get_key 함수를 대체할 수 있다.
# def get_key(image):
#     return image.created_at


class LikeImage(APIView):
    def get(self, request, image_id, format=None):
        user = request.user

        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexistinig_like = models.Like.objects.get(
                creator = user,
                image = found_image
            )
            preexistinig_like.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Like.DoesNotExist:
            new_like = models.Like.objects.create(
                creator = user,
                image = found_image
            )
            new_like.save()

            return Response(status=status.HTTP_201_CREATED)

    
class CommentOnImage(APIView):
    def post(self, request, image_id, format=None):
        user = request.user

        try:
            found_imgae = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(creator=user, image=found_image)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
