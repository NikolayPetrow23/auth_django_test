from django.contrib import admin

from users.models import User, OTP

admin.site.register(OTP)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)
