from django.contrib import admin

# Register your models here.
from .models import Entries


class EntriesAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Entries, EntriesAdmin)
