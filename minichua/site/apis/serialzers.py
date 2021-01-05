from rest_framework import serializers
from minichua import models

class TagsSerializer(serializers.ModelSerializer):
    # tags = serializers.ListField(allow_empty=True)
    class Meta:
        fields = (
            'tags',
        )
        model = models.Tags

class MiniSerializer(serializers.ModelSerializer):
    # tags = serializers.ListField(allow_empty=True)
    class Meta:
        fields = (
            'id',
            'name',
            'image_url',
            'tags',
        )
        model = models.Mini

