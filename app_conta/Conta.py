# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 09:50:22 2025

@author: francisco.silveira
"""
class Conta:
    def __init__(self, numero,titular,saldo ):
        """
        Método construtor. Inicializa a conta com o nome do titular e um saldo.
        O saldo inicial deve ser sempre positivo.
        """
        self._numero =  numero
        self._titular = titular
        self._saldo = 0
        
    #Métodos get
    def get_numero(self):
        return self._numero
    
    def get_titular(self):
        return self._titular
    @property
    def get_saldo(self):
        return self._saldo
    
    #Métodos set
    def set_numero(self,numero):
        self._numero = numero
    
    def set_titular(self,titular):
        self._titular = titular
        
    def set_saldo(self,saldo):
        if(saldo<0):
            print('O saldo não pode ser negativo')
        else: self._saldo = saldo
    
    def saque(self,valor):
        if(self._saldo>=valor):
            self._saldo-=valor
            print("Saque realizado com sucesso.")
        else:
            print('Saldo insuficiente')
    
    def deposita(self,valor):
        if(valor>=0):
            self._saldo+=valor
            print(f'R${valor} depositado com sucesso')
        else:
            print('O saldo não pode ser negativo')
    
    def extrato(self):
        print('Cliente: ', self._titular+'\nSaldo Atual: R$',self._saldo)
