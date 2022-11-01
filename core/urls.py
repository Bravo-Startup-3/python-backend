from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^comments/', include("blog.urls", namespace='comments')),
    path(r'^api/users/', include("users.urls", namespace='users-api')),
    path(r'^api/comments/', include("blog.urls", namespace='comments-api')),
    path(r'^api/posts/', include("blog.urls", namespace='posts-api')),
    path(r'^api/auth/token/', obtain_jwt_token),
    path('login/', views.login, name='login'),
    path('users/', include('allauth.urls')),
    path('api/', include("users.urls")),
    path('/', include("users.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)