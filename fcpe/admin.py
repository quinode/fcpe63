# -*- coding:utf-8 -*-
from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from fcpe.models import *
from django_mailman.models import List

from fcpe.autocomplete_admin import FkAutocompleteAdmin,InlineAutocompleteAdmin
from django.utils.translation import ugettext_lazy as _


#from autocomplete.views import autocomplete, AutocompleteSettings
#from autocomplete.admin import AutocompleteAdmin


from django.utils.safestring import mark_safe
from django.utils.html import escape


import unicodedata
def to_ascii(input_str):
    nkfd_form = unicodedata.normalize('NFKD', unicode(input_str))
    only_ascii = nkfd_form.encode('ASCII', 'ignore')
    return only_ascii


class AdherLinkWidget(forms.Widget):
    def __init__(self, obj, attrs=None):
        self.object = obj
        super(AdherLinkWidget, self).__init__(attrs)
    def render(self, name, value, attrs=None):
        if self.object.pk:
            return mark_safe(u'<a href="../../../%s/%s/%s/">%s</a>' % (self.object._meta.app_label,
                    self.object.adherent._meta.object_name.lower(), self.object.adherent.pk, u'Fiche adhérent'))
        else:
            return mark_safe(u'')


class AdherMoreForm(forms.ModelForm):
    link = forms.CharField(label='link', required=False)
    def __init__(self, *args, **kwargs):
        super(AdherMoreForm, self).__init__(*args, **kwargs)
        # instance is always available, it just does or doesn't have pk.
        self.fields['link'].widget = AdherLinkWidget(self.instance)
    class Meta:
        model = Adherent.conseil_local.through


class AdherentInline(admin.TabularInline):
    form = AdherMoreForm
    model = Adherent.conseil_local.through
    extra = 0
    raw_id_fields = ('adherent',)
    fields = ('adherent', 'link', 'adhesion_primaire', 'role')


class ConseilAdmin(FkAutocompleteAdmin):
    list_display = ('nom','primaire','secondaire','code','nb_adherents','code_postal','commune')
    list_display_links = ('nom',)
    list_editable = ('primaire','secondaire')
    related_search_fields = {  'commune': ('nom','maj','code_postal'), }
    search_fields = ['nom','code', 'commune']
    inlines = [ AdherentInline, ]
admin.site.register(ConseilLocal,ConseilAdmin)




class ParentLinkWidget(forms.Widget):
    def __init__(self, obj, attrs=None):
        self.object = obj
        super(ParentLinkWidget, self).__init__(attrs)
    def render(self, name, value, attrs=None):
        if self.object.pk:
            return mark_safe(u'<b><a href="../../../fcpe/adherent/%s/">%s</a></b>' % (self.object.pk, u'Fiche adhérent'))
        else:
            return mark_safe(u'')

class ParentInlineForm(forms.ModelForm):
    link = forms.CharField(label='link', required=False)
    def __init__(self, *args, **kwargs):
        super(ParentInlineForm, self).__init__(*args, **kwargs)
        # instance is always available, it just does or doesn't have pk.
        self.fields['link'].widget = ParentLinkWidget(self.instance)
    class Meta:
        model = Adherent




class FamilleInline(InlineAutocompleteAdmin):
    model = Enfant
    fields = ('nom','prenom','classe','etablissement')
    related_search_fields = {  'etablissement': ('nom','commune__nom','commune__code_postal'), }
    extra = 0


class ParentsInline(InlineAutocompleteAdmin):
    model = Adherent
    form = ParentInlineForm
    fields = ('nom','prenom','link','telephone','mobile','email')
    extra = 0


class FoyerAdmin(FkAutocompleteAdmin):
    list_display = ('__unicode__','nom_adherent1','nb_enfants','commune',)
    related_search_fields = {  'commune': ('nom','maj','code_postal'), }
    search_fields = ['code_foyer','commune__code_postal','commune__nom','commune__maj','rattachement__nom']
    inlines = [ParentsInline,FamilleInline]
admin.site.register(Foyer,FoyerAdmin)


class EngagementInline(InlineAutocompleteAdmin):
    model = Engagement
    related_search_fields = {  'conseil_local': ('nom','commune__nom','commune__code_postal'), }
    extra = 1


from django.contrib.admin.widgets import AdminTextInputWidget
from django.core.urlresolvers import reverse

class LinkWidget(AdminTextInputWidget):
    def render(self, name, value, attrs=None):
        #s = super(AdminTextInputWidget, self).render(name, value, attrs)
        s = '<a href="%s">%s</a>' % ( value,
            #reverse('admin:fcpe_foyer_change', (value.foyer.id,)),
            'Voir la fiche du foyer')
        return mark_safe(s)



class ModelLinkWidget(forms.HiddenInput):
    def __init__(self, admin_site, original_object):
        self.admin_site = admin_site
        self.original_object = original_object
        super(ModelLinkWidget,self).__init__()

    def render(self, name, value, attrs=None):
        if value is not None:
            link = '/admin/fcpe/foyer/%d/' % (self.original_object.pk)
            enfants = '<p><b>Enfants : </b><br/><ul>'
            for e in self.original_object.famille.all():
                enfants += '<li>%s</li>' % unicode(e)
            enfants += '</ul></p>'
            return super(ModelLinkWidget, self).render(name, value, attrs) + mark_safe('''<a href="%s">%s</a>''' % (link, escape(unicode(self.original_object))) + enfants)
        else:
            return mark_safe(u'<b>Vous ajoutez un adhérent sans avoir préalablement <a href="/admin/fcpe/foyer/add/">créé son Foyer</a> ! </b>')

class ModelLinkAdminFields(object):
    def get_form(self, request, obj=None):
        form = super(ModelLinkAdminFields, self).get_form(request, obj)

        if hasattr(self, 'modellink'):
            for field_name in self.modellink:
                if field_name in form.base_fields:
                    form.base_fields[field_name].widget = ModelLinkWidget(self.admin_site, getattr(obj, field_name, ''))
                    form.base_fields[field_name].required = False
        return form


class AdherentAdminForm(forms.ModelForm):
    lien_foyer = forms.CharField(max_length=250)
    def __init__(self, *args, **kwargs):
        super(AdherentAdminForm, self).__init__(*args, **kwargs)
        self.fields['lien_foyer'].required = False
        self.fields['lien_foyer'].widget = LinkWidget()
    class Meta:
        model = Adherent

class PersonneAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'partenaire','email')
    filter_horizontal = ('listes',)
    list_filter = ('partenaire',)
    search_fields = ['nom','prenom','email']
    def save_model(self, request, obj, form, change):
        #prev = obj.listes.values_list('id',flat=True)
        if change:
            prev = obj.listes.all()
            new = form.cleaned_data['listes']
            #print prev,new
            for liste in prev :
                if liste not in new :
                    liste.unsubscribe(form.cleaned_data['email'])
                    print "desinscription de %s de la liste %s" % (form.cleaned_data['email'],liste.name)
            for liste in new :
                if form.cleaned_data['email'] == '':
                    raise forms.ValidationError("Pour inscrire une personne sur une liste, l'e-mail doit etre valide.")
                if liste not in prev :
                    print "inscription de %s (%s %s) sur %s" % (form.cleaned_data['email'],to_ascii(form.cleaned_data['prenom']), to_ascii(form.cleaned_data['nom']), liste.name)
                    liste.subscribe(    form.cleaned_data['email'],
                                        to_ascii(form.cleaned_data['prenom']),
                                        to_ascii(form.cleaned_data['nom']))
        super(PersonneAdmin, self).save_model(request, obj, form, change)
admin.site.register(Personne,PersonneAdmin)



class AdherentAdmin(PersonneAdmin,ModelLinkAdminFields, FkAutocompleteAdmin):
    #form = AdherentAdminForm
    modellink = ('foyer',)
    list_display = ('nom','prenom','nb_enfants','telephone','mobile','email','commune')
    list_filter = ('annee_scolaire',)
    search_fields = ['nom','prenom','email','cfoyer','adhesion_id']
    related_search_fields = {  'commune': ('nom','maj','code_postal'), }
    inlines = [EngagementInline,]
    filter_horizontal = ('listes','conseil_local')
    fieldsets = (
        (None, {
            'fields': (('nom', 'prenom'), ('telephone', 'mobile'),'email','foyer','listes')
        }),
        ('Infos partenaires', {
            'classes': ('collapse',),
            'fields': ('partenaire','organisation', 'role', )
        }),

    )
    def save_model(self, request, obj, form, change):
        #prev = obj.listes.values_list('id',flat=True)
        if change:
            prev = obj.listes.all()
            new = form.cleaned_data['listes']
            #print prev,new
            for liste in prev :
                if liste not in new :
                    liste.unsubscribe(form.cleaned_data['email'])
                    print "desinscription de %s de la liste %s" % (form.cleaned_data['email'],liste.name)
            for liste in new :
                if form.cleaned_data['email'] == '':
                    raise forms.ValidationError("Pour inscrire une personne sur une liste, l'e-mail doit etre valide.")
                if liste not in prev :
                    print "inscription de %s (%s %s) sur %s" % (form.cleaned_data['email'],to_ascii(form.cleaned_data['prenom']), to_ascii(form.cleaned_data['nom']), liste.name)
                    liste.subscribe(    form.cleaned_data['email'],
                                        to_ascii(form.cleaned_data['prenom']),
                                        to_ascii(form.cleaned_data['nom']))
        super(AdherentAdmin, self).save_model(request, obj, form, change)
admin.site.register(Adherent,AdherentAdmin)

class EtabAdmin(FkAutocompleteAdmin):
    list_display = ('nom','code','perimetre','code_postal','commune')
    search_fields = ['nom','commune__nom','commune__code_postal']
    related_search_fields = {  'commune': ('nom','maj','code_postal'), }
admin.site.register(Etablissement, EtabAdmin)

admin.site.register(Classe)
admin.site.register(Role)
admin.site.register(AnneeScolaire)



from coop_cms.admin import ArticleAdmin
from coop_cms.settings import get_article_class

class ArticleFCPE(ArticleAdmin):
    list_filter = ('tags',)
    fieldsets = (
        #('Arborescence', {'fields': ('navigation_parent',)}),
        ('Contenu', {'fields': ('title', 'content','tags',('publication','template'),'logo')}),
    )
admin.site.unregister(get_article_class())
admin.site.register(get_article_class(), ArticleFCPE)

