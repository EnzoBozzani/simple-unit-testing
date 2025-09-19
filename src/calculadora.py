import math
from typing import List, Tuple, Union

Number = Union[int, float]


class Calculadora:
    """Pequena calculadora com rastreamento de histórico e validações defensivas."""

    def __init__(self) -> None:
        self.historico: List[str] = []
        self.resultado: Number = 0

    def _validar_operandos(self, *args: Number) -> Tuple[Number, ...]:
        """Valida operandos garantindo tipos numéricos válidos e evitando valores indefinidos."""

        if not args:
            raise ValueError("Pelo menos um argumento deve ser informado")

        valores: List[Number] = []
        for valor in args:
            if isinstance(valor, bool):
                raise TypeError(
                    "Argumentos devem ser numeros (por mais que bool seja considerado instância de int, não é valido)"
                )
            if not isinstance(valor, (int, float)):
                raise TypeError("Argumentos devem ser numeros")
            if isinstance(valor, float) and math.isnan(valor):
                raise ValueError("Argumentos nao podem ser NaN")
            valores.append(valor)
        return tuple(valores)

    def _verificar_resultado(self, valor: Union[Number, complex]) -> Number:
        if isinstance(valor, complex):
            raise ValueError("Resultados complexos nao sao suportados")
        if isinstance(valor, float):
            if math.isnan(valor):
                raise ValueError("Resultado indefinido (NaN)")
            if math.isinf(valor):
                raise OverflowError("Resultado excede o limite representavel")
        return valor

    def _registrar_operacao(self, expressao: str, resultado: Number) -> Number:
        self.historico.append(expressao)
        self.resultado = resultado
        return resultado

    def somar(self, a: Number, b: Number) -> Number:
        a_validado, b_validado = self._validar_operandos(a, b)
        resultado = self._verificar_resultado(a_validado + b_validado)
        return self._registrar_operacao(f"{a_validado} + {b_validado} = {resultado}", resultado)

    def subtrair(self, a: Number, b: Number) -> Number:
        a_validado, b_validado = self._validar_operandos(a, b)
        resultado = self._verificar_resultado(a_validado - b_validado)
        return self._registrar_operacao(f"{a_validado} - {b_validado} = {resultado}", resultado)

    def multiplicar(self, a: Number, b: Number) -> Number:
        a_validado, b_validado = self._validar_operandos(a, b)
        resultado = self._verificar_resultado(a_validado * b_validado)
        return self._registrar_operacao(f"{a_validado} * {b_validado} = {resultado}", resultado)

    def dividir(self, a: Number, b: Number) -> Number:
        a_validado, b_validado = self._validar_operandos(a, b)
        if b_validado == 0:
            raise ValueError("Divisao por zero nao permitida")
        resultado = self._verificar_resultado(a_validado / b_validado)
        return self._registrar_operacao(f"{a_validado} / {b_validado} = {resultado}", resultado)

    def potencia(self, base: Number, expoente: Number) -> Number:
        base_validado, expoente_validado = self._validar_operandos(base, expoente)
        try:
            resultado = pow(base_validado, expoente_validado)
        except ZeroDivisionError as exc:
            raise ValueError("Potencia indefinida para base zero com expoente negativo") from exc
        except OverflowError as exc:
            raise OverflowError("Resultado da potencia excede o limite representavel") from exc
        resultado_verificado = self._verificar_resultado(resultado)
        return self._registrar_operacao(
            f"{base_validado} ^ {expoente_validado} = {resultado_verificado}",
            resultado_verificado,
        )

    def limpar_historico(self) -> None:
        self.historico.clear()
        self.resultado = 0

    def obter_ultimo_resultado(self) -> Number:
        return self.resultado
