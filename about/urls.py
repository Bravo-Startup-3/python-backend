from django.urls import include, re_path
from django.contrib import admin
from .views import HomePageAPIView, PricingAPIView, AboutUsAPIView, TermsAPIView, ServicesAPIView, PrivacyAPIView

app_name = 'about'
urlpatterns = [
    re_path('', HomePageAPIView.as_view()),
    re_path('about/pricing', PricingAPIView.as_view()),
    re_path('about-us', AboutUsAPIView.as_view()),
    re_path('about/terms', TermsAPIView.as_view()),
    re_path('about/services', ServicesAPIView.as_view()),
    re_path('about/privacy', PrivacyAPIView.as_view()),
]
