from django.contrib import admin
from .models import Tgusers,Button
# Register your models here.


admin.site.register(Tgusers)
class SingletonModelAdmin(admin.ModelAdmin):
    """
    Prevents Django admin users deleting the singleton or adding extra rows.
    """
    actions = None  # Removes the default delete action.

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

@admin.register(Button)
class ButtonAdmin(SingletonModelAdmin):
    pass


