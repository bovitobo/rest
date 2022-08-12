from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from .api_views.article import ArticleViewSet

admin.autodiscover()
from .views.main import main_page

# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter('')
router.register(r'article', ArticleViewSet)

urlpatterns = [
    path('', main_page),
]
urlpatterns += router.urls
