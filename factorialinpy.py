sayi = int(input("Lutfen bir sayi giriniz : "))
factorial = 1 
if (sayi < 0 ):
    print("Negatif faktorial")
elif (sayi<2):
    print("{}!={}".format(sayi,factorial))
else :
    for sayi in range(sayi ,1 ,-1):
        factorial = sayi*factorial
        
        print("{}".format(factorial))
