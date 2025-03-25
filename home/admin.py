from django.contrib import admin
from home.models import *


# **


admin.site.register(GlazingFrameless)


# admin.site.register(GlazingAdvantage)
@admin.register(GlazingAdvantage)
class GlazingAdvantageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'glazing')
    list_filter = ['created_timestamp']
    search_fields = ['title', 'description']
    ordering = ['id']


admin.site.register(GlazingType)
admin.site.register(GlazingTypeMovement)
