from django.contrib import admin
from .models import Post, Author

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ()
    prepopulated_fields = {'slug': ('title',)}
    # list_display
    # list_filter = ('author', )

admin.site.register(Post, PostAdmin)
admin.site.register(Author)