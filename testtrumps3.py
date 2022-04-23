from unittest import result


def ustel (a , b):
    sonuc = 1 
    for x in range (b):
        sonuc = sonuc * a 
    return sonuc 

print(ustel(4,5))