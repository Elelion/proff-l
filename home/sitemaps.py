from django.contrib.sitemaps import Sitemap
from .models import *
from django.urls import reverse


class GlazingFramelessSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return GlazingFrameless.objects.all()

    def lastmod(self, obj):
        return obj.created_timestamp

    def location(self, obj):
        return reverse("home:glazing_frameless_detail", args=[obj.pk])


# **


class GlazingTypeSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return GlazingType.objects.all()

    def lastmod(self, obj):
        return obj.created_timestamp

    def location(self, obj):
        return reverse("home:glazing_frameless_type_detail", args=[obj.pk])


# **


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ["home:index", "home:success_mail", "home:feedback_modal", "home:page_not_found"]

    def location(self, item):
        return reverse(item)
