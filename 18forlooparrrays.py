def translate(phrase):
     translation = ""
     for harf in phrase:
          if harf.lower() in "aeiou":
               if harf.isupper():
                    translation = translation + "G"
               else:
                    translation = translation + "g"
          else:
               translation = translation + harf
     return translation
print(translate(input("Enter a phrase : ")))