lucky_numbers = [4,5,6,9,3]
dizi1=["Yunus", "Firat" ,"Firat" , "Dogukan"]
dizi1.insert(1, "Kelly")
dizi1.append("Ozan")
dizi1.extend(lucky_numbers)
dizi1.remove("Firat")
dizi1.pop()
print(dizi1)
print(dizi1.index("Ozan"))
print(dizi1.count("Firat"))
dizi2 = ["x","r","w","q","z"]
dizi2.sort()
print(dizi2)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
dizi3 = dizi1.copy()
print(dizi3)
