from django.contrib.admin import ModelAdmin, register

from users.models import User


@register(User)
class MaterialUserPictureAdmin(ModelAdmin):
    icon_name = 'person'
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser')
    list_editable = ['is_active']
    list_filter = ('date_joined',)
