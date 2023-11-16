character_name = "Zahid Hasan"

print(character_name.upper()) # ZAHID HASAN
print(character_name.lower()) # zahid hasan

print(character_name.isupper()) # false
print(character_name.islower()) # false

print(character_name.upper().isupper()) # true
print(character_name.lower().islower()) # true

print(len(character_name)) # 11
print(character_name[0]) # Z
print(character_name[10]) # n

print(character_name.index("Z")) # 0
print(character_name.index("Has")) # 6

print(character_name.replace("Hasan", "Ontor")) # Zahid Ontor
