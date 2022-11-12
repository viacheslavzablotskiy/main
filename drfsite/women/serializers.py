import io

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women, Comment, Like, Category


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # comment = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Women
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        fields = '__all__'
    # title = serializers.CharField(max_length=255)
    # content = serializers.CharField()
    # time_create = serializers.DateTimeField(read_only=True)
    # time_update = serializers.DateTimeField(read_only=True)
    # is_published = serializers.BooleanField(default=True)
    # cat_id = serializers.IntegerField()
    #
    # def create(self, validated_data):
    #     return Women.objects.create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.time_create = validated_data.get('time_create', instance.time_create)
    #     instance.time_update = validated_data.get('time_update', instance.time_uodate)
    #     instance.cat_id = validated_data.get('cat_id', instance.cat_id)
    #     instance.save()
    #     return instance

# def encode():
#     model = WomenModel('Компьютеры', 'Content: Но ничего себе это  получилось')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"rgjtoirtjgirtj", "content": "kgrigtjritjhio"}')
#     data = JSONParser().parse(stream)
#     serializers = WomenSerializer(data=data)
#     serializers.is_valid()
#     print(serializers.validated_data)


# class UserSerializer(serializers.ModelSerializer):
#     posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#
#     class Meta:
#         model = User
#         fields = '__all__'



# class UserSerializer(serializers.ModelSerializer):
#     posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#
#     class Meta:
#         model = User
#         fields = '__all__'
