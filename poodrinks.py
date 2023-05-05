class Drinks:
    def __init__(self,tipo,color,price):
        self.color = color
        self.tipo = tipo
        self.price = price
    def get_info(self):
        return f"\n Tipo: {self.tipo}\n Color: {self.color}\n Precio: {self.price}"

    def get_type(self):
        return self.tipo

    def get_price(self):
       return self.price
    
    def set_price(self,new_price):
        if new_price >0:
           self.price = new_price
        else:
            print("el precio de la bebida no puede ser menor o igual a 0")
    
    def get_color(self):
        return self.color


drinks1 = Drinks("cafe","negro","1000")
drinks2 = Drinks("jugo de naranja","naranja","1000")


drinks1.set_price(0)


print(drinks1.get_info())
print(drinks2.get_info())

#------------inheritence--------------

class Caliente(Drinks):
    def __init__(self,tipo,color,price,take):
        super().__init__(tipo, color, price)
        self.take = take
    
    def get_info(self):
        return f"\n Tipo: {self.tipo}\n Color: {self.color}\n Precio: {self.price}\n temperatura: {self.take}"
    def  get_tomar(self):
        return( f"el {self.tipo} esta muy {self.take}")


caliente1 = Caliente("cafe", "negro" ,5000 ,"caliente")
print(caliente1.get_info())
print(caliente1.get_tomar())