from django.urls import path
from .views import ( InfluencerSignupView,
 BrandSignupView, AdminSignupView,
 CustomAuthToken, LogoutView, BrandOnlyView, InfluencerOnlyView, AdminOnlyView)

urlpatterns=[
    path('signup/influencer/', InfluencerSignupView.as_view()),
    path('signup/brand/', BrandSignupView.as_view()),
    path('signup/admin/', AdminSignupView.as_view()),
    path('login/',CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('influencer/dashboard/', InfluencerOnlyView.as_view(), name='influencer-dashboard'),
    path('brand/dashboard/', BrandOnlyView.as_view(), name='brand-dashboard'),
    path('admin/dashboard/', AdminOnlyView.as_view(), name='admin-dashboard'),
]