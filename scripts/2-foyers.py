# -*- coding:utf-8 -*-

import csv
import logging
import pdb

logging.basicConfig(level=logging.ERROR)

# foyers_new = {}
# foyers_exi = {}
depts = ('63', '43', '15', '03', '42', '39')

rows = csv.reader(open('2012-fin/foyers.csv', 'rb'), delimiter=';')

from fcpe.models import Commune, AnneeScolaire, Foyer


def verify_foyer(row):
    com_found = False
    for dep in depts:
        try:
            com = Commune.objects.get(maj=row[1], code_postal__startswith=dep)
            com_found = True
            logging.info(u"Commune \"%s\" trouvée dans le département %s" % (row[1], dep))
            break
        except:
            logging.info(u"Commune \"%s\" non trouvée dans le département %s" % (row[1], dep))
            pass
    try:
        com = Commune.objects.get(maj=row[1])
        logging.info(u"Commune \"%s\" trouvée en France" % row[1])
        com_found = True
    except:
        pass
    if not com_found:
        logging.info(u"Commune \"%s\" non trouvée en France" % row[1])
    else:
        annee = AnneeScolaire.objects.get(id=row[2])
        f = Foyer.objects.filter(code_foyer=row[0])
        if f.exists():
            f[0].commune = com
            f[0].annee_scolaire = annee
            f[0].save()
            # foyers_exi[f[0].code_foyer] = f[0]
            logging.info(u"%s mis à jour" % unicode(f[0]))
        else:
            newf = Foyer(code_foyer=row[0], commune=com, annee_scolaire=annee)
            newf.save()
            # foyers_new[newf.code_foyer] = newf
            logging.info(u"%s créé" % unicode(f[0]))


for row in rows:
    verify_foyer(row)
