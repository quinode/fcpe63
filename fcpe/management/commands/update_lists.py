# -*- coding:utf-8 -*-

from django.core.management.base import BaseCommand
from fcpe.models import Personne, Adherent, ConseilLocal
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
        for a in adherents:
            if lists['adherents'] not in t.listes.all() and not t.optout:
                lists['adherents'].subscribe(t.email, to_ascii(t.prenom), to_ascii(t.nom))
                t.listes.add(lists['adherents'])
        