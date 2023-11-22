# %%
from time import sleep

class Persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Altura: {self.altura} metros")

    def calcular_edad_en_dias(self):
        dias_por_anio = 365
        edad_en_dias = self.edad * dias_por_anio
        return edad_en_dias

# %%
# Crear una instancia de la clase Persona
persona1 = Persona(nombre="Enrique", edad=22, altura=1.74)

# Mostrar la información de la persona
persona1.mostrar_informacion()

# %%
# Calcular y mostrar la edad en días
edad_en_dias = persona1.calcular_edad_en_dias()
print(f"Edad en días: {edad_en_dias}")

# %%
# Dormir por 2 segundos para dar tiempo de leer la información
sleep(2)

# Modificar la información de la persona
persona1.nombre = "Enrique Alejandro"
persona1.edad = 24
persona1.altura = 1.78

# Mostrar la nueva información de la persona
persona1.mostrar_informacion()


