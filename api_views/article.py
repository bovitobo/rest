# -*- coding: utf-8 -*-
import json

from django.db.models import Q
from rest_framework import permissions, serializers, status, viewsets
from rest_framework.response import Response

from rest.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Use these methods to override default behavior of Django Rest Framework
    """
    def create(self, request, *args, **kwargs):
        json_items = json.loads(request.data.get('items'))
        serializer = self.get_serializer(data=json_items, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        response_dict = {"success": True, "items": serializer.data, 'total': 1}
        return Response(response_dict, status=status.HTTP_201_CREATED, headers=headers)

    # Get records
    def list(self, request, *args, **kwargs):
        start = 0
        if 'start' in request.query_params:
            start = int(request.query_params.get('start'))

        limit = 100
        if 'limit' in request.query_params:
            limit = int(request.query_params.get('limit'))

        sort = []
        if 'sort' in request.query_params:
            sort_attrib = json.loads(request.query_params.get('sort'))
            for s in sort_attrib:
                if s['property'] is None:
                    continue
                if s['direction'] == 'DESC':
                    s['property'] = '-' + s['property']
                sort.append(s['property'])

        sq = Q()

        if 'query' in self.request.query_params:
            query = self.request.query_params.get('query').strip()
            sq = Q(name__icontains=query) | Q(description__icontains=query)

        queryset = Article.objects.filter(sq).extra(order_by=sort)[start:start+limit]
        serializer = self.get_serializer(queryset, many=True)
        response = {"success": True, "items": serializer.data, 'total': Article.objects.filter(sq).count()}
        return Response(response, status=status.HTTP_200_OK)

    # GET single record
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        response = {"success": True, "items": serializer.data, 'total': 1}
        return Response(response, status=status.HTTP_200_OK)  # return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        json_items = json.loads(request.data.get('items'))

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=json_items, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        response_dict = {"success": True, "items": serializer.data, 'total': 1}
        return Response(response_dict, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            self.perform_destroy(instance)

            return Response({"success": True}, status=status.HTTP_200_OK)  # return Response(status=status.HTTP_204_NO_CONTENT)
    """