'''
url = "https://www.butebank.com.br/cambio?moedaorige=real&moedaddino=dolar&valor=1500"

argumento = "moedaorigem=real"

subString = argumento[5:11]
print(subString)
'''
from extratorargumentosurl import ExtratorArgumentosUrl

url = "moedaorigem=real&moedadestino=dolar"

argumento = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = argumento.ExtraiArgumentos()
print(moedaDestino, moedaOrigem)




from extratorargumentosurl import ExtratorArgumentosUrl
url =  'https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=150'
cambio = ExtratorArgumentosUrl(url)
moedaOrigem,moedaDestino=cambio.retornaMoedas()
valor = cambio.retornaValor()
print(moedaOrigem,moedaDestino,valor)
#aqui ta tudo bem, teste agora o caso em que “moedaorigem=moedadestino”.
url ='https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=150'
cambio = ExtratorArgumentosUrl(url)
moedaOrigem,moedaDestino=cambio.retornaMoedas()
valor = cambio.retornaValor()
print(moedaOrigem,moedaDestino,valor)