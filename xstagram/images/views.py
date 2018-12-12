from rest_framework.views import APIView
from rest_framework.response import Response
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
        print(image_id)
        return Response(status=200)

    
