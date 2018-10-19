from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["__str__", "create_date", "published_date"]
    list_filter = ["create_date", "published_date"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
