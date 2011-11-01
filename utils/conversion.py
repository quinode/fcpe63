all = Adherent.objects.all()
err = set()
for a in all:
    vq = Commune.objects.filter(maj=a._ville)
    if vq.exists():
        pass
        #print 'OK!',vq[0].maj,a._ville
    else:
        err.add(a._ville)

        
for a in all:
    vq = Commune.objects.filter(maj=a._ville)
    if vq.exists():
        a.commune = vq[0]
        a.save()


for a in all:
    if a._ville.startswith('ST '):
        new = a._ville.replace('ST ','SAINT ')
        a._ville = new
        a.save()
    if a._ville.startswith('STE '):
        new = a._ville.replace('STE ','SAINTE ')
        a._ville = new
        a.save()    
        

for a in all:
    if ' STE ' in a._ville:
        new = a._ville.replace(' STE ',' SAINTE ')
        a._ville = new
        a.save()
        
        
        
##### recoller les conseils locaux

all = Adherent.objects.all()
err = set()
for a in all:
    vq = ConseilLocal.objects.filter(nom=a._cl)
    if vq.exists():
        pass
        #print 'OK!',vq[0].maj,a._ville
    else:
        err.add(a._cl)
  
  
e

for a in all:
    vq = ConseilLocal.objects.filter(nom=a._cl)
    if vq.exists():
        a.conseil_local = vq[0]
        a.save()
     