from django.contrib import admin
from .models import *
from django.utils.html import format_html


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_categories', 'get_tags', 'created_at', 'updated_at')
    search_fields = ('title', 'content',)
    list_filter = ('categories', 'tags',)

    def get_categories(self, obj):
        return ",".join([category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories'

    def get_tags(self, obj):
        return ",".join([tag.name for tag in obj.tags.all()])

    get_tags.short_description = 'Tags'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_at')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'get_profile_pic')

    def has_delete_permission(self, request, obj=None):
        return False
    def get_profile_pic(self, obj):
        if obj.profile_pic:
            return format_html(f'<a href="{obj.profile_pic.url}" target="_blank">'
                         f'<img src="{obj.profile_pic.url}" width="150" height="150"/>'
                         f'</a>')
        return '---'

    get_profile_pic.short_description = 'Profile Picture'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

