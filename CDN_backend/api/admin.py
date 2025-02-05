from django.contrib import admin

from .models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "latitude", "longitude",)
    search_fields = ("name",)
    list_filter = ("name",)


admin.site.register(City, CityAdmin)
