from django.contrib import admin

from common.models import MediaFile, BlogPost


@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ("id", "file")

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "category", "published_date", "comment_count")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "category")
    list_filter = ("category", "published_date")