"""
A few notes about these models:

In this file, I have made a number of assumptions based on my ability to grok both the
`content_api.json` and `quotes_api.json` files. Both of these .json files appear to be
data returned from calls to internal Motley Fool API endpoints (Wagtail CMS?)

The data inside each appears consistently structured and standardized, so I've chosen
to represent the data with relational models (i.e. Django Models + PostgreSQL.)

Some of the data relations in the original .json files are inferrable, while others are
not. I've created several relations to demonstrate based on available data assumptions.
Certain relations will be partial, incorrect, or missing compared to the original
API structure.

Some fields in the .json files are difficult to infer so I have either not included
those fields, or have added 'sample' enumerated choices for demonstration purposes.

Also, per Django documentation standards, Model-level constants and defaults are kept
within the scope of the Model object for both isolation and readability.
"""
import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class Author(models.Model):
    """
    For demonstration, adding several `Contributor Types` even though the original
    `content_api.json` had one contributor type enumeration.

    The original `authors.links` field appears to be an internal API reference,
    and Django should be able to handle with its own ORM syntax. Excluding from the
    Django model because of that reason.
    """

    def clean(self):
        # Example clean method
        if self.byline not in {f"{self.first_name} {self.last_name}", self.username}:
            raise ValidationError(_("Byline must match either real name or username."))

    class ContributorType(models.TextChoices):
        INDIVIDUAL = "individual", _("Individual")
        COMPANY = "company", _("Company")
        SPONSOR = "sponsor", _("Sponsor")
        STAFF = "staff", _("Staff")

    # These are most likely set by CMS (Wagtail?)
    DEFAULT_SMALL_AVATAR_URL = "http://g.foolcdn.com/avatar/1593347483/small.ashx"
    DEFAULT_LARGE_AVATAR_URL = "http://g.foolcdn.com/avatar/1593347483/large.ashx"
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=255, unique=True)
    byline = models.CharField(max_length=255)
    contributor_type = models.CharField(
        max_length=255,
        choices=ContributorType.choices,
        default=ContributorType.INDIVIDUAL,
    )
    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    fool_uid = models.BigIntegerField(unique=True)  # TODO: add a `fool_uid_validator`
    primary = models.BooleanField(default=False)
    small_avatar_url = models.URLField(default=DEFAULT_SMALL_AVATAR_URL)
    large_avatar_url = models.URLField(default=DEFAULT_LARGE_AVATAR_URL)
    twitter_username = models.CharField(max_length=255, null=True, blank=True)
    short_bio = models.TextField(null=True, blank=True)
    long_bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.byline}"


class Article(models.Model):
    class ArticleType(models.TextChoices):
        ARTICLE = "article", _("Article")
        TEN_PROMISE_SERIES = "10-promise-series", _("10 Promise Series")

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    body = models.TextField()
    headline = models.TextField()
    promo = models.TextField(blank=True)
    byline = models.CharField(max_length=255)  # A relation btwn this and Author.byline
    article_type = models.CharField(
        max_length=255, choices=ArticleType.choices, default=ArticleType.ARTICLE
    )
    featured_image_url = models.URLField()
    featured_image_name = models.TextField(null=True, blank=True)
    static_page = models.BooleanField(default=False)
    path = models.TextField(unique=True)  # for the sake of this demo
    created = models.DateTimeField()
    publish_at = models.DateTimeField()
    # In a real-world scenario, modified date would of course get updated appropriately.
    modified = models.DateTimeField()
    disclosure = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.headline}"


class Quote(models.Model):
    """
    Data from `quotes_api.json`.

    My initial thought is to have rows in this table unique based on a combination of
    (Exchange -> Symbol -> Timestamp). Uniqueness constraints will be implemented as
    time allows.

    There is probably a way to save a Company's detailed information as a separate table
    from the quote data (and also historical quote data.)
    """

    class ExchangeType(models.TextChoices):
        # TODO: Eventually add other exchange choices like Nikkei, ASX, etc.
        NYSE = "NYSE", _("NYSE")
        NASDAQ = "NASDAQ", _("NASDAQ")
        NYSEMKT = "NYSEMKT", _("NYSE MKT")
        NASDAQOTH = "NASDAQOTH", _("NASDAQOTH")
        UNKNOWN = "UNKNOWN", _("Unknown")

    class CurrencyType(models.TextChoices):
        USD = "USD", _("USD")
        # TODO: Add other currencies, same as `ExchangeType` above.

    company_name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    exchange = models.CharField(
        max_length=255, choices=ExchangeType.choices, default=ExchangeType.UNKNOWN
    )
    currency_code = models.CharField(
        max_length=255, choices=CurrencyType.choices, default=CurrencyType.USD
    )
    description = models.TextField()
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    # TODO: possible Django validator -> change = (current_price - close_price)
    change = models.DecimalField(max_digits=10, decimal_places=2)
    # TODO: Make percent_change constraints less artbitrary
    percent_change = models.DecimalField(max_digits=30, decimal_places=20)
    website = models.URLField()
    last_trade_date = models.DateTimeField()

    class Meta:
        # There should only be one (symbol + exchange) row for each last_trade_date
        unique_together = ["symbol", "exchange", "last_trade_date"]

    def __str__(self):
        return f"{self.symbol}"


class Tag(models.Model):
    """
    Tag data goes here. Would of course have appropriate constraints and relations.
    """

    pass


class Instruments(models.Model):
    """
    Instruments data goes here. Would of course have appropriate constraints and
    relations.
    """

    pass
