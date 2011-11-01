# -*- coding:utf-8 -*-
from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from fcpe.models import *
from django_mailman.models import List


from autocomplete.views import autocomplete, AutocompleteSettings
from autocomplete.admin import AutocompleteAdmin


# from django.utils.safestring import mark_safe
# class ModelLinkWidget(forms.Widget):
#     def __init__(self, obj, attrs=None):
#         self.object = obj
#         super(ModelLinkWidget, self).__init__(attrs)
#     def render(self, name, value, attrs=None):
#         if self.object.pk:
#             return mark_safe(u'<a target="_blank" href="../../../%s/%s/%s/">%s</a>' % (self.object._meta.app_label,
#                     self.object._meta.object_name.lower(), self.object.pk, self.object))
#         else:
#             return mark_safe(u'')
# 
# 
# class AdherMoreForm(forms.ModelForm):
#     link = forms.CharField(label='link', required=False)
#     def __init__(self, *args, **kwargs):
#         super(AdherMoreForm, self).__init__(*args, **kwargs)
#         # instance is always available, it just does or doesn't have pk.
#         self.fields['link'].widget = ModelLinkWidget(self.instance)
#     class Meta:
#         model = Adherent

class AdherentInline(admin.TabularInline):
    #form = AdherMoreForm
    model = Adherent.conseil_local.through
    extra = 0
    raw_id_fields = ('adherent',)
    #fields = ('link','telephone','mobile','email')

# class AdherentAutocomplete(AutocompleteSettings):
#     search_fields = ('^nom', '^prenom')
# autocomplete.register(Adherent.conseil_local, AdherentAutocomplete)


class ConseilAdmin(admin.ModelAdmin):
    list_display = ('nom','code','nb_adherents','code_postal','commune')
    raw_id_fields = ('commune',)
    search_fields = ['nom','code']
    inlines = [ AdherentInline, ]
admin.site.register(ConseilLocal,ConseilAdmin)

class FamilleInline(admin.TabularInline):
    model = Enfant
    fields = ('nom','prenom','classe','etablissement')
    raw_id_fields = ('etablissement',)
    extra = 0

class AdherentAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','cfoyer','nb_enfants','telephone','mobile','code_postal','commune')
    search_fields = ['nom','prenom','email','cfoyer','adhesion_id']
    raw_id_fields = ('commune',)
    inlines = [ FamilleInline, ]
    filter_horizontal = ('listes','conseil_local')
    fieldsets = (
        (None, {
            'fields': ('nom', 'prenom', 'email','listes')
        }),
        ('Infos partenaires', {
            'classes': ('collapse',),
            'fields': ('organisation', 'role', )
        }),
        ('Coordonnées', {
            'fields': ('telephone', 'mobile', 'adr1','adr2','commune')
        }),
        ('FCPE', {
            'fields': ('annee_scolaire','cfoyer', 'adhesion_id')
        }),
        
    )
    def save_model(self, request, obj, form, change):
        #prev = obj.listes.values_list('id',flat=True)
        if change:
            prev = obj.listes.all()
            new = form.cleaned_data['listes']
            print prev,new
            for liste in prev :
                if liste not in new :
                    liste.unsubscribe(form.cleaned_data['email'])
                    print "se desinscrire de ",liste.name
            for liste in new :
                if liste not in prev :
                    print "inscrire sur ",liste.name            
                    liste.subscribe(form.cleaned_data['email'], form.cleaned_data['prenom'], form.cleaned_data['nom'])
        super(AdherentAdmin, self).save_model(request, obj, form, change)    
admin.site.register(Adherent,AdherentAdmin)

class EtabAdmin(admin.ModelAdmin):
    list_display = ('nom','code','perimetre','code_postal','commune')
    search_fields = ['nom','commune']
    raw_id_fields = ('commune',)
admin.site.register(Etablissement, EtabAdmin)

admin.site.register(Classe)
admin.site.register(AnneeScolaire)
admin.site.register(Personne)

