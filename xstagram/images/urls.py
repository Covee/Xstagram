from django.urls import path

from .views import (
    ListAllImages,

)

app_name = "images"
urlpatterns = [
    path("all/", view=ListAllImages.as_view(), name="all_images"),
]
