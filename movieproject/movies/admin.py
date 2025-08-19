from django.contrib import admin
from .models import Genre, Customer, Theater, Movie, Screening, Ticket, Review, User, Role
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User, Role

# 1️⃣ Custom forms to handle password hashing
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'role', 'hire_date', 'is_staff', 'is_active')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'role', 'hire_date', 'is_staff', 'is_active')

# 2️⃣ Custom UserAdmin
class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('username', 'role', 'hire_date', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'role', 'hire_date')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role', 'hire_date', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(Genre)
admin.site.register(Customer)
admin.site.register(Theater)
admin.site.register(Movie)
admin.site.register(Screening)
admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(User, UserAdmin)
admin.site.register(Role)


# Register your models here.
