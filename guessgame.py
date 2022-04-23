tahmin = "makas"
tahmin_et = ""
tahmin_sayisi = 0 
tahmin_limiti = 3 
tahmin_bitti = False 

while tahmin != tahmin_et and not(tahmin_bitti) :
    if tahmin_sayisi < tahmin_limiti :
        tahmin_et = input("Tahmin giriniz : ")
        tahmin_sayisi +=1 
    else :
        tahmin_bitti = True 

if tahmin_bitti :
    print("Oyunu kaybettin! ")
else :
    print("Oyunu kazandin ! ")