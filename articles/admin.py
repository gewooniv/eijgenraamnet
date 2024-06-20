from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Author, CustomUser

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ()
    prepopulated_fields = {'slug': ('title',)}
    # list_display
    list_filter = ('author', )

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        "email",
        "first_name",
        "last_name",
        "date_of_birth",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "first_name",
        "last_name",
        "date_of_birth",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": (
            "first_name",
            "last_name", 
            "email", 
            "password", 
            "date_of_birth")}
        ),
        ("Permissions", {"fields": (
            "is_staff", 
            "is_active", 
            "groups", 
            "user_permissions")}
        ),
    )
    add_fieldsets = (
        ( None, {"fields": (
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "date_of_birth",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions")}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(Post, PostAdmin)
admin.site.register(Author)