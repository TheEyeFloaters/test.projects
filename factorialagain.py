sayi = int(input("Bir sayi giriniz :"))
ak = sayi  
fact = 1 
if (sayi < 0 ):
    print("Computer can not count ")
elif (sayi < 2):
    print("{}! = {} ".format(sayi,fact))
else :
    for sayi in range(sayi , 1 , -1):
        fact = fact * sayi
        
print("{}! = {}".format(ak , fact))