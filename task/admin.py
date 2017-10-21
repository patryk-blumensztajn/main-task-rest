from django.contrib import admin
from .models import Material

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name']
admin.site.register(Material, CategoryAdmin)