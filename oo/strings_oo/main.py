url = "bytebank.com/cambio?moedaOrigem=real"
print(url)
#pega a base da url
url_base = url[0 : 19]
print(url_base)

#pega somente os parametros da url
url_parametros = url[20:]
url_parametros = url[20:36]
print(url_parametros)

#string no Python são imutáveis
print(url)