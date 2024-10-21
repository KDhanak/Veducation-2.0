from django.contrib import admin
from .models import Account, Publication
from  django.contrib.admin.models import LogEntry  

# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        LogEntry.objects.filter(user_id=obj.id).delete()  # Delete log entries for the user
        obj.delete()  # Now delete the user

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            LogEntry.objects.filter(user_id=obj.id).delete()  # Delete log entries for each user
        super().delete_queryset(request, queryset)  # Call the parent method to delete the users

admin.site.register(Publication)
