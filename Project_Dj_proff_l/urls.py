"""
URL configuration for Project_Dj_proff_l project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# для sitemap
from home.sitemaps import *
from home.views import page_not_found
from django.contrib.sitemaps.views import sitemap
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('home.urls', namespace='home')),
    path('windows/', include('windows.urls', namespace='windows')),
]


# **


handler404 = page_not_found


# **


# для sitemap
sitemaps = {
    "glazing_frameless": GlazingFramelessSitemap,
    "glazing_type": GlazingTypeSitemap,
    "static": StaticViewSitemap,
}

urlpatterns += [
    path('sitemap.xml', cache_page(86400)(sitemap), {'sitemaps': sitemaps}, name='sitemap'),
]