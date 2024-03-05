from django.contrib import admin
from .models import Departman, Personel

@admin.register(Departman)
class DepartmanAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_people_display']
    search_fields =  ['name']

    def total_people_display(self, departman):
        return departman.total_people()
    total_people_display.short_description = 'Toplam Personel Sayısı'

@admin.register(Personel)
class PersonelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'title', 'gender', 'salary', 'start_date', 'departman', 'user','calculate_working_days']
    search_fields = ['first_name', 'last_name']
