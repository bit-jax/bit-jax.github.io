from rest_framework import serializers
from minichua import models

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'tag',
            'mini_set',
        )
        model = models.Tags

class MiniSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'image_url',
            'tags',
            'url',
        )
        model = models.Mini

