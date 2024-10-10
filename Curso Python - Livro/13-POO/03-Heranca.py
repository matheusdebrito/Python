class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        return "Som genérico"

class Cachorro(Animal):
    def __init__(self, nome, raca):
        # Chamando o construtor da classe pai (Animal) com super()
        super().__init__(nome)
        self.raca = raca

    def latir(self):
        # Chamando o método da classe pai e estendendo a funcionalidade

        som_base = super().emitir_som()
        return f"{som_base}. O cachorro late!"

# Usando a classe Cachorro
dog = Cachorro("Rex", "Labrador")
print(dog.nome)          # Saída: Rex
print(dog.raca)          # Saída: Labrador
print(dog.latir())  # Saída: Som genérico. O cachorro late!
