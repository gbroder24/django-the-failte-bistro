from django.test import TestCase
from .forms import CommentForm

# Create your tests here.

class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        """
        Test validation for content field
        """
        comment_form = CommentForm({'content': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')


    def test_form_is_invalid(self):
        """
        Test validation for empty content field
        """
        comment_form = CommentForm({'content': ''})
        self.assertFalse(comment_form.is_valid(), msg='Form is valid')
