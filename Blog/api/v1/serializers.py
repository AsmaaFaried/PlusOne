from rest_framework import serializers

from Blog.models import *

def parse_fields(data, m2m_fields):
    data._mutable = True
    for field in data:
        if field in m2m_fields:
            if data.get(field) == 'null' or data.get(field) == '':
                data.setlist(field, [])
            elif data.get(field):
                data.setlist(field, data.get(field).split(','))
        else:
            if data.get(field) == 'null':
                data[field] = None
    data._mutable = False
    return data


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['author'] = instance.author.user.username
        return ret

    def to_internal_value(self, data):
        m2m_fields = ['tags', 'categories']
        data = parse_fields(data, m2m_fields)
        return super().to_internal_value(data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
