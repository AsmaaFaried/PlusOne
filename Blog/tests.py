from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.authtoken.models import Token


class PostTest(APITestCase):
    def setUp(self):
        # Add user and profile for test #
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(user=self.user)
        # Login user#
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        # Add tags and cateogires#
        self.tag1 = Tag.objects.create(name='Tag1')
        self.tag2 = Tag.objects.create(name='Tag2')
        self.tag3 = Tag.objects.create(name='Tag3')
        self.category1 = Category.objects.create(name='Categ1')
        self.category2 = Category.objects.create(name='Categ2')
        self.category3 = Category.objects.create(name='Categ3')

    def test_can_create_post(self):
        print("=============Add Post=============")
        data = {
            'title': 'Test Post',
            'content': 'The body of the test post.',
            'tags': [self.tag1.id, self.tag2.id],
            'categories': [self.category1.id, self.category3.id]
        }
        url = reverse('blog:post-list-create')
        response = self.client.post(url, data, format='multipart') # used (multipart) cause the request handle to take form data not json object
        print("Response ===> ",response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_update_post(self):
        print("==========Update Post==========")
        post = Post.objects.create(
        title='Test Post in update', content='The body of the test post to update.', author=self.profile)
        post.tags.set([self.tag1, self.tag3])
        post.categories.set([self.category1, self.category3, self.category2])
        url = reverse('blog:post-get-update-delete', kwargs={'pk': post.id})
        data = {
            'title': 'Updated Test Post',
            'content': 'The body of the updated test post.',
            'tags': [self.tag1.id, self.tag2.id],
            'categories': [self.category1.id],
         }
        response = self.client.put(url, data, format='multipart')# used (multipart) cause the request handle to take form data not json object
        print("Response ===> ", response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_create_comment(self):
        print("=============Add Comment=============")
        post = Post.objects.create(
            title='Test Post in update',
            content='The body of the test post to update.')
        post.tags.set([self.tag1, self.tag3])
        post.categories.set([self.category1, self.category3, self.category2])
        data = {
            'post': post.id,
            'content': 'The body of the test post.',
        }
        url = reverse('blog:comment-list-create')
        response = self.client.post(url, data, format='multipart') # used (multipart) cause the request handle to take form data not json object
        print("Response ===> ", response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)