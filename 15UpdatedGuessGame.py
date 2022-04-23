tahmin_kelime = "Amcik"
tahmin = ""
yapilan_tahmin = 0 
max_tahmin_sayisi = 3
tahmin_boole = False 

while tahmin != tahmin_kelime and not(tahmin_boole):
    if yapilan_tahmin < max_tahmin_sayisi:
        tahmin = input("Tahmininizi giriniz : ")
        yapilan_tahmin += 1
    else :
        tahmin_boole = True
        
if tahmin_boole :
    print("Kaybettiniz aminakodumun evladi ")
else : 
    print("Kazandiniz abi ")
    