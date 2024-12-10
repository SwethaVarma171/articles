from django.contrib import admin
from .models import Articles

@admin.register(Articles)
class AdminArticles(admin.ModelAdmin):
    list_display=['title','discription']
    # list_display_links=['title']
