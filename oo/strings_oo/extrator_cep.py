endereco = "Rua dos Bobos 00, apartamento 00, Lugar Nenhum, Poços de Caldas, MG, 37707-000"

import re # Regular Expression

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) # Match

if busca:
    cep = busca.group()
    print(cep)
