class Programa:
    def __init__(self, nome, ano,):
        self._nome = nome.title()
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
    
    @nome.setter
    def nome(self, novo_nome):
         self._nome = novo_nome

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._likes} Likes"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} Min - {self._likes} Likes"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
         return f"{self._nome} - {self.ano} - {self.temporadas} Temporadas - {self._likes} Likes"
    
class Playlist(list):
    def __init__(self, nome, programas):
        super().__init__(programas)
        self.nome = nome.title()
        self.programas = programas


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
mad_max = Filme("mad max - estrada da furia", 2016, 185)
atlanta = Serie("atlanta", 2019, 2)
justiceiro = Serie("justiceiro", 2019, 2)

vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
mad_max.dar_like()
mad_max.dar_like()
mad_max.dar_like()
mad_max.dar_like()
justiceiro.dar_like()


filmes_series = [vingadores, mad_max, atlanta, justiceiro]
playlist_fim_semana = Playlist("playlist fim de semana", filmes_series)

print( f"Quantidade de Filmes ou Series: {len(playlist_fim_semana)}")
for programa in playlist_fim_semana:
    print(programa)

print(f"Faz parte da Playlist? {justiceiro in playlist_fim_semana}")