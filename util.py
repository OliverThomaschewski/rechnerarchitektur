from math import floor

def directcache(anz, bytes, adress):
    """
        Cache Zugriffe und so
        :param anz: Anzahl der Blöcke
        :param bytes: Größe pro Block
        :param adress: Adresse
        :param num: Um verschiedene Caches zu unterscheiden, Cahce 1 = 1, Chache 2 = 2, usw
    """
    blockNum = floor(adress/bytes)
    blockIdx = blockNum%anz
    tag = floor(blockNum/anz)
    offset = adress % bytes

    print()
    print("Direct Mapping Cache")
    print("------------------------")
    print(f"Blocknummer: {blockNum}")
    print(f"Blockindex: {blockIdx}")
    print(f"Tag:{tag}")
    print(f"Offset: {offset}")
    print("(rechts nach links, Start bei 0)")


def multiwaycache(cacheBytes, blocksize, adress, way):
    """
    Berechnet werte für Multi Way Set-Associate Caches
    :param cacheBytes: Gesamtbytes des Caches
    :param blocksize: Byte pro Block
    :param adress: Die Byte Adresse
    :param way: Anzahl der Ways
    """

    anzBlocks = cacheBytes/blocksize
    anzSets = anzBlocks/way
    blockNum = floor(adress/blocksize)
    setIdx = blockNum % anzSets
    tag = floor(blockNum/anzSets)
    offset = adress % blocksize
        
    print()
    print(f"{way}-Way Cache")
    print("------------------------")
    print(f"Anzahl Blöcke: {anzBlocks}")
    print(f"Anzahl Sets: {anzSets}")
    print(f"Blocknummer: {blockNum}")
    print(f"Set Index:{setIdx}")
    print(f"Tag:{tag}")
    print(f"Offset: {offset}")
    print("(rechts nach links, Start bei 0)")

def backwards(srcIdx, srcTag, srcAnzSets,targetAnzSets):
    blockNr = srcIdx+srcTag*srcAnzSets
    idx = blockNr % targetAnzSets
    tag = floor(blockNr/targetAnzSets)

    
    print("\n Tag und Index für zurückschreiben")
    print(f"Blocknummer: {blockNr}")
    print (f"Index: {idx}")
    print(f"Tag: {tag}")
    
