from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from .models import HomePage, Pricing, AboutUs, Services, Terms, Privacy
from .serializers import HomePageSerializer, PricingSerializer, AboutUsSerializer, ServicesSerializer, TermsSerializer, PrivacySerializer
from rest_framework.permissions import AllowAny

class HomePageAPIView(RetrieveAPIView):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer
    permission_classes = [AllowAny]


class PricingAPIView(RetrieveAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer
    permission_classes = [AllowAny]


class AboutUsAPIView(RetrieveAPIView):
    queryset = Pricing.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [AllowAny]


class ServicesAPIView(RetrieveAPIView):
    queryset = Pricing.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [AllowAny]


class TermsAPIView(RetrieveAPIView):
    queryset = Terms.objects.all()
    serializer_class = TermsSerializer
    permission_classes = [AllowAny]


class PrivacyAPIView(RetrieveAPIView):
    queryset = Privacy.objects.all()
    serializer_class = PrivacySerializer
    permission_classes = [AllowAny]


