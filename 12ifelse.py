def max_sayi(say1, say2, say3):
    if say1>=say2 and say1>=say3:
        return say1
    elif say2>=say1 and say2>=say3:
        return say2
    else:
        return say3

print(max_sayi(5,9,7))
