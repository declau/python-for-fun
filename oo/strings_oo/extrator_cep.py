endereco = "Rua dos Bobos 00, apartamento 00, Lugar Nenhum, Poços de Caldas, MG, 37707000"

import re # Regular Expression

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
busca = padrao.search(endereco) # Match

if busca:
    cep = busca.group()
    print(cep)
