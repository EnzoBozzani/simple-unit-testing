import math

class Calculadora:
    def __init__(self):
        self.historico = []
        self.resultado = 0
    
    # Novo método de validação com validação de bool
    def _validar_operandos(self, *args):
        for valor in args:
            if not isinstance(valor, (int, float)):
                raise TypeError("Argumentos devem ser numeros")
            if isinstance(valor, bool):
                raise TypeError("Argumentos devem ser numeros (por mais que bool seja considerado instância de int, não é valido)")

    def somar(self, a, b):
        self._validar_operandos(a, b)
        
        resultado = a + b

        self.historico.append(f"{a} + {b} = {resultado}")

        self.resultado = resultado

        return resultado

    def subtrair(self, a, b):
        self._validar_operandos(a, b)
        
        resultado = a - b

        self.historico.append(f"{a} - {b} = {resultado}")

        self.resultado = resultado

        return resultado

    def multiplicar(self, a, b):
        self._validar_operandos(a, b)
        
        resultado = a * b

        self.historico.append(f"{a} * {b} = {resultado}")

        self.resultado = resultado

        return resultado

    def dividir(self, a, b):
        self._validar_operandos(a, b)
        
        if b == 0:
            raise ValueError("Divisao por zero nao permitida")
        
        resultado = a / b

        self.historico.append(f"{a} / {b} = {resultado}")

        self.resultado = resultado

        return resultado

    def potencia(self, base, expoente):
        self._validar_operandos(base, expoente)
        
        resultado = base ** expoente

        self.historico.append(f"{base} ^ {expoente} = {resultado}")

        self.resultado = resultado

        return resultado

    def limpar_historico(self):
        self.historico.clear()

    def obter_ultimo_resultado(self):
        return self.resultado
