from django_countries.fields import CountryField
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        INFLUENCER = "INFLUENCER", "Influencer"
        BRAND = "BRAND", "Brand"

    base_role = Role.INFLUENCER

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class AdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.ADMIN)

class Admin(User):

    base_role = User.Role.ADMIN

    admin = AdminManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for staff of the company with company branded emails"
        

@receiver(post_save, sender=Admin)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "ADMIN":
        AdminProfile.objects.create(user=instance)


class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=200, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    tik_tok_url = models.URLField(null=True, blank=True)


class InfluencerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.INFLUENCER)

class Influencer(User):

    base_role = User.Role.INFLUENCER

    influncer = InfluencerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for influencers"
        

@receiver(post_save, sender=Influencer)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "INFLUENCER":
        InfluencerProfile.objects.create(user=instance)


class InfluencerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    influencer_id = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    portfolio = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    tik_tok_url = models.URLField(null=True, blank=True)

class BrandManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.BRAND)


class Brand(User):

    base_role = User.Role.BRAND

    brand = BrandManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for brands"


class BrandProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    brand_id = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=200, null=True, blank=True)
    company_size = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    tik_tok_url = models.URLField(null=True, blank=True)


@receiver(post_save, sender=Brand)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "BRAND":
        BrandProfile.objects.create(user=instance)

'''
class User(AbstractUser):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    brand_name = models.CharField(max_length=200, null=True, blank=True)
    company_size = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=200, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    portfolio = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    tik_tok_url = models.URLField(null=True, blank=True)

class UserRole(User):
    userfield = models.ForiegnKey(User, on_delete=models.CASCADE)

class AccountType(UserRole):
    CHOICES = (
        ('Influencer', 'Influencer'),
        ('Brand', 'Brand'),
        ('Admin', 'Admin'),
    )
'''