# Pytanie 9 - dla danego stringa x stwórz słownik
# przechowujący informację ile razy dana litera wystąpiła w stringu


x = "myszydokazujągdykotanieczują"

ile_liter = {}


for letter in x:
    if letter not in ile_liter.keys():
        ile_liter[letter] = 1
    else:
        ile_liter[letter] += 1
        
print(ile_liter)


# tak tez mozna
for letter in x:
    if letter not in ile_liter:
        ile_liter[letter] = 1
    else:
        ile_liter[letter] += 1
        
print(ile_liter)



S = {x:x+1 for x in range(10000) if x%23 == 0}


if 7430 in S.keys():
    print("True")
else:
    print("False")
    
print(True if 7430 in S.keys() else False)