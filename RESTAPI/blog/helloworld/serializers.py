# This file translate the django in native language (JSON).
# It can also be considered as bridge between your database model and JSON/API data

from rest_framework import serializers
from helloworld.models import Post

class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.username", read_only=True)
    class Meta:
        model = Post
        fields = ('__all__')
        read_only_fields = ('created_by',)

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return Post.objects.create(**validated_data)
