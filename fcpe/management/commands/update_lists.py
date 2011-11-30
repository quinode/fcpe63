# -*- coding:utf-8 -*-

from django.core.management.base import BaseCommand
from fcpe.models import Personne, Adherent, ConseilLocal, Role
from django_mailman.models import List

import unicodedata
def to_ascii(input_str):
    nkfd_form = unicodedata.normalize('NFKD', unicode(input_str))
    only_ascii = nkfd_form.encode('ASCII', 'ignore')
    return only_ascii


class Command(BaseCommand):
    help = "Mise à jour mailing-listes"

    def handle(self, *args, **options):
        lists = {}
        for l in List.objects.all()[:30]:
            lists[l.name] = l
        tous = Personne.objects.exclude(email='')
        for t in tous:
            if lists['general'] not in t.listes.all() and not t.optout:
                lists['general'].subscribe(t.email, to_ascii(t.prenom), to_ascii(t.nom))
                t.listes.add(lists['general'])
        adherents = Adherent.objects.exclude(email='')
        for t in adherents:
            if lists['adherents'] not in t.listes.all() and not t.optout:
                lists['adherents'].subscribe(t.email, to_ascii(t.prenom), to_ascii(t.nom))
                t.listes.add(lists['adherents'])
        conseils = ConseilLocal.objects.exclude(primaire=False,secondaire=False)
        membre = Role.objects.get(libelle='Membre')
        for cl in conseils:
            if(cl.adhesions.all().count() > 0):
                for e in cl.adhesions.exclude(role=membre):
                    if cl.primaire and lists['responsables-clp'] not in e.listes.all() and not e.optout:
                        print 'primaire',cl,e
                        #lists['responsables-clp'].subscribe(e.email, to_ascii(e.prenom), to_ascii(e.nom))
                        #e.listes.add(lists['responsables-clp'])
                    if cl.secondaire and lists['responsables-cls'] not in e.listes.all() and not e.optout:
                        print 'secondaire',cl,e
                        #lists['responsables-cls'].subscribe(e.email, to_ascii(e.prenom), to_ascii(e.nom))
                        #e.listes.add(lists['responsables-cls'])
        