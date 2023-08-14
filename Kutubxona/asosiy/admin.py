from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *

# Register your models here.

# registratsiya qilishning 2-usuli:
@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ['id','ism','kurs','yosh','kitob_soni','user']
    list_display_links = ['ism']
    list_editable = ['kurs','kitob_soni','user']
    search_fields = ['ism','kurs']
    search_help_text = "Kursi, ismi bo'yicha qidiring."
    list_filter = ["kurs"]
    list_per_page = 5

@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ["id","ism","tugilgan_yil","tirik","kitoblari_soni","jinsi"]
    list_display_links = ["ism","id"]
    list_editable = ["kitoblari_soni","tirik"]
    search_fields = ["ism"]
    search_help_text = "Ismi bo'yicha qidiring."
    list_filter = ["tirik"]

@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ["id","nom","muallif","sahifa","janr"]
    list_display_links = ["nom"]
    list_editable = ["sahifa","muallif"]
    list_filter = ["janr"]
    search_fields = ["nom","muallif__ism"]
    search_help_text = "Nomi va muallifining ismi bo'yicha qidiring."
    autocomplete_fields = ["muallif"] # ma'lumot qo'shishda

@admin.register(Kutubxonachi)
class KutubxonachiAdmin(admin.ModelAdmin):
    list_display = ["id","ism","ish_vaqti"]
    list_display_links = ["ism"]
    list_editable = ["ish_vaqti"]
    list_filter = ["ish_vaqti"]
    search_fields = ["ism"]
    search_help_text = "Ismi bo'yicha qidiring."

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ["id","talaba","kitob","kutubxonachi","olingan_sana","qaytardi","qaytarish_sanasi"]
    list_display_links = ["id"]
    list_editable = ["qaytardi"]
    list_filter = ["qaytardi"]
    search_fields = ["talaba__ism"]
    search_help_text = "Talabani ismi bo'yicha qidiring."
    autocomplete_fields = ["talaba","kitob","kutubxonachi"]

# registratsiya qilishning 1-usuli:
# admin.site.register(Talaba)
# admin. site. register(Kutubxonachi)
# admin. site. register(Muallif)
# admin. site. register(Kitob)
# admin. site. register(Record)


