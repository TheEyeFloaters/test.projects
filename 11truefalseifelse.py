is_erkek = False 
is_uzun = True

if is_erkek and not(is_uzun):
    print("Erkek ama uzun degil ")
elif not(is_erkek) and not(is_uzun):
    print("Erkek degil uzun degil ")
elif is_erkek and is_uzun:
    print("uzun bir erkek ")
else :
    print("Erkek degil ama uzun")
