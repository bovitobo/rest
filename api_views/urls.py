# -*- coding: utf-8 -*-
from django.urls import path, include
from django.contrib import admin

from rest_framework import routers

from .article import ArticleViewSet

admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter('')
router.register(r'article', ArticleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += router.urls
