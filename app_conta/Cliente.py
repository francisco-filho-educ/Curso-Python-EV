# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 09:14:37 2025

@author: francisco.silveira
"""
#atributos de uma classe representam as características que ela possui.
class Cliente:
    def __init__(self, nome, fone):#define o construtor da classe obrigando ao programador determinar valores default no momento da inicialização do objeto.
    #Todo método Python tem self como primeiro parâmetro.
        #self.nome = n
        #self.telefone = fone
        #adicionando _ no inicio do atributo, restringe o acesso em outras classes (encapsulamento)
        self._nome = nome
        self._telefone = fone
        
    #Métodos get
    def get_nome(self):
        return self._nome
    
    def get_fone(self):
        return self._telefone
    
    #Métodos set 
    def set_nome(self,nome):
        self._nome = nome
        
    def set_fone(self,fone):
       self._telefone = fone