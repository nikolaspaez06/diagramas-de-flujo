class Animals:
    def __init__(self,kind,respiration,birth):
        self.kind = kind
        self.respiration = respiration
        self.birth = birth
    def get_info(self):
        return f"\n Tipo: {self.kind}\n Respiracion: {self.respiration}\n Nacimiento: {self.birth}"

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
class Insecto(Animals):
    def __init__(self,kind,respiration,birth,eat):
       super().__init__(kind,respiration,birth)
       self.eat = eat

    def get_info(self):
        return f"\n Tipo: {self.kind}\n Respiracion: {self.respiration}\n Nacimiento: {self.birth}\n Comer: {self.eat}"
    
    def get_comer(self):
        return f"la {self.kind} come {self.eat}"



insecto1 = Insecto("mosca", "traquial",  "oviparo", "fruta")
print(insecto1.get_info())
print(insecto1.get_comer())
