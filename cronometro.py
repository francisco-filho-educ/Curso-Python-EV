import time 
import os

class Cronometro:
    def __init__(self,segundos=0,minutos=0,horas=0):
        self.segundos = segundos
        self.minutos = minutos
        self.horas = horas
    
    def __repr__(self):
        return f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}"
    
    def incremento(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1
            
    def start(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self)
            time.sleep(1)
            self.incremento()
 # Garante que um bloco de código só seja executado quando o arquivo for rodado diretamente, e não quando ele for importado como módulo em outro script.   
if __name__ == "__main__": 
    Cronometro_1 = Cronometro()
    Cronometro_1.start()