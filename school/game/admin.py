from django.contrib import admin
from .models import Inscription,Score

class Afficher(admin.ModelAdmin):
    list_display= ["nom","email","password","image","date_creation"]
class AfficherScore(admin.ModelAdmin):
    list_display= ["joueur","score"]
admin.site.register(Score,AfficherScore)
admin.site.register(Inscription,Afficher)

# Register your models here.
# 
