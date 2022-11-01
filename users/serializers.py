
from rest_framework import serializers
from django_countries.serializers import CountryField
from .models import User, Influencer, Brand, Admin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'password', 'is_brand']

class InfluencerSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['username','email','password', 'password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_influencer=True
        user.save()
        Influencer.objects.create(user=user)
        return user


class BrandSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['username','email','password', 'password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    

    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_brand=True
        user.save()
        Brand.objects.create(user=user)
        return user


class AdminSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['username','email','password', 'password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    

    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_admin=True
        user.save()
        Admin.objects.create(user=user)
        return user















'''from rest_framework import serializers
from .models import User, AdminManager, BrandManager, InfluencerManager, AdminProfile, BrandProfile, InfluencerProfile

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