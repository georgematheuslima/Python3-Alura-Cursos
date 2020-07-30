import requests
class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError ("CEP Inválido")

    def __str__(self):
        return self.format_self()


    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False


    def format_self(self):
        return "{}-{}".format(self.cep[0:5], self.cep[5:])

    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        bairro = dados.get('bairro')
        cidade = dados.get('localidade')
        uf = dados.get('uf')
        return bairro, cidade, uf