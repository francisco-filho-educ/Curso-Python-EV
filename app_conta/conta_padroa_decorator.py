# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 10:19:27 2025

@author: francisco.silveira
"""
# ==================================
# 1. Definição da Interface (IConta)
# ==================================
class IConta:
    """Interface (Abstrata) para todas as contas e decoradores."""
    def sacar(self, valor: float):
        raise NotImplementedError #sinalizar que um método (ou uma parte de uma função) deve ser implementado pelas subclasses ou por quem estiver utilizando a classe.
    def depositar(self, valor: float):
        raise NotImplementedError
    def verificar_saldo(self):
        raise NotImplementedError

# ==================================
# 2. Implementação do Componente Concreto (ContaBasica)
# ==================================
class ContaBasica(IConta):
    """Componente Concreto: A conta bancária original."""
    def __init__(self, titular: str, saldo: float = 0.0):
        self.titular = titular
        self._saldo = saldo
        print(f"Conta de {titular} criada com saldo de R$ {saldo:.2f}")

    def sacar(self, valor: float):
        if valor <= self._saldo:
            self._saldo -= valor
            print(f"    [Base] Saque de R$ {valor:.2f} realizado.")
            return True
        print(f"    [Base] Erro: Saldo insuficiente para sacar R$ {valor:.2f}.")
        return False

    def depositar(self, valor: float):
        self._saldo += valor
        print(f"    [Base] Depósito de R$ {valor:.2f} realizado.")

    def verificar_saldo(self):
        return self._saldo
    
# ==================================
# 3. Criação do Decorador Base (ContaDecorator)
# ==================================
class ContaDecorator(IConta):
    """Decorador Abstrato: Mantém uma referência ao objeto Conta."""
    def __init__(self, conta: IConta):
        self._conta = conta

    def sacar(self, valor: float):
        return self._conta.sacar(valor)

    def depositar(self, valor: float):
        self._conta.depositar(valor)

    def verificar_saldo(self):
        return self._conta.verificar_saldo()

#==================================
# 4. Criação dos Decoradores Concretos (TaxaSaqueDecorator, BonusDepositoDecorator)
# Poderia ser tipo uma conta especial, eu acrescento funcionalidades  
# as mudanças são aplicadas em tempo de execução
# ==================================
class TaxaSaqueDecorator(ContaDecorator):
    """Adiciona uma taxa de R$ 5.00 a cada saque."""
    def sacar(self, valor: float):
        TAXA = 5.00
        valor_total = valor + TAXA
        
        # 1. Adiciona o comportamento ANTES de chamar o objeto base
        if self._conta.verificar_saldo() < valor_total:
             print(f" [Deco] ERRO: Saque falhou. Saldo insuficiente para cobrir R$ {valor:.2f} + taxa de R$ {TAXA:.2f}.")
             return False

        print(f" [Deco] Aplicando taxa de R$ {TAXA:.2f} ao saque de R$ {valor:.2f}...")
        
        # 2. Chama a operação do objeto encapsulado (a ContaBasica)
        return self._conta.sacar(valor_total) # Saca valor + taxa


class BonusDepositoDecorator(ContaDecorator):
    """Adiciona um bônus de 1% sobre cada depósito."""
    def depositar(self, valor: float):
        BONUS_PERCENTUAL = 0.01  # 1%
        bonus = valor * BONUS_PERCENTUAL
        
        # 1. Chama a operação do objeto encapsulado (deposita o valor base)
        super().depositar(valor)
        
        # 2. Adiciona o comportamento DEPOIS da chamada base (deposita o bônus)
        self._conta._saldo += bonus
        print(f" [Deco] Bônus de depósito de R$ {bonus:.2f} adicionado.")
        
# ==================================
# 5. Demonstração de Uso
# ==================================        
    
# 1. Criação da Conta Básica
conta_joao = ContaBasica("João", saldo=500.00)
saldo_inicial = conta_joao.verificar_saldo()
print("-" * 30)


# 2. Adicionando DECORATORS (Comportamento em Tempo de Execução)
# Primeiro decora a conta básica com o Bônus
conta_decorada_bonus = BonusDepositoDecorator(conta_joao)

# Depois, decora o Bônus com a Taxa
conta_final = TaxaSaqueDecorator(conta_decorada_bonus)


# 3. Operações com a Conta Decorada
print("--- TESTE 1: DEPÓSITO COM BÔNUS ---")
conta_final.depositar(100.00)
# A chamada de depositar passará pelo BonusDepositoDecorator

print(f"Novo Saldo: R$ {conta_final.verificar_saldo():.2f}")
print("-" * 30)


print("--- TESTE 2: SAQUE COM TAXA ---")
# O saque passará pelo TaxaSaqueDecorator, que adiciona R$ 5.00
conta_final.sacar(50.00)
# Saque real na conta base é de R$ 55.00 (50.00 + 5.00)

print(f"Novo Saldo: R$ {conta_final.verificar_saldo():.2f}")
print("-" * 30)

# 4. Saque que falha devido à taxa
print("--- TESTE 3: SAQUE INSUFICIENTE (Taxa) ---")
# Saldo restante é R$ 556.00. Tentando sacar R$ 600.00 + R$ 5.00 = R$ 605.00
conta_final.sacar(600.00) 
print(f"Saldo Final: R$ {conta_final.verificar_saldo():.2f}")