from rest_framework import serializers
from minichua import models

class MinichuaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'image_url',
            'tags',
        )
        model = models.Minichua