"""
The 'throwback' API endpoints are duplicates of the main project functionality, with
updated HTML + CSS for the UI. Eventually I plan to make the duplicate functions better
follow 'Don't Repeat Yourself (D.R.Y.)' principles. I would also consider making some
kind of `/helpers/` directory to house the non-standard helper/utility functions.
"""
import random
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Quote


def index(request):
    """
    Retrive the "10 Promise Series" Article instance with the newest
    `Article.publish_at` date, then pass that Article instance into its corresponding
    Django template.
    """
    newest_promise_article = Article.objects.filter(
        article_type=Article.ArticleType.TEN_PROMISE_SERIES
    ).latest("publish_at")
    # TODO: This will ensure uniqueness of main article, but not the three others. Fix.
    articles = Article.objects.exclude(uuid=newest_promise_article.uuid)
    context = {
        "main_article": newest_promise_article,
        "article_1": random.choice(articles),
        "article_2": random.choice(articles),
        "article_3": random.choice(articles),
    }
    return render(request, "blog/home.html", context)


def index_throwback(request):
    """Same as standard `index()` but with a little personal flair."""
    newest_promise_article = Article.objects.filter(
        article_type=Article.ArticleType.TEN_PROMISE_SERIES
    ).latest("publish_at")
    # TODO: This will ensure uniqueness of main article, but not the three others. Fix.
    articles = Article.objects.exclude(uuid=newest_promise_article.uuid)
    context = {
        "main_article": newest_promise_article,
        "article_1": random.choice(articles),
        "article_2": random.choice(articles),
        "article_3": random.choice(articles),
    }
    return render(request, "throwback/home.html", context)


def article_detail(request, uuid):
    article = Article.objects.get(uuid=uuid)
    quotes = Quote.objects.all()
    context = {
        "article_det": article,
        "quote_1": random.choice(quotes),
        "quote_2": random.choice(quotes),
        "quote_3": random.choice(quotes),
    }
    return render(request, "blog/article.html", context)


def article_detail_throwback(request, uuid):
    article = Article.objects.get(uuid=uuid)
    quotes = Quote.objects.all()
    context = {
        "article_det": article,
        "quote_1": random.choice(quotes),
        "quote_2": random.choice(quotes),
        "quote_3": random.choice(quotes),
    }
    return render(request, "throwback/article.html", context)


def get_three_more_quotes(request):
    """Handling AJAX from an Article page. Retrieves three new Quote instances."""
    if request.is_ajax and request.method == "GET":
        quotes = Quote.objects.all()
        data = [
            model_to_dict(random.choice(quotes)),
            model_to_dict(random.choice(quotes)),
            model_to_dict(random.choice(quotes)),
        ]
        return HttpResponse(data)


def sanity_check(request):
    """Verification of a successfully running Django API server."""
    return HttpResponse("Congratulations, application installed successfully!")
