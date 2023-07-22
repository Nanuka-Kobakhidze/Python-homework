from django.contrib import admin
from .models import Post, Comment, Tag, Categories


class CommentInline(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Categories)
