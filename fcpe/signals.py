# -*- coding:utf-8 -*-

from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from fcpe.models import Personne
from django_mailman.models import List

#TODO : quand https://code.djangoproject.com/ticket/16073 sera corrigé...

#@receiver(m2m_changed)
def update_subscriptions(sender, **kwargs):
    if(sender == Personne.listes.through and kwargs["model"]==List):
        action = kwargs["action"]
        pk_set = kwargs["pk_set"]
        instance = kwargs["instance"]
        added = False
        print action,pk_set
        if(action == "pre_add"):
            before = instance.prev
            print instance,before
            added = True
            print "inscriptions", pk_set
            for liste in pk_set:
                if liste not in before :
                    print "inscription sur",liste
            for liste in before:
                if liste not in pk_set :
                    print "desincription de ",liste
        #if(not added and len(before) > 1): #pas d'ajout
        #    print "rien ajouté mais reste qqchose"
        
        
