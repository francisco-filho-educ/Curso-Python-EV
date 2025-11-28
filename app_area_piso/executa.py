from area import Retangulo
import math
import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Cálculo de azulejos necessários para cobrir um piso retangular.\n")
    print("Digite as dimensões do piso ou digite zero '0' para sair.")
    piso_a = float(input("Digite um lado do piso (em metros): "))
    if piso_a == 0:
        print("Encerrando o programa.")
        break
    piso_b = float(input("Digite o outro lado do piso (em metros): "))
    if piso_b == 0:
        print("Encerrando o programa.")
        break
  
    piso = Retangulo(piso_a, piso_b)

    az_a = float(input("Digite um lado do azulejo (em centímetros): "))
    az_b = float(input("Digite o outro lado do azulejo (em centímetros): "))   
    if az_a == 0 or az_b == 0:
        print("Encerrando o programa.")
        break
    azulejo = Retangulo(az_a, az_b)
    # Convertendo as dimensões do azulejo de centímetros para metros
    azulejo.muda_valores(az_a / 100, az_b / 100)

    area_piso = piso.calcula_area()
    area_azulejo = azulejo.calcula_area()

    qtd_azulejos = area_piso / area_azulejo

    if area_piso % area_azulejo == 0:
        print(f"A quantidade exata de azulejos é {qtd_azulejos}")
    else:
        print(f"A quantidade mínima de azulejos necessária é {math.ceil(qtd_azulejos)}")
    
    print("\nPressione Enter para continuar...")
    input()

