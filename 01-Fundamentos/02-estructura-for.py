# Range -> Genera un objeto iterable -> [ ]

# Minimo tenemos que pasarle un dato entero

mi_rango = range(3) # [0, 1, 2]
mi_rango = range(5) # [0, 1, 2, 3, 4]

print(mi_rango) # -> range(0, 5)
print(list(mi_rango)) # -> [0, 1, 2, 3, 4]


# Sintaxis For

for i in range(5):
    print(i)
    # 0
    # 1
    # 2
    # 3
    # 4
    
lista = ["Val", "Nati", "Fede"]

for nombre in lista:
    print(nombre)
    
print('----------------------------------------------------------------')

for j in range(3, 10): # incluyendo - excluyendo
    print(j)

print('----------------------------------------------------------------')

for k in range(5, 15, 2): # desde, hasta, pasos
    print(k)

print('----------------------------------------------------------------')

for k in range(15, 5, -1): # desde, hasta, pasos
    print(k)
    
print('----------------------------------------------------------------')

for i in range(15):
    if i % 2 == 0:
        print(i)

print('----------------------------------------------------------------')

lista_numero = range(10, 20, 2)
print(lista_numero)
lista_numero = list(range(10, 20, 2))
print(lista_numero)