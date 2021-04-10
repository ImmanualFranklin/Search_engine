from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.
@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    search_fields = ('name', )
    list_display = ('name',)
    pass
# Register your models here.
