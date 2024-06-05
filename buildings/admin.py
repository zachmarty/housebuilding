from django.contrib import admin

from buildings.models import Building, Pillar, Plate

@admin.register(Pillar)
class PillarAdmin(admin.ModelAdmin):
    list_display = ("serial_number", "length", "width", "height")

@admin.register(Plate)
class PlateAdmin(admin.ModelAdmin):
    list_display = ("serial_number", "length", "width", "height")

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("name", "length", "width", "height")