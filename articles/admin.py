from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ()
    prepopulated_fields = {'slug': ('title',)}
    # list_display
    list_filter = ('author', )

admin.site.register(Post, PostAdmin)