from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Comment

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["title", "content"]
	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment)

'''from django.contrib import admin
from blog.models import Post, Category, Comment

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)'''