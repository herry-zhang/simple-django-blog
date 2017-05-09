from django import forms
from willblog.apps.article.models import Article, Category


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='标题')
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    content = forms.CharField(label='内容')

    class Meta:
        model = Article
        fields = ['title', 'category', 'content']
