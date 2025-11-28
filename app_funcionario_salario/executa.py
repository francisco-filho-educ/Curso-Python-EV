from app_funcionario_salario.funcionario_salario_hora import Funcionario
  
func = Funcionario("João Silva", "joao.silva@example.com")

# Informando salário e horas trabalhadas no mês:
#janeiro:
func.cadastro_horas("Janeiro", 160)
func.cadastro_salario_hora("Janeiro", 25)
#fevereiro:
func.cadastro_horas("Fevereiro", 150)
func.cadastro_salario_hora("Fevereiro", 30)
#março:
func.cadastro_horas("Março", 170)
func.cadastro_salario_hora("Março", 28)
#Saida dos dados do funcionário e cálculo do salário de Janeiro:    
print(func) 
print("Salário de Janeiro:", func.calcular_salario("Janeiro"))
#Saída do cálculo do salário de Fevereiro:
print("Salário de Fevereiro:", func.calcular_salario("Fevereiro"))
#Saída do cálculo do salário de Março:
print("Salário de Março:", func.calcular_salario("Março"))