from django.contrib import admin
from .models import CarMake, CarModel
# ===============================
# Inline admin for CarModel
# ===============================
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of empty forms to display
    fields = ('name', 'type', 'year', 'color', 'price')  # Fields to show inline
    readonly_fields = ('vin_number',)  # VIN should not be editable inline

# ===============================
# CarModel Admin
# ===============================
@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'color', 'price')
    list_filter = ('car_make', 'type', 'year')
    search_fields = ('name', 'car_make__name', 'vin_number')
    ordering = ('car_make', 'name')

# ===============================
# CarMake Admin
# ===============================
@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'founded_year')
    search_fields = ('name', 'country')
    inlines = [CarModelInline]
#
