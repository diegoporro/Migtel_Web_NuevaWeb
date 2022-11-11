from django.db import models
from django.contrib import admin

CIUDAD = [
    ['Higuerote', 'Higuerote'],
    ['Caracas', 'Caracas'],
    ['Guarenas - Guatire', 'Guarenas - Guatire'],
]

ZONA = [
    ['1', '1'],
    ['2', '2'],
    ['3', '3'],
    ['4', '4'],
]


class Cobertura(models.Model):
    ciudad = models.CharField(max_length=20, null=False, blank=False, choices=CIUDAD)
    zona = models.CharField(max_length=20, null=False, blank=False, choices=ZONA)
    sector = models.CharField(max_length=180, null=False, blank=False, default='')

    def __str__(self):
        return self.sector


class CoberturaAdmin(admin.ModelAdmin):
    list_display = ('ciudad', 'zona', 'sector')
    search_fields = ['ciudad', 'zona', 'sector']
