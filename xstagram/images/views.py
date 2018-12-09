from rest_framework.views import APIView
from rest_framework.response import Response
from . import models


class Feed(APIView):

    def get(self, request,  format=None):
        user = request.user
        following_users = user.following.all()

        for following_user in following_users:
            user_images = following_user.images.all()[:2]

        return Response(status=200)
