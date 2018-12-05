from django.urls import path

from .views import (
    ListAllImages,
    ListAllComments,
    ListAllLikes,

)

app_name = "images"
urlpatterns = [
    path("all/", view=ListAllImages.as_view(), name="all_images"),
    path("comments/", view=ListAllComments.as_view(), name="all_comments"),
    path("likes/", view=ListAllLikes.as_view(), name="all_likes"),
]
