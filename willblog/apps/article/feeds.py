from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from willblog.apps.article.models import Article


class LatestArticleFeed(Feed):
    title = "Willtunner's RSS"
    link = '/article/'
    description = 'New posts of my blog.'

    def items(self):
        return Article.objects.order_by("-create_time")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 100)

    def item_link(self, item):
        return reverse("article:detail", kwargs={"pk": item.id})
