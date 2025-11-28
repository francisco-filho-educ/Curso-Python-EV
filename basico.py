# -*- coding: utf-8 -*-
"""
Curso de Introdução
"""
# Crtl + Enter -> executa a célula ou todo o script
# F9 -> Executa a linha ou seleção
#Print ef
print('dsdsd'+'sdsdsd')
print( '2' + '2 = 4')
print('dsdsd','sdsdsd')

#MASCARA DE FORMATAÇÃO

codigo = 55
nome = 'Francisco'
salario = 12526.00
ativo  =True

print("Código: %d:\n...OK"%codigo)
print("Nome: %s\n:...OK"%nome)
print("Salário: %.2f\n:...OK"%salario)
print("aTIVO: %r\n:...OK"%ativo)

#Usando a f-string, mas atual
print(f"Código:{codigo}")
print(f"Código:{codigo}\nSalário: {salario}\nAtivo: {ativo}")

#ENTRADA DE DADOS

codigo = int(input("Digite o código de funcionário:")) #Inteiro
nome = input('Escreva o seu nome: ') #string
salario = float(input("Digite o salário em R$:"))#

print(f"Código: {codigo}\nNome: {nome}\nSalário: R${salario}\nAtivo: {ativo}")

#ESTRUTURAS DE DECISÃO:

#exemplo 1:
idade = int(input('Digite sua idade:'))
if idade>=18:
    print('Maior de idade')
elif idade<18 and idade>13:
    print('Adolescente')
else: 
    print('Criança')    
    

# Exemplo 2
a = int(input('Digite o valor de A'))
b = int(input('Digite o valor de B'))

if a < b :
    aux = b
    b = a
    a = aux 
print(f"O valor de A agora é {a}\nValor de B agora é{b}")


#ESTRUTURA DE REPETIÇÃO:

#for
print('Inteiros de 1 a 10:\n')
for num in range(1,9):
    print(num)


print('Números pares até 20:\n')
for num in range(2,22,2):
    print(num)

print('Inteiros de 9 a 1 (descrescente):\n')
for num in range(9,0,-1):
    print(num)

#while

qtd = 0
i = 0
valor = float(input('Digite o valor máximo da série: '))
while i <= valor:
    print(i)
    i = 1+i

#Gera uma sequencia de numeros e a média dessa sequencia.
import os
os.system('cls' if os.name == 'nt' else 'clear')
i = 1
soma = 0
valor = 0
print('Para INICIAR a sequencia digite um número positivo\nPara SAIR digite um número negativo')
while i >= 0:
    valor = float(input(f'Digite {i}º Valor:'))
    if(valor>=0):
        soma = valor+soma 
        i = i+1
    else: 
        print(f'Quantidade de valores:{i}\n')
        print('Total da soma:',soma,'\n')
        print('Média:',soma/i )
        i = valor
        

#FUNÇÕES ----------------

#Cálculo da média de notas

#funcao de cálculo:
def calcMedia(totalSoma,quantidade):
    return(totalSoma/quantidade)

#função de entrada
def executa():
    nota = 0
    totalSoma = 0
    print('Calculo da Média:')
    for i in range(1,5):
        nota = float(input(f"Digite a {i}º nota:"))
        totalSoma =totalSoma+nota
    return(calcMedia(totalSoma,4))
    
os.system('cls' if os.name == 'nt' else 'clear')
executa()    

# Funçoes com lambda

# nome_funcao = lambda variavel_1, variavel_2: variavel_2 operador variavel_1

soma = lambda a, b: b+a 
print(soma(1,3))


# MANIPUPAÇÃO DE TEXTO
#Função open:
import os
os.chdir(r'C:\Users\francisco.silveira\Documents\Projetos\Python\curso_bradesco')
print(os.getcwd())

open('file', mode='r', encoding=None)
# 'r'	Read — leitura (erro se o arquivo não existir)
# 'w'	Write — escrita (cria o arquivo e apaga conteúdo anterior)
# 'a'	Append — adiciona conteúdo ao final do arquivo
# 'x'	Exclusive creation — cria novo arquivo (erro se já existir)
# 'b'	Binary — abre em modo binário (ex: imagens, PDFs)
# 't'	Text — abre em modo texto (padrão)
# '+'	Read/Write — leitura e escrita juntas
#texto = "O poeta é um fingidor.\nFinge tão completamente\nQue chega a fingir que é dor\nA dor que deveras sente."

arquivo = open('poema.txt',mode= 'r', encoding='UTF-8')
texto = arquivo.read()
arquivo.close() # fechar o arquivo após a leitura
print(texto)

#outra forma de leitura (com with não é necessário o close())

with open('poema.txt',mode= 'r', encoding='UTF-8') as arquivo:
    texto = arquivo.read()
    print(texto)

#Leitura linha a linha
i = 1
with open(r"poema.txt", mode='r', encoding='utf-8') as arq:
    for linha in arq:
        print(i,'ª Linha: ')
        print(linha.strip())
        i =i+1


#Escrevendo um arquivo com open() e with

with open('saida.txt','w',encoding='UTF=8') as arq: #Se o arquivo existir, sera subescrevido, senã será criado
    arq.write('Esta será a 1ª Linha. ')
    arq.write('Continuando na 2ª Linha\n')
    arq.write('Esta será a 3ª linha.')
   

#Acrescentando uma linha:
with open('saida.txt','a',encoding='UTF=8') as arq: #Se o arquivo existir, sera subescrevido, senã será criado
    arq.write('Continuando a 3º linha.\n')
    arq.write('Esta será a 4º linha')
    
#Escrevendo com o write

# Entre aspas
 #Simples ou duplas
print('Escrevendo com aspas simples', "e duplas...")

#Três aspas - permite inserir várias linhas
print("""O poeta é um fingidor.
Finge tão completamente
Que chega a fingir que é dor
A dor que deveras sente.""")


#Função len() tamnho da string
nome = 'Nietzcher'
len(nome)



