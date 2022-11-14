from django.contrib import admin
from .models import User, Influencer, Brand, Employee


admin.site.register(User)
admin.site.register(Brand)
admin.site.register(Influencer)
admin.site.register(Employee)