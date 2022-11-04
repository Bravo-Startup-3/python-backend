from django.urls import include, re_path
from django.contrib import admin

from .views import PageCreateAPIView, PageDeleteAPIView, PageDetailAPIView, PageListAPIView, PageUpdateAPIView


#app_name = 'about'
urlpatterns = [
    #PostAPI
	#re_path(r'^$', PageListAPIView.as_view()),
    #re_path(r'^create/$', PageCreateAPIView.as_view()),
    #re_path(r'^(?P<slug>[\w-]+)/$', PageDetailAPIView.as_view()),
    #re_path(r'^(?P<slug>[\w-]+)/edit/$', PageUpdateAPIView.as_view()),
    #re_path(r'^(?P<slug>[\w-]+)/delete/$', PageDeleteAPIView.as_view()),

    re_path(r'^$', PageListAPIView.as_view(), name='list'),
    re_path(r'^create/$', PageCreateAPIView.as_view(), name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', PageDetailAPIView.as_view(), name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', PageUpdateAPIView.as_view(), name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', PageDeleteAPIView.as_view(), name='delete'),
	re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]


	