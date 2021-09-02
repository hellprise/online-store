from django.contrib import admin
from users.models import User
from products.admin import BasketAdminInline


@admin.register(User) # равносильно admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdminInline,)