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

    # def create(self, validated_data):
    #     new_tag = validated_data.pop('tags')
    #     tag_id = new_tag.get('id', None)
    #     tag = new_tag.get('tag', None)
    #     mini_set = new_tag.get('mini_set', None)

    #     if not tag:
    #         raise serializers.ValidationError('no tag found')

    #     tag_obj = Tags.objects.get_or_create(tag=tag,mini_set=mini_set)
    #     validated_data.update({"new_tag":tag_obj})
