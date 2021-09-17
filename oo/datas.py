class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def formata_data(self):
        print(f"{self.__dia}/{self.__mes}/{self.__ano}")