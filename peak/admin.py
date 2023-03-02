from django.contrib import admin
from import_export.admin import ExportActionMixin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Peak, WhiteListCountry, RejectedConnexion

@admin.register(Peak)
class PeakAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name', 'latitude', 'longitude', 'altitude']
    list_display = ('name', 'latitude', 'longitude', 'altitude','full_url')

@admin.register(WhiteListCountry)
class WhiteListCountryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['country_code']
    list_display = ('country_code',)


@admin.register(RejectedConnexion)
class RejectedConnexionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['ip', 'country_code']
    list_display = ('ip', 'country_code',)
