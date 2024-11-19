from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Dish, Comment

class TestMenuViews(TestCase):

    def setUp(self):
        """
        Set up data for self user, dish and comment
        """
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.dish = Dish(dish_title="Dish title", slug="dish-title",
                         author=self.user, content="Dish content",
                         status=1, excerpt="Dish excerpt")
        self.dish.save()

        self.comment = Comment(post=self.dish, author=self.user,
                               approved=True)
        self.comment.save()


    def test_render_menu_detail_page_with_comment_form(self):
        """
        Test valdation for render of menu detail 
        page with comment form
        """
        response = self.client.get(reverse(
            'menu_detail', args=['dish-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Dish title", response.content)
        self.assertIn(b"Dish content", response.content)
        self.assertEqual(response.context['comment_count'], 1)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)


    def test_dish_no_hearts(self):
        """
        Test valdation for no hearts
        """
        self.assertEqual(self.dish.hearts.count(), 0)


    def test_dish_hearts(self):
        """
        Test valdation to add hearts
        """
        self.dish.hearts.add(self.user)
        self.assertEqual(self.dish.hearts.count(), 1)


    def test_comment_no_likes(self):
        """
        Test valdation for no likes
        """
        self.assertEqual(self.comment.likes.count(), 0)


    def test_comment_likes(self):
        """
        Test valdation to add likes
        """
        self.comment.likes.add(self.user)
        self.assertEqual(self.comment.likes.count(), 1)


    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'content': 'This is a test comment.'
        }
        response = self.client.post(reverse(
            'menu_detail', args=['dish-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )