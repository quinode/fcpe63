# -*- coding:utf-8 -*-

import csv
import logging
import pdb

logging.basicConfig(level=logging.ERROR)
from fcpe.models import Enfant, Classe, Foyer, Etablissement

rows = csv.reader(open('2012-fin/enfants.csv', 'rb'), delimiter=';')


def verify_enfant(row):
    classe = Classe.objects.get(id=int(row[6]))
    try:
        foyer = Foyer.objects.get(code_foyer=row[0])
    except Exception, e:
        logging.error(u'Aucun foyer trouvé avec le code "%s"' % row[0])
        raise e
    try:
        ets = Etablissement.objects.get(id=row[5])
    except Exception, e:
        logging.error(u"Aucun établissement trouvé avec l'ID %s" % row[5])
        raise e
    #pdb.set_trace()

    e, ecreated = Enfant.objects.get_or_create(
                nom__iexact=row[2].decode('utf-8'), prenom__iexact=row[3].decode('utf-8'),
                cfoyer=foyer, defaults={'nom': row[2].decode('utf-8'), 
                                        'prenom': row[3].decode('utf-8').title(),
                                         'etablissement': ets, 'id_classe_norma': row[4], 
                                         'classe': classe})

    if not ecreated:
        e.id_classe_norma = row[4]
        e.classe = classe
        e.prenom = e.prenom.title()
        e.etablissement = ets
        e.save()
        logging.info(u"Enfant trouvé et mis à jour :  %s " % e)
    else:
        logging.info(u"Enfant créé : %s" % e)


for row in rows:
    verify_enfant(row)
