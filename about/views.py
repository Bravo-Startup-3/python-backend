'''from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .pagination import PageLimitOffsetPagination, PageNumberPagination
from .permissions import IsOwnerOrReadOnly 
from .serializers import PageCreateUpdateSerializer, PageDetailSerializer, PageListSerializer
from django.contrib.auth.decorators import login_required

from .models import Page
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin

#Page APIs
class PageCreateAPIView(CreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageCreateUpdateSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PageDetailAPIView(RetrieveAPIView):
    queryset = Page.objects.all()
    serializer_class = PageDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    #lookup_url_kwarg = "abc"


class PageUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email


class PageDeleteAPIView(DestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"


class PageListAPIView(ListAPIView):
    serializer_class = PageListSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    search_fields = ['title', 'content', 'user__first_name']
    pagination_class = PageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PageListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Page.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(title__icontains=query)|
                    Q(content__icontains=query)|
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list
'''