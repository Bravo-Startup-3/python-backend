from django.db import models
from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer
from .models import HomePage, Pricing, AboutUs, Services, Terms, Privacy

class HomePageSerializer(ModelSerializer):
    class Meta:
        model = HomePage
        fields = [
            'title',
            'body'
        ]

class PricingSerializer(ModelSerializer):
    class Meta:
        model = Pricing
        fields = [
            'title',
            'body'
        ]

class AboutUsSerializer(ModelSerializer):
    class Meta:
        model = AboutUs
        fields = [
            'title',
            'body'
        ]

class ServicesSerializer(ModelSerializer):
    class Meta:
        model = Services
        fields = [
            'title',
            'body'
        ]

class TermsSerializer(ModelSerializer):
    class Meta:
        model = Terms
        fields = [
            'title',
            'body'
        ]

class PrivacySerializer(ModelSerializer):
    class Meta:
        model = Privacy
        fields = [
            'title',
            'body'
        ]

