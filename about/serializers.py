'''from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField, ValidationError
from users.serializers import UserSerializer
from .models import Page
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

#Page Serializers
class PageCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish'
        ]


page_detail_url = HyperlinkedIdentityField(
        view_name='pages-api:detail',
        lookup_field='slug'
        )


class PageDetailSerializer(ModelSerializer):
    url = page_detail_url
    user = UserSerializer(read_only=True)
    image = SerializerMethodField()
    html = SerializerMethodField()
    class Meta:
        model = Page
        fields = [
            'url',
            'id',
            'user',
            'title',
            'slug',
            'content',
            'html',
            'publish',
            'image',
        ]

    def get_html(self, obj):
        return obj.get_markdown()

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image


class PageListSerializer(ModelSerializer):
    url = page_detail_url
    user = UserSerializer(read_only=True)
    class Meta:
        model = Page
        fields = [
            'url',
            'user',
            'title',
            'content',
            'publish',
        ]
'''