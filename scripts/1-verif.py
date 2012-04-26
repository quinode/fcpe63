# -*- coding:utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)

import csv
from fcpe.models import Etablissement, ConseilLocal, Foyer, \
                Adherent, Personne, Engagement, Role

#verification
rows = csv.reader(open('2012/etablissements.csv', 'rb'), delimiter=';')
for row in rows:
    try:
        c = Etablissement.objects.get(id=row[0])
    except:
        logging.info("Etablissement \"%s\" absent" % row[0])


# preparation
rows = csv.reader(open('2012/conseils.csv', 'rb'), delimiter=';')
for row in rows:
    try:
        c = ConseilLocal.objects.get(nom=row[0])
    except:
        logging.info("Conseil Local \"%s\" absent " % row[0])



# adherents