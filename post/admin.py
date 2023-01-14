from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
	list_display = ["title", "author", "date_created"]
	list_filter = ["author", "date_created"]
	search_fields = ["author", "title", "content"]
	
	
class CommentAdmin(admin.ModelAdmin):
	list_display = ["commenter", "content"]
	search_fields = ["commenter"]
	
	
admin.site.register(Post, PostAdmin)
admin.site.register(Subscriber)
admin.site.register(Comment, CommentAdmin)