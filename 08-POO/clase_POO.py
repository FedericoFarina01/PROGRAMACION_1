class Persona: #UpperCamelCase
    #Constructor
    #Atributos (características): altura, peso, nombre

    def __init__(self, altura:int, peso:int, nombre:str, apellido:str, edad:int, documento_unico:int, fecha_nac:str, genero:str):
        self.altura = altura # Público
        self._peso = peso # Protegido
        self.__nombre = nombre # Privados
        self.apellido = apellido
        self.edad = edad
        self.DNI = documento_unico
        self.estado_activo = True
        self.genero = genero


    #Métodos (comportamiento):
    def mostar_nombre(self):
        return self.__nombre


    def modificar_nombre(self, nombre:str):
        self.__nombre = nombre


    def get_edad(self):
        self.fecha_nac
        # Fecha de hoy
        # Lógica que calcula la edad
        # return edad        

persona_a = Persona(100, 90, "Val", "Pavlov", 35, 12345678, "M") # __init__()

persona_b = Persona(160, 80, "Sofia", "Perez", 40, 87654321, "F") # __init__()

print(f"Mi nombre y genero es: {persona_a.mostar_nombre()}, {persona_a.genero}")
persona_a.modificar_nombre("Pepe")

#persona_a.nombre = "Valeriy"
print(f"Mi nombre y genero es: {persona_a.mostar_nombre()}, {persona_a.genero}")


