from django.contrib import admin
#from .views import post_list, post_create, post_detail, post_update, post_delete
from django.urls import include, re_path
from django.contrib import admin

from .views import PostCreateAPIView, PostDeleteAPIView, PostDetailAPIView, PostListAPIView, PostUpdateAPIView
#from .views import comment_thread, comment_delete
from .views import CommentCreateAPIView, CommentDetailAPIView, CommentListAPIView

app_name = 'blog'
urlpatterns = [
    #PostAPI
	re_path(r'^$', PostListAPIView.as_view()),
    re_path(r'^create/$', PostCreateAPIView.as_view()),
    re_path(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view()),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view()),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view()),
	re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

	#CommentAPI
	re_path(r'^$', CommentListAPIView.as_view()),
    re_path(r'^create/$', CommentCreateAPIView.as_view()),
    re_path(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view()),
    #re_path(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]
