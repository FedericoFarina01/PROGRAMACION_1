# Break -> Permite romper una estructura repetitiva

print('---- Break ----')

for i in range(2):   
    for j in range(5): # [0, 1, 2, 3, 4]
        print(j)
        if j == 2:
            break # Sale de la estructura repetitiva más proxima
    print("Fin de la iteración externa")
    
print('---- Continue ----')

for i in range(5): # [0, 1, 2, 3, 4]
    if i == 2:
        continue # Salta a la siguiente iteración
    print(i) # 0 - 1 - 3 - 4