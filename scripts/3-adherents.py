# -*- coding:utf-8 -*-

import csv
import logging
import pdb

logging.basicConfig(level=logging.ERROR)
from fcpe.models import ConseilLocal, Foyer, \
                Adherent, Personne, Engagement, Role

membre = Role.objects.get(id=8)

rows = csv.reader(open('2012-fin/adherents.csv', 'rb'), delimiter=';')


def verify_person(row):
    try:
        foyer = Foyer.objects.get(code_foyer=row[0])
    except Exception, e:
        logging.error(u'Aucun foyer trouvé avec le code "%s"' % row[0])
        raise e
    try:
        conseil = ConseilLocal.objects.get(nom=row[6])
    except Exception, e:
        logging.error(u'Aucun conseil local trouvé avec le nom "%s"' % row[0])
        raise e
    #pdb.set_trace()

    try:
        adh = Adherent.objects.get(nom__iexact=row[1].decode('utf-8'),
                                    prenom__iexact=row[2].decode('utf-8'), foyer=foyer)
        logging.info(u"Adhérent trouvé : %s %s" % (adh.nom, adh.prenom))
        if row[5] != '' and row[5] != adh.email:
            logging.info(u"Email mis à jour pour : %s %s" % (adh.nom, adh.prenom))
            adh.email = row[5]
        if row[3] != '' and row[3] != adh.telephone and len(adh.telephone) > 0:
            adh.telephone = row[3]
            logging.info(u"Telephone de %s %s mis à jour : %s" % (adh.nom, adh.prenom, row[3]))
        if row[4] != '' and row[4] != adh.mobile and len(adh.mobile) > 0:
            adh.mobile = row[4]
            logging.info(u"Mobile de %s %s mis à jour : %s" % (adh.nom, adh.prenom, row[4]))
        if adh.commune == None or adh.commune != foyer.commune:
            adh.commune = foyer.commune
            logging.info(u"Commune de %s %s mise à jour : %s" % (adh.nom, adh.prenom, foyer.commune))
        adh.prenom = adh.prenom.title()
        adh.save()
    except Adherent.DoesNotExist:
        adh = Adherent(foyer=foyer, nom=row[1].decode('utf-8'), prenom=row[2].decode('utf-8').title(), 
                        telephone=row[3], mobile=row[4], email=row[5], commune=foyer.commune)
        adh.save()
        logging.info(u"Nouvel adhérent(e) créé(e) : %s %s" % (adh.nom, adh.prenom))

    # les rôles ne sont pas mis à jour, et doivent l'être manuellement

    e, ecreated = Engagement.objects.get_or_create(adherent=adh, 
                                                  conseil_local=conseil,
                                                  defaults={'role': membre})
    if ecreated:
        logging.info(u"Engagement créé pour %s dans le conseil local %s" % (unicode(adh), conseil))
    else:
        logging.info(u"Engagement trouvé pour %s dans le conseil local %s" % (unicode(adh), conseil))


for row in rows:
    verify_person(row)
