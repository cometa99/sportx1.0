from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "id"]
#    list_display_links = ["title"]
    list_editable = ["title"]
    list_filter  = ["updated", "timestamp"]
    search_fields = ["title", "content", "primera", "segunda","tercera"]

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
