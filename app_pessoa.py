class Pessoa :
    "Isto é uma classe nova chamada Pessoa"
    idade = 15
    def saudacao(self):
        print ( 'Olá Pessoas!')


print("Executando a aplicação")
mateus =  Pessoa()
mateus.saudacao()
print('Idade:' + str(mateus.idade))
print("Fim da aplicação")