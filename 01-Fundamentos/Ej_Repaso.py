
precio_barbijo_mas_caro = 0
mayor_fabricante = 0
cantidad_jabon = 0
mayor_cantidad_unidades = 0

for i in range(3):
    tipo_producto = input("Tenemos jabon, alcohol y barbijo\nIngresa el producto: ").lower()
    while tipo_producto != 'jabon' and tipo_producto != 'alcohol' and tipo_producto != 'barbijo':
        tipo_producto = input("ERROR | Ingresa un producto válido: ").lower()
    
    precio_producto = int(input('Ingresa el precio (100-300): '))
    while precio_producto < 100 or precio_producto > 300:
        precio_producto = int(input('ERROR | Ingresa un precio válido: '))
    
    cantidad_unidades = int(input('Ingresa la cantidad de unidades (1-1000): '))
    while cantidad_unidades < 1 or cantidad_unidades > 1000:
        cantidad_unidades = int(input('ERROR | Ingresa una cantidad válida: '))
    
    marca = input('Ingresa la marca: ')
    fabricante = input('Ingresa el fabricante:  ')
    
    # Punto A
    
    if precio_barbijo_mas_caro == 0 and tipo_producto == 'barbijo':
        precio_barbijo_mas_caro = precio_producto
        cantidad_barbijos_caros = cantidad_unidades
        fabricante_barbijos_caros = fabricante
    elif precio_barbijo_mas_caro < precio_producto and tipo_producto == 'barbijo':
        precio_barbijo_mas_caro = precio_producto
        cantidad_barbijos_caros = cantidad_unidades
        fabricante_barbijos_caros = fabricante
    
    # Punto B
    
    if mayor_cantidad_unidades == 0 and cantidad_unidades > mayor_fabricante:
        mayor_cantidad_unidades = cantidad_unidades
        mayor_fabricante = fabricante
    elif mayor_cantidad_unidades < cantidad_unidades:
        mayor_cantidad_unidades = cantidad_unidades
        mayor_fabricante = fabricante
        
    
    # Punto C
    
    if tipo_producto == 'jabon':
        cantidad_jabon += cantidad_unidades

    
if precio_barbijo_mas_caro == 0:
    print('No se ingreso barbijos')
else:
    print(f"El barbijo más caro tiene un stock de {cantidad_barbijos_caros} unidades y es fabricado por {fabricante_barbijos_caros}")

print(f"El item con mas unidades es: {mayor_fabricante} y es: {mayor_cantidad_unidades}")

print(f"La cantidad de jabones: {cantidad_jabon}")