from django import forms
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from post.models import Post, Comment
from django_ckeditor_5.widgets import CKEditor5Widget


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                    'placeholder': "name@company.com",
                    'required': True,
                }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                    'placeholder': "••••••••",
                    'required': False,
                }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required")
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is not registered")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("Password is required")
        return password

    def user_authenticate(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                return user
            else:
                raise forms.ValidationError("Invalid Password")
        except User.DoesNotExist:
            pass
        return None


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                    'placeholder': "johndoe",
                    'required': True,
                }),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                    'placeholder': "John",
                    'required': True,
                }),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                    'placeholder': "Doe",
                    'required': True,
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                    'placeholder': "name@company.com",
                    'required': True,
                }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                    'placeholder': "••••••••",
                    'required': False,
                }),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        if not email:
            raise forms.ValidationError("Email is required")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already registred")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Opps! Username is taken by another")
        return email


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False

    class Meta:
        model = Post
        fields = ['image', 'title', 'content', 'created_by']

        help_texts = {
            'image': " Upload an Image for thubnail of Blog"
        }
        labels = {
            'image':"Thumbnail"
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500',
                    'placeholder': "Type title of blog",
                    'required': True,
                }),
            'image': forms.FileInput(
                attrs={
                    'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
                    'required': False,
                }),
            'created_by': forms.HiddenInput()
        }
        content = CKEditor5Widget(attrs={
            'class': 'django_ckeditor_5'
        },
            config_name='extends')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', 'comment_by', 'comment_post']

        widgets = {
            'comment_text': forms.Textarea(
                attrs={
                    'class': "px-0 w-full text-sm text-gray-900 border-0 focus:ring-0 dark:text-white dark:placeholder-gray-400 dark:bg-gray-800",
                    'placeholder': 'Write a comment...',
                    'rows': 6,
                    'required': True
                }
            ),
            'comment_post': forms.HiddenInput(),
            'comment_by': forms.HiddenInput()
        }
