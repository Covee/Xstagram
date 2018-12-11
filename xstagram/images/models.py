from django.db import models

from django.utils.encoding import python_2_unicode_compatible
from xstagram.users import models as user_models


@python_2_unicode_compatible
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # (below) 이 클래스가 DB에 저장되지 않게끔 abstract 모델이라고 선언해준다.(모듈처럼 다른 클래스에서 확장하여 쓰려고 만든 모델이기 때문)
    class Meta:
        abstract = True 


@python_2_unicode_compatible
class Image(TimeStampedModel):
    file        = models.ImageField()
    location    = models.CharField(max_length=140)
    caption     = models.TextField()
    creator     = models.ForeignKey(
                        user_models.User,
                        null=True, 
                        on_delete=models.PROTECT,
                        related_name='images'
                        )

    @property   # property는 모델의 필드 중 하나임. function임.
    def like_count(self):
        return self.likes.all().count()

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)


@python_2_unicode_compatible
class Comment(TimeStampedModel):
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
    image   = models.ForeignKey(Image, null=True, on_delete=models.PROTECT, related_name='comments')

    def __str__(self):
        return self.message
    

@python_2_unicode_compatible
class Like(TimeStampedModel):
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
    image   = models.ForeignKey(Image, null=True, on_delete=models.PROTECT, related_name='likes')

    def __str__(self):
        return 'User: {} - Image Caption: {}'.format(self.creator.username, self.image.caption)

    