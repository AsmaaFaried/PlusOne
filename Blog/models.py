from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.translation import gettext_lazy as _
import os
import uuid


def _get_image_name(instance, filename):
    """Generate Image File Path"""
    file_extension = filename.split('.')[1]
    filename = f'{uuid.uuid4()}.{file_extension}'
    file_path = os.path.join('user/profile/', filename)
    return file_path


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    bio = models.CharField(verbose_name=_("Bio"), max_length=255, null=True, blank=True)
    profile_pic = models.ImageField(upload_to=_get_image_name, null=True, blank=True, verbose_name=_('Profile Picture'))


    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        ordering = ('id',)

    def __str__(self):
        return self.user.username


class Tag(models.Model):

    name = models.CharField(verbose_name=_("name"), max_length=255)
    slug = models.SlugField(null=True, blank=True, max_length=255,
                                   verbose_name=_('Slug'))

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        ordering = ('id',)

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(verbose_name=_("name"), max_length=255)
    slug = models.SlugField(null=True, blank=True, max_length=255,
                                   verbose_name=_('Slug'))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ('id',)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField(Category, verbose_name=_('Categories'))
    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ('id',)

    def __str__(self):
        return self.title


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ('id',)

    def __str__(self):
        return self.content