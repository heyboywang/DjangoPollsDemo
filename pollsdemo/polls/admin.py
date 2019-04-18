from django.contrib import admin
from .models import Options,Questions

# Register your models here.
admin.site.register(Questions)

class OptionsAdmin(admin.ModelAdmin):
    list_display = ['id','option','num']

admin.site.register(Options,OptionsAdmin)
