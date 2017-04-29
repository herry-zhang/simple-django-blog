from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from article.models import Article


class LatestArticleFeed(Feed):
    title = 'willtunner'
    link = '/article/'
    description = 'New posts of my blog.'

    def items(self):
        return Article.objects.order_by("-pub_time")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)

    def item_link(self, item):
        return reverse("article_detail", kwargs={"pk": item.id})
