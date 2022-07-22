from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import ContactUs, User
from .models import UserPost, Event, Profile, Participate

admin.site.register(UserPost)

admin.site.register(Event)
admin.site.register(Profile)
admin.site.register(Participate)
admin.site.register(ContactUs)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'wilaya', 'email', 'is_org', 'org_document']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('wilaya', 'is_org', 'org_document')}),
    )


admin.site.register(User, CustomUserAdmin)


