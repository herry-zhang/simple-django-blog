from willblog.apps.article.models import Article
from willblog.apps.collection.models import Collection


def get_popular(limit=None):
    if limit:
        try:
            popular_articles = Article.objects.order_by("-views")[:limit]
            popular_collections = Collection.objects.order_by("-views")[:limit]
        except:
            return {}
        else:
            return {"popular_articles": popular_articles,
                    "popular_collections": popular_collections,
                    }
    else:
        try:
            popular_articles = Article.objects.order_by("-views")
            popular_collections = Collection.objects.order_by("-views")
        except:
            return {}
        else:
            return {"popular_articles": popular_articles,
                    "popular_collections": popular_collections,
                    }
