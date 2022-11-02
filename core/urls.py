from django.contrib import admin
from django.urls import include, re_path
from django.contrib.auth import views as auth_views
from users import views
from django.conf.urls.static import static
from django.conf import settings
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^', include("blog.urls")),
    #re_path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #re_path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path('api/users/', include('allauth.urls')),
    re_path('api/', include("users.urls")),
    re_path('/', include("users.urls")),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)