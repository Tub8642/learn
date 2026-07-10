from rest_framework import serializers
from .models import Project, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProjectSerializers(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'video_url', 'image', 'category', 'slug']