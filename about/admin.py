from django.contrib import admin

from about.views import PageCreateAPIView

# Register your models here.
from .models import Page

class PageModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["title", "content"]
	class Meta:
		model = PageCreateAPIView


admin.site.register(Page, PageModelAdmin)