from django.contrib import admin
from .views import post_list, post_create, post_detail, post_update, post_delete
from django.conf.urls import url, include
from django.contrib import admin

from .views import PostCreateAPIView, PostDeleteAPIView, PostDetailAPIView, PostListAPIView, PostUpdateAPIView
from .views import comment_thread, comment_delete
from .views import CommentCreateAPIView, CommentDetailAPIView, CommentListAPIView

urlpatterns = [
    #PostAPI
	url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),
	
	#Post
	url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

	#Comment
    url(r'^(?P<id>\d+)/$', comment_thread, name='thread'),
    url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),

	#CommentAPI
	url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
    #url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]

urlpatterns = [

    #url(r'^posts/$', "<appname>.views.<function_name>"),
]

