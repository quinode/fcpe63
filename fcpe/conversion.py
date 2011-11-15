
from fcpe.models import Foyer,Adherent,Enfant

def cpfoyer():
    for a in Adherent.objects.all():
        f = Foyer(  adr1=a.adr1, adr2=a.adr2, commune=a.commune, 
                    adhesion_id=a.adhesion_id, 
                    annee_scolaire=a.annee_scolaire,
                    code_foyer=a.cfoyer)
        f.save()
        a.foyer = f
        a.save()


def enfants():
    for e in Enfant.objects.all():
        e.cfoyer = e.foyer.foyer
        e.save()              