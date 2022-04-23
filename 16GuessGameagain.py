kelime = "Makas"
tahmin = ""
tahmin_sayisi = 0 
tahmin_siniri = 3
tahmin_testi = True 

while tahmin != kelime and tahmin_testi :
    if tahmin_sayisi < tahmin_siniri :
        tahmin = input("Lutfen bir kelime giriniz : ")
        tahmin_sayisi +=1 
    else :
        tahmin_testi = False 
        
if not(tahmin_siniri):
    print("Tahmininiz Yanlis")
else :
    print("Tahmin dogru")
    