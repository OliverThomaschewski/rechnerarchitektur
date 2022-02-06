from util import backwards, directcache, multiwaycache
"""
    Berechnet Adressen, Tags usw. von Speicherzugriffen

    Methoden:

    directcache(): Berechnungen für direct Cache
    multiwaycache(): Berechnungen für multiway cache
    backwards(): Berechnungen für zurückschreiben vpn Daten wenn die die "rausfliegen" als Valid markiert sind.

"""

a0 = 1000
a1 = 3040
a2 = 9196

anzBlocks1 = 32
blocksize1 = 16
adress1 = a0



print("\n Erster direct cache")
directcache(anzBlocks1, blocksize1, adress1)





# Second
print("\nZweite Ebene")
cacheBytes2 = 1024
blocksize2 = 8
adress2 = a1
way2 = 2

multiwaycache(cacheBytes2, blocksize2, adress2, way2)



