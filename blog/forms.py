# _*_ coding: utf-8 _*_

from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text='Please enter the category name.')
    views = forms.IntegerField(initial=0, widget=forms.HiddenInput())
    slug = forms.CharField(required=False, widget=forms.HiddenInput())

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='Please enter the title of the page.')
    url = forms.URLField(help_text='Please enter the URL of the page.')
    description = forms.Textarea()

    class Meta:
        model = Page
        # Or you can use exclude = ('category',)
        fields = ('title', 'url', 'description')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith(('http://', 'https://')):
            url = 'http://' + url
            cleaned_data['url'] = url
        return cleaned_data


class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='Please enter the title of the page.')
    context = forms.CharField()

    class Meta:
        model = Article
        fields = ('title', 'context')


class UserForm(forms.ModelForm):
    # user model include password , but it is not hidden when user input their password ,so redesign it.
    password = forms.CharField(max_length=20, min_length=6, widget=forms.PasswordInput())
    username = forms.CharField(max_length=18)
    first_name = forms.CharField(max_length=18)
    last_name = forms.CharField(max_length=18)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    photo = forms.ImageField(required=False)
    nickname = forms.CharField(max_length=18)

    class Meta:
        model = UserProfile
        fields = ('photo', 'nickname')
