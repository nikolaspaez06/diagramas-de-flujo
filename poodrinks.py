class Drinks:
    def __init__(self, tipo, color, price):
        self.__color = color
        self.__tipo = tipo
        self._price = price
    
    def get_info(self):
        return f"\n Tipo: {self.__tipo}\n Color: {self.__color}\n Precio: {self._price}"

    def set_type(self, new_type):
        self.__tipo = new_type
    
    def set_price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("El precio de la bebida no puede ser menor o igual a 0") 

    def set_color(self, color):
        self.__color = color
   
    def get_type(self):
        return self.__tipo

    def get_price(self):
        return self._price
    
    def get_color(self):
        return self.__color


drinks1 = Drinks("cafe", "negro", 1000)
drinks2 = Drinks("jugo de naranja", "naranja", 1000)


drinks1.set_price(0)

print(drinks1.get_info())
print(drinks2.get_info())

# ------------inheritance--------------

class Caliente(Drinks):
    def __init__(self, tipo, color, price, take):
        super().__init__(tipo, color, price)
        self.__take = take
    
    def get_info(self):
        return f"\n Tipo: {self.get_type()}\n Color: {self.get_color()}\n Precio: {self.get_price()} \n Temperatura: {self.__take}"
    
    def get_tomar(self):
        return f"El {self.get_type()} está muy {self.__take}"


caliente1 = Caliente("cafe", "negro", 5000, "caliente")
print(caliente1.get_info())
print(caliente1.get_tomar())
