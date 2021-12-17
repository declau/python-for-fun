class Cliente:
    def __init__(self, nome):
        self.__nome = nome  # Para usar o property o atributo tem que ser privado

    @property # Metodos que representam uma propriedade da classe
    def nome(self):
        print ("chamando @property nome()")
        return self.__nome.title()

    @nome.setter 
    def nome(self, nome):
        print ("chamando setter nome()")
        self.__nome = nome 