class Programa:
    def __init__(self, nome, ano,):
        self._nome = nome
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes
        
    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    
    @property
    def nome(self):
        return self._nome

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0
    

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0
    
    
vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()
print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Temporadas: {vingadores.duracao}"
        f" - Likes: {vingadores.likes}")

        
atlanta = Serie("atlanta", 2019, 2)
atlanta.dar_like()
atlanta.dar_like()
print(f"Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas}"
       f"- Likes: {atlanta.likes}")