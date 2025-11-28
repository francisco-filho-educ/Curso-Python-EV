# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 08:36:15 2025

@author: francisco.silveira
"""
class Main:
    pass # usar pass quando a classe não tiver estrutura
print("Teste de projeto")
from Cliente import Cliente
from Conta import Conta
c1 = Cliente('Lucrécio Bastos', '85-9.5568.6696') #
conta =Conta(4455, c1.get_nome(), 0)

#conta.deposita(1500)
#conta.saque(1600)# valor acima do saldo
#conta.saque(600)
#conta.extrato()

#print(c1)
#print('Nome', c1.nome,'\nTelefone:',c1.telefone)
#print('Titular: ',conta.titular,'\nNúmero: ',conta.numero,'\nSaldo R$',conta.saldo)
