url = "bytebank.com/cambio?moedaOrigem=real"
print(url)
#pega a base da url
url_base = url[0 : 19]
print(url_base, "URL base")

#pega somente os parametros da url
url_parametros = url[20:]
url_parametros = url[20:36]
print(url_parametros, "URL parametros")

#string no Python são imutáveis
print(url, "padrão")


# nova URL
nova_url = "http://bytebank.com/cambio?moedaOrigem=real"
#find retorna posição na string
indice_interrogacao = nova_url.find("?")
url_find = nova_url[0:indice_interrogacao]
print(url_find, "URL base find")

url_find_parametro = nova_url[indice_interrogacao+1:]
print(url_find_parametro, "URL parametro find")