from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # (below) 이 클래스가 DB에 저장되지 않게끔 abstract 모델이라고 선언해준다.(모듈처럼 다른 클래스에서 확장하여 쓰려고 만든 모델이기 때문)
    class Meta:
        abstract = True 


class Image(TimeStampedModel):
    file        = models.ImageField()
    location    = models.CharField(max_length=140)
    caption     = models.TextField()


class Comment(TimeStampedModel):
    message = models.TextField()

