# -*- coding:utf-8 -*-
from django.db import models
from communes.models import Commune
from django.contrib.localflavor.fr.forms import FRPhoneNumberField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class AnneeScolaire(models.Model):
    libelle = models.CharField(blank=True, max_length=100)
    def __unicode__(self):
        return self.libelle
    class Meta:
        verbose_name = "Année scolaire"
        verbose_name_plural = "Années scolaires"

class ConseilLocal(models.Model):
    nom = models.CharField(blank=True, max_length=100)
    code = models.CharField(blank=True, max_length=9,unique=True)
    adr1 = models.CharField(blank=True, max_length=100)
    adr2 = models.CharField(blank=True, max_length=100)
    commune = models.ForeignKey(Commune)
    _cp = models.CharField(blank=True, max_length=5, editable=False)
    _ville = models.CharField(blank=True, max_length=100, editable=False)
    def code_postal(self):
        return self.commune.code_postal
    def nb_adherents(self):
        return self.adhesions.count()
    def __unicode__(self):
         return self.nom
    class Meta:
        verbose_name = "Conseil Local"
        verbose_name_plural = "Conseil Locaux"
    

class Etablissement(models.Model):
    nom = models.CharField(blank=True, max_length=100)
    code = models.CharField(blank=True, max_length=8,unique=True, verbose_name="Code FCPE")
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
    listes = models.ManyToManyField(List,blank=True,null=True)
    def __unicode__(self):
        return self.prenom+u' '+self.nom
    def clean(self):
        if(self.email == None):
            raise ValidationError(u'La personne doit avoir un email pour être inscrit sur une liste')


class Role(models.Model):
    libelle = models.CharField(blank=True, max_length=100)
    def __unicode__(self):
        return self.libelle

class Adherent(Personne):
    adr1 = models.CharField(blank=True, max_length=100, verbose_name="Adresse")
    adr2 = models.CharField(blank=True, max_length=100, verbose_name="Adresse")
    commune = models.ForeignKey(Commune, null=True)
    telephone = models.CharField(blank=True, max_length=100)
    mobile = models.CharField(blank=True, max_length=100)
    adhesion_id = models.IntegerField(blank=True, null=True,unique=True, verbose_name="ID Norma")
    annee_scolaire = models.ForeignKey(AnneeScolaire)
    _cp = models.CharField(blank=True, max_length=5, editable=False)
    _ville = models.CharField(blank=True, max_length=100, editable=False)
    _cl =  models.CharField(blank=True, max_length=100, editable=False)
    cfoyer = models.CharField(blank=True, max_length=11,unique=True, verbose_name="Code Foyer")
    conseil_local = models.ManyToManyField(ConseilLocal,through='Engagement')
    #user = models.ForeignKey(User, blank=True, null=True, unique=True)
    class Meta:
        verbose_name = "Adhérent"
        verbose_name_plural = "Adhérents"
    def code_postal(self):
        return self.commune.code_postal
    def nb_enfants(self):
        return self.famille.count()    
    def create_user(self):
        from random import Random
        rng = Random()
        righthand = '23456qwertasdfgzxcvbQWERTASDFGZXCVB'
        passwordLength = 8
        password = ''
        for i in range(passwordLength):
            password = password + rng.choice(righthand)
        username = self.nom.replace(' ','').lower()
        user = User.objects.create_user(username,self.email,password )
        user.last_name = self.nom
        user.save()
        self.user = user
        self.save()
        return([username,password])

        


class Enfant(models.Model):
    nom = models.CharField(blank=True, max_length=100)
    prenom = models.CharField(blank=True, max_length=100)
    etablissement = models.ForeignKey(Etablissement)
    classe = models.ForeignKey(Classe)
    id_classe_norma = models.IntegerField(blank=True, null=True,editable=False)
    foyer = models.ForeignKey(Adherent,related_name='famille')
    def __unicode__(self):
         return self.prenom+u' '+self.nom+u' ('+self.classe.__unicode__()+u')'

class Engagement(models.Model):
    adherent = models.ForeignKey(Adherent)
    conseil_local = models.ForeignKey(ConseilLocal,related_name='adhesions')
    adhesion_primaire = models.BooleanField(default=True)
    role = models.ForeignKey(Role,default=Role.objects.get(libelle='Membre').id)
    class Meta:
        verbose_name = "Adhésion"
        verbose_name_plural = "Adhésions"
    def __unicode__(self):
        return u'Code foyer : '+self.adherent.cfoyer
        
        