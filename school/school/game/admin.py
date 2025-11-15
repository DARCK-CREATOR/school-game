from django.contrib import admin
from .models import Inscription


class Afficher(admin.ModelAdmin):
    list_display= ["nom","email","password","image","date_creation"]
    
admin.site.register(Inscription,Afficher)
# Register your models here.
# 
