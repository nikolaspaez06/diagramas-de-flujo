class Boock:
    def __init__(self,title,price,author):
        self.__title = title
        self.__price = price
        self.__author = author
   #
    def get_info(self):
        return f"\n Tiulo: {self.__title}\n precio: {self.__price}\n Autor: {self.__author}"
   # 
    def set_title(self,title):
        self.__title = title
   #
    def set_price(self,price):
        self.__price = price
    #
    def set_authot(self,author):
        self.__author = author
    #
    def get_title(self):
        return self.__title
    #
    def get_price(self):
        return self.__price
    #
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("El precio del libro no puede ser menor o igual a 0")
    #
    def get_author(self):
        return self.__author
    #
book1 = Boock("viaje al centro de la tierra","6.000" ,"julio berne")
book1.set_price(6000)
print(book1.get_info())
#------------inheritence--------------
class Comic(Boock):
    def __init__(self,title, price, author,num_page):
        super().__init__(title, price, author)
        self.num_page = num_page
    #
    def get_info(self):
         return (f"\n Tiulo: {self.get_title()}\n precio: {self.get_price()}\n Autor: {self.get_author()}\n numero de paginas: {self.num_page}")
    #
    def get_leer(self):
        return f"el comoc tiene {self.num_page} paginas "
    #


comic1 = Comic ("batman",5000,"pepito",30)
print (comic1.get_info())
print (comic1.get_leer())
    
