# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.localflavor.fr.forms import FRZipCodeField


class Commune(models.Model):
    insee = models.CharField(blank=True, max_length=5)
    nom = models.CharField(blank=True, max_length=100)
    maj = models.CharField(blank=True, max_length=100)
    code_postal = models.CharField(blank=True, max_length=5)
    latitude = models.CharField(blank=True, max_length=20)
    longitude = models.CharField(blank=True, max_length=20)
    def __unicode__(self):
        return self.nom+u' ('+self.code_postal+u')'
        
