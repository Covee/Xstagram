from django.contrib import admin
from . import models


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    search_fields = [   # admin에 관련 필드를 검색할 수 있는 검색창 생성
        'file',
        'creator',
    ]

    list_filter = [     # admin 오른쪽에 filter 창이 생김. 여기선 location별로 필터 할 수 있게 된다.
        'location'
    ]

    list_display_links = [   # list_display 항목 중에서 여기 선택된 필드는 링크가 생겨 바로 수정창으로 가게 된다.
        'location',
    ]

    list_display = [
        'file',
        'location',
        'caption',
        'creator',
        'created_at',
        'updated_at',  
    ]


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = [
        'creator',
        'image',
        'created_at',
        'updated_at',
    ]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'message',
        'creator',
        'image',
        'created_at',
        'updated_at',
    ]
