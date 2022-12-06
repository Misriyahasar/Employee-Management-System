from django.contrib import admin
from .models import User,Leave
# Register your models here.
from rest_framework.authtoken.admin import TokenAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin


TokenAdmin.raw_id_fields = ['user']
admin.site.register(Leave)
@admin.register(User)

class CustomUserAdmin(UserAdmin):
    add_form_template = 'admin/auth/user/add_form.html'
    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'email')}),
        (_('Employee details'), {'fields': ('reporting_to',)}),
        (_('Permissions'), {
        'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        )
    add_fieldsets = (
        (None, {
        'classes': ('wide',),
         'fields': ('email', 'username', 'full_name', 'is_superuser', 'password1', 'password2'),
        }),
        )

