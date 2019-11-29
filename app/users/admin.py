from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin

from users.models import User


@register(User)
class MaterialUserPictureAdmin(MaterialModelAdmin):
    icon_name = 'person'
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser')
    list_editable = ['is_active']
    list_filter = ('date_joined',)
