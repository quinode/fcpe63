# -*- coding:utf-8 -*-
from django.db import models
from communes.models import Commune
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from django.contrib.gis.db import models as geomodels


class AnneeScolaire(models.Model):
    libelle = models.CharField(blank=True, max_length=100)

    def __unicode__(self):
        return self.libelle

    class Meta:
        verbose_name = "Année scolaire"
        verbose_name_plural = "Années scolaires"


class ConseilLocal(geomodels.Model):
    nom = models.CharField(blank=True, max_length=100)
    code = models.CharField(blank=True, max_length=9, unique=True)
    adr1 = models.CharField(blank=True, max_length=100)
    adr2 = models.CharField(blank=True, max_length=100)
    commune = models.ForeignKey(Commune)
    _cp = models.CharField(blank=True, max_length=5, editable=False)
    _ville = models.CharField(blank=True, max_length=100, editable=False)
    primaire = models.BooleanField(default=False)
    secondaire = models.BooleanField(default=False)

    location = geomodels.PointField(verbose_name="localisation", blank=True, null=True, srid=4326)
    objects = geomodels.GeoManager()

    def code_postal(self):
        return self.commune.code_postal

    def nb_adherents(self):
        return self.adhesions.count()

    def responsables(self):
        resp = []
        membre = Role.objects.get(libelle="Membre")
        for a in self.adhesions.all():
            if a.role != membre:
                resp.append(a)
        return resp

    def __unicode__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('fcpe_fiche_conseil', args=[self.code])

    class Meta:
        verbose_name = "Conseil Local"
        verbose_name_plural = "Conseil Locaux"


class Etablissement(models.Model):
    nom = models.CharField(blank=True, max_length=100)
    code = models.CharField(blank=True, max_length=8, unique=True, verbose_name="Code FCPE")
    adr1 = models.CharField(blank=True, max_length=100, verbose_name="Adresse")
    adr2 = models.CharField(blank=True, max_length=100, verbose_name="Adresse")
    commune = models.ForeignKey(Commune, null=True)
    perimetre = models.ForeignKey(ConseilLocal)
    _cp = models.CharField(blank=True, max_length=5, editable=False)
    _ville = models.CharField(blank=True, max_length=100, editable=False)

    def code_postal(self):
        return self.commune.code_postal

    def __unicode__(self):
        return self.nom


class Classe(models.Model):
    libelle = models.CharField(max_length=100)

    def __unicode__(self):
        return self.libelle

from django_mailman.models import List


class Personne(models.Model):
    nom = models.CharField(blank=True, max_length=100)
    prenom = models.CharField(blank=True, max_length=100)
    organisation = models.CharField(blank=True, max_length=100)
    role = models.CharField(blank=True, max_length=100)
    email = models.EmailField(blank=True)
    partenaire = models.BooleanField(default=False)
    listes = models.ManyToManyField(List, blank=True, null=True)
    optout = models.BooleanField(default=False, verbose_name="Désinscription des listes")

    def __unicode__(self):
        return self.prenom + u' ' + self.nom

    def clean(self):
        if(self.email == None):
            raise ValidationError(u'La personne doit avoir un email pour être inscrit sur une liste')


class Role(models.Model):
    libelle = models.CharField(blank=True, max_length=100)

    def __unicode__(self):
        return self.libelle

    class Meta:
        verbose_name = "Rôle"
        verbose_name_plural = "Rôles"


class Foyer(models.Model):
    adr1 = models.CharField(blank=True, max_length=100, verbose_name="Adresse")
    adr2 = models.CharField(blank=True, max_length=100, verbose_name="Adresse")
    commune = models.ForeignKey(Commune, null=True)
    adhesion_id = models.IntegerField(blank=True, null=True, unique=True, verbose_name="ID Norma")
    annee_scolaire = models.ForeignKey(AnneeScolaire, blank=True, null=True)
    code_foyer = models.CharField(blank=True, max_length=11, verbose_name="Code Foyer")

    def code_postal(self):
        return self.commune.code_postal

    def __unicode__(self):
        if not self.code_foyer:
            return u'Foyer %s (code foyer FCPE manquant, à renseigner!)' % self.pk
        else:
            return u'Foyer FCPE ' + self.code_foyer

    def nb_enfants(self):
        return self.famille.count()

    def nom_adherent1(self):
        return self.rattachement.all()[0]


class Adherent(Personne):
    adr1 = models.CharField(blank=True, max_length=100, verbose_name="Adresse", editable=False)
    adr2 = models.CharField(blank=True, max_length=100, verbose_name="Adresse", editable=False)
    commune = models.ForeignKey(Commune, null=True, editable=False)
    telephone = models.CharField(blank=True, max_length=100)
    mobile = models.CharField(blank=True, max_length=100)
    adhesion_id = models.IntegerField(blank=True, null=True, unique=True, verbose_name="ID Norma", editable=False)  # A VIRER
    annee_scolaire = models.ForeignKey(AnneeScolaire, blank=True, null=True, editable=False)  # A VIRER
    _cp = models.CharField(blank=True, max_length=5, editable=False)  # A VIRER
    _ville = models.CharField(blank=True, max_length=100, editable=False)  # A VIRER
    _cl = models.CharField(blank=True, max_length=100, editable=False)  # A VIRER
    cfoyer = models.CharField(blank=True, max_length=11, verbose_name="Code Foyer")  # A VIRER
    conseil_local = models.ManyToManyField(ConseilLocal, through='Engagement')
    foyer = models.ForeignKey(Foyer, blank=True, null=True, related_name='rattachement')
    #user = models.ForeignKey(User, blank=True, null=True, unique=True)

    class Meta:
        verbose_name = "Adhérent"
        verbose_name_plural = "Adhérents"

    def lien_foyer(self):
        return '<a href="%s">%s</a>' % (
                             reverse('admin:fcpe_foyer_change', (self.foyer.id,)),
                             'Voir la fiche du foyer'
                     )

    def code_postal(self):
        return self.foyer.commune.code_postal

    def nb_enfants(self):
        return self.foyer.famille.count()

    def create_user(self):
        from random import Random
        rng = Random()
        righthand = '23456qwertasdfgzxcvbQWERTASDFGZXCVB'
        passwordLength = 8
        password = ''
        for i in range(passwordLength):
            password = password + rng.choice(righthand)
        username = self.nom.replace(' ', '').lower()
        user = User.objects.create_user(username, self.email, password)
        user.last_name = self.nom
        user.save()
        self.user = user
        self.save()
        return([username, password])


class Enfant(models.Model):
    nom = models.CharField(blank=True, max_length=100)
    prenom = models.CharField(blank=True, max_length=100)
    etablissement = models.ForeignKey(Etablissement)
    classe = models.ForeignKey(Classe)
    id_classe_norma = models.IntegerField(blank=True, null=True, editable=False)
    cfoyer = models.ForeignKey(Foyer, related_name='famille')

    def __unicode__(self):
        return unicode(self.prenom) + u' ' + unicode(self.nom) + u' (' + self.classe.__unicode__() + u')'


class Engagement(models.Model):
    adherent = models.ForeignKey(Adherent)
    conseil_local = models.ForeignKey(ConseilLocal, related_name='adhesions')
    adhesion_primaire = models.BooleanField(default=True)
    role = models.ForeignKey(Role, default='8')

    class Meta:
        verbose_name = "Adhésion"
        verbose_name_plural = "Adhésions"
        ordering = ['role']

    def __unicode__(self):
        return self.role.__unicode__() + u' du Conseil local ' + self.conseil_local.__unicode__()

#from taggit.managers import TaggableManager
from taggit_autocomplete_modified.managers import TaggableManagerAutocomplete as TaggableManager
from coop_cms.models import BaseArticle
from django.contrib.auth.models import User


class Article(BaseArticle):
    author = models.ForeignKey(User, blank=True, default=None, null=True)
    #template = models.CharField(_(u'template'), max_length=200, blank=True, default='fcpe_article.html')

    tags = TaggableManager(blank=True)

    def can_publish_article(self, user):
        return (self.author == user)

    def can_view_article(self, user):
        if self.publication != BaseArticle.PUBLISHED:
            return self.can_edit_article(user)
        else:
            return True

    #def can_edit_article(self, user):
    #    return True
    #

Article._meta.get_field('template').default = 'fcpe_article.html'


from django.contrib.admin.filterspecs import FilterSpec, RelatedFilterSpec
from django.contrib.admin.util import get_model_from_relation
from django.db.models import Count


class TaggitFilterSpec(RelatedFilterSpec):
    """
    A FilterSpec that can be used to filter by taggit tags in the admin.

    To use, simply import this module (for example in `models.py`), and add the
    name of your :class:`taggit.managers.TaggableManager` field in the
    :attr:`list_filter` attribute of your :class:`django.contrib.ModelAdmin`
    class.
    """

    def __init__(self, f, request, params, model, model_admin,
                 field_path=None):
        super(RelatedFilterSpec, self).__init__(
            f, request, params, model, model_admin, field_path=field_path)

        other_model = get_model_from_relation(f)
        if isinstance(f, (models.ManyToManyField,
                          models.related.RelatedObject)):
            # no direct field on this model, get name from other model
            self.lookup_title = other_model._meta.verbose_name
        else:
            self.lookup_title = f.verbose_name # use field name
        rel_name = other_model._meta.pk.name
        self.lookup_kwarg = '%s__%s__exact' % (self.field_path, rel_name)
        self.lookup_kwarg_isnull = '%s__isnull' % (self.field_path)
        self.lookup_val = request.GET.get(self.lookup_kwarg, None)
        self.lookup_val_isnull = request.GET.get(
                                      self.lookup_kwarg_isnull, None)
        # Get tags and their count
        through_opts = f.through._meta
        count_field = ("%s_%s_items" % (through_opts.app_label,
                through_opts.object_name)).lower()
        queryset = getattr(f.model, f.name).all()
        queryset = queryset.annotate(num_times=Count(count_field))
        queryset = queryset.order_by("-num_times")
        self.lookup_choices = [(t.pk, "%s (%s)" % (t.name, t.num_times))
                for t in queryset]


# HACK: we insert the filter at the beginning of the list to avoid the manager
# to be picked as a RelatedFilterSpec
FilterSpec.filter_specs.insert(0, (lambda f: isinstance(f, TaggableManager),
    TaggitFilterSpec))
