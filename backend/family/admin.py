# your_app/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Person
from .forms import PersonForm


# Register your custom User model with the admin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    form = PersonForm
    autocomplete_fields = ['spouses', 'parents']
    list_display = ('first_name', 'last_name', 'gender')
    search_fields = ('first_name', 'last_name')