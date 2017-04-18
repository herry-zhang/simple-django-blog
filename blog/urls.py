# _*_ coding: utf-8 _*_

from django.conf.urls import url
from blog.views import *

# index
urlpatterns = [
    url(r'^$', index, {'template': 'blog/index/index.html'}, name='index'),
    url(r'^search/$', search, {'template': 'blog/index/search.html'},
        name='search'),
]

# about
urlpatterns += [
    url(r'^about/$', about, {'template': 'blog/about/about.html'},
        name='about'),
    url(r'^contact$', contact_me, {'template': 'blog/about/contact.html'},
        name='contact'),
]
# account
urlpatterns += [
    url(r'^account/register/$', register, {'template': 'blog/account/register.html'}, name='register'),
    url(r'^account/login/$', user_login,
        {'template': 'blog/account/login.html', 'loginFalse': 'blog/account/login-false.html'}, name='login'),
    url(r'^account/logout/$', user_logout, {'redirect': '/'}, name='logout'),
    url(r'^account/profile/$', user_profile, {'template': 'blog/account/user_profile.html'}, name='user_profile'),
]

# content
urlpatterns += [
    url(r'^(?P<category>(\w|-)+)/pages/$', page,
        {'template': 'blog/content/page.html'}, name='pages'),
    url(r'^(?P<category>(\w|-)+)/articles/$', article,
        {'template': 'blog/content/articles.html'}, name='articles'),
    url(r'^pages/$', page, {'template': 'blog/content/page.html'},
        name='all_pages'),
    url(r'^articles/$', article, {'template': 'blog/content/articles.html'},
        name='all_articles'),
    url(r'^article/(?P<writings>(\w|-|\d)+)/$', article,
        {'template': 'blog/content/article.html'},
        name='article'),
]

# add content
urlpatterns += [
    url(r'^add-page/$', add_page,
        {'template': 'blog/add_content/add_page.html'}, name='add_page'),
    url(r'^add-article/$', add_article,
        {'template': 'blog/add_content/add_article.html'}, name='add_article'),
    url(r'^add-category/$', add_category,
        {'template': 'blog/add_content/add_category.html'},
        name='add_category'),
    url(r'^markdown/preview/$', pre_markdown,
        {'template': 'blog/add_content/markdown-preview.html'},
        name='markdown_preview')
]
