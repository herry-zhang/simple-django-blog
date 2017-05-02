from article.models import Article
from collection.models import Collection


def get_sidebar_content():
    try:
        popular_articles = Article.objects.order_by("-views")[:5]
        new_articles = Article.objects.order_by("-pub_time")[:5]
        popular_collections = Collection.objects.order_by("-views")[:5]
        new_collections = Collection.objects.order_by("-pub_time")[:5]
    except:
        return {}
    else:
        return {"popular_articles": popular_articles,
                "new_articles": new_articles,
                "popular_collections": popular_collections,
                "new_collections": new_collections,
                }
