class Boock:
    def __init__(self,title,price,author):
        self.title = title
        self.price = price
        self.author = author
    def get_info(self):
        return f"\n Tiulo: {self.title}\n precio: {self.price}\n Autor: {self.author}"

    def get_title(self):
        return self.title

    def get_price(self):
        return self.price
    
    def set_price(self,new_price):
        if new_price >0:
           self.price = new_price
        else:
            print("el precio del libro no puede ser menor o igual a 0")
    
    def get_author(self):
        return self.autor

book1 = Boock("viaje al centro de la tierra","6.000" ,"julio berne")




book1.set_price(0)


print(book1.get_info())
#------------inheritence--------------
class Comic(Boock):
    def __init__(self,title, price, author,num_page):
        super().__init__(title, price, author)
        self.num_page = num_page
    
    def get_info(self):
         return f"\n Tiulo: {self.title}\n precio: {self.price}\n Autor: {self.author}\n numero de paginas: {self.num_page}"
    def get_leer(self):
        return(f"comoc tiene {self.num_page} paginas ")



comic1 = Comic ("batman",5000,"pepito",30)
print(comic1.get_info())
print(comic1.get_leer())
    
