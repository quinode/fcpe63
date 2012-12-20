# -*- coding:utf-8 -*-
from django.contrib import admin
from communes.models import Commune

class CommuneAdmin(admin.ModelAdmin):
    list_display = ('nom','code_postal','insee')
    search_fields = ['nom','code_postal','maj']
admin.site.register(Commune, CommuneAdmin)


