from django.test import TestCase
from accounts.forms import UserRegisterForm, CommentForm


class TestForms(TestCase):

    def test_user_form_valid(self):
        form = UserRegisterForm(data={
            'username': 'Leon123',
            'email': 'email@gmail.com',
            'password1': 'testing12345',
            'password2': 'testing12345'
        })

        self.assertTrue(form.is_valid())

    def test_user_form_no_data(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_comment_form_valid(self):
        form = CommentForm(data={
            'name': 'Leon123',
            'body': 'yeet'
        })

        self.assertTrue(form.is_valid())

    def test_comment_form_no_data(self):
        form = CommentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
