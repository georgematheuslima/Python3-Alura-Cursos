import re

email1 = 'meu numero é 1234-5678'
email2 = 'Fale comigo em 1234-1234 esse é meu telefone'
email3 = '1234-1234 é o meu celular '

padrao = '[0123456789][0123456789][0123456789][0123456789]-[0123456789][0123456789][0123456789][0123456789]'

retorno = re.search(padrao, email1)
print(retorno.group())


padrao = "[0-9]{4}[-][0-9]{4}"
texto =  "Meu número para contato é 2633-5723"
retorno = re.search(padrao,texto)
print(retorno.group())