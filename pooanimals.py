class Animals:
    def __init__(self,kind,respiration,birth):
        self.kind = kind
        self.respiration = respiration
        self.birth = birth
    def get_info(self):
        return f"\n Tipo: {self.kind}\n Respiracion: {self.respiration}\n Nacimiento: {self.birth}"
    def  get_kind(self, kind):
        self.__kind = kind
    def get_respration(self):
        self.__respiration = respiration
    
    def get_birth(self):
       self.__birth = birth 
    
    def get_kind(self):
        return self.kind

    def get_respration(self):
        return self.respiration
    
    def get_birth(self):
        return self.birth
   
   
    


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
       self.eat = eat

    def get_info(self):
        return f"\n Tipo: {self.kind}\n Respiracion: {self.respiration}\n Nacimiento: {self.birth}\n Comer: {self.eat}"
    def get_eat(self):
        return self__eat
    def get_comer(self):
        return f"la {self.kind} come {self.eat}"
   
 

    



bird1 = Bird ("paloma", "pulmonar",  "oviparo", "fruta")
print(bird1.get_info())
print(bird1.get_comer())
