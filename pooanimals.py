class Animals:
    def __init__(self,kind,respiration,birth):
        self.__kind = kind
        self.__respiration = respiration
        self.__birth = birth
   
    def get_info(self):
        return f"\n Tipo: {self.__kind}\n Respiracion: {self.__respiration}\n Nacimiento: {self.__birth}"
   
    def set_kind(self, kind):
        self.__kind = kind
   
    def set_respiration(self,respiration):
        self.__respiration = respiration
    
    def set_birth(self,birth):
        self.__birth = birth 
    
    def get_kind(self):
        return self.__kind

    def get_respration(self):
        return self.__respiration
    
    def get_birth(self):
        return self.__birth

    


animal1 = Animals ("leon","pulmonar","mamifero" )
animal2 = Animals ("pez payaso","branquial","oviparo")
animal3 = Animals ("gallina","pulmonar","oviparo")

print(animal1.get_info())
print(animal2.get_info())
print(animal3.get_info())
#------------inheritence--------------
class   Bird(Animals):
    def __init__(self,kind,respiration,birth,eat):
       super().__init__(kind,respiration,birth)
       self.__eat = eat

    def get_info(self):
        return f"{super().get_info()}\n Comer: {self.__eat}"
    
    def set_eat(self, eat):
        self.__eat = eat
    
    def get_eat(self):
        return self.__eat
 

    



bird1 = Bird ("paloma", "pulmonar",  "oviparo", "fruta")
print(bird1.get_info())
print(bird1.get_eat())
