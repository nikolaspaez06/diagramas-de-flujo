class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
        
    def describir_genero(self):
        if self.genero == "M":
            print("Soy un hombre.")
        elif self.genero == "F":
            print("Soy una mujer.")
        elif  self.genero == "B":
            print("Soy una persona no binaria.")
         
persona1 = Persona("Juan", 30, "M") 
persona1.presentarse()  # Salida: Hola, mi nombre es Juan y tengo 30 años.
persona1.describir_genero()  # Salida: Soy un hombre.0

persona2 = Persona("maria",25,"F") 
persona2.presentarse()  # Salida: Hola, mi nombre es marui y tengo 25 años.
persona2.describir_genero()  # Salida: Soy un mujer.

#------------inheritence--------------
class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, universidad):
        super().__init__(nombre, edad, genero)
        self.universidad = universidad
        
    def estudiar(self):
        print(f"Estoy estudiando en la universidad {self.universidad}.")

estudiante1 = Estudiante("Ane", 20,"B" , "Universidad Nacional")
estudiante1.presentarse()  # Salida: Hola, mi nombre es Ana y tengo 20 años.
estudiante1.describir_genero()  # Salida: Soy una mujer.
estudiante1.estudiar()  # Salida: Estoy estudiando en la universidad Universidad Nacional.

