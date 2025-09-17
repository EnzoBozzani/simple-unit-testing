import unittest
import sys

from src.calculadora import Calculadora

class TestInterface(unittest.TestCase):
    def test_entrada_saida_soma(self):
        calc = Calculadora()
        resultado = calc.somar(5, 3)
        self.assertEqual(resultado, 8)
        self.assertEqual(calc.obter_ultimo_resultado(), 8)

    def test_entrada_saida_subtracao(self):
        calc = Calculadora()
        resultado = calc.subtrair(5, 3)
        self.assertEqual(resultado, 2)
        self.assertEqual(calc.obter_ultimo_resultado(), 2)

    def test_entrada_saida_multiplicacao(self):
        calc = Calculadora()
        resultado = calc.multiplicar(5, 3)
        self.assertEqual(resultado, 15)
        self.assertEqual(calc.obter_ultimo_resultado(), 15)

    def test_entrada_saida_divisao(self):
        calc = Calculadora()
        resultado = calc.dividir(6, 3)
        self.assertEqual(resultado, 2)
        self.assertEqual(calc.obter_ultimo_resultado(), 2)

    # Teste adicional que verifica entrada-saída do método de potência
    def test_entrada_saida_potencia(self):
        calc = Calculadora()
        resultado = calc.potencia(3, 2)
        self.assertEqual(resultado, 9)
        self.assertEqual(calc.obter_ultimo_resultado(), 9)

    def test_tipagem_invalida(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar("5", 3) 
        with self.assertRaises(TypeError):
            calc.dividir(10, None)
        with self.assertRaises(TypeError):
            calc.subtrair([], 3)
        with self.assertRaises(TypeError):
            calc.multiplicar("88", 3)
        with self.assertRaises(TypeError):
            calc.potencia(3, {})

    # Teste adicional que verifica entrada booleana
    def test_tipagem_invalida_bool(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar(True, 3) 

    def test_consistencia_historico(self):
        calc = Calculadora()
        calc.somar(2, 3)
        calc.multiplicar(4, 5)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 + 3 = 5", calc.historico)
        self.assertIn("4 * 5 = 20", calc.historico)

    # Teste adicional que verifica se o histórico está vazio depois de ser limpo
    def test_consistencia_historico_vazio(self):
        calc = Calculadora()
        calc.multiplicar(4, 5)
        self.assertEqual(len(calc.historico), 1)
        self.assertIn("4 * 5 = 20", calc.historico)
        calc.limpar_historico()
        self.assertNotIn("4 * 5 = 20", calc.historico)
        self.assertEqual(len(calc.historico), 0)

    def test_inicializacao(self):
        calc = Calculadora()
        self.assertEqual(calc.resultado, 0)
        self.assertEqual(len(calc.historico), 0)

    # Teste adicional que verifica se os tipos são corretos após inicialização
    def test_inicializacao_tipos(self):
        calc = Calculadora()
        self.assertIsInstance(calc.resultado, int)
        self.assertIsInstance(calc.historico, list)
        self.assertEqual(calc.historico, [])

    def test_modificacao_historico(self):
        calc = Calculadora()
        calc.somar(1, 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)

    # Teste adicional que verifica se os dados são inseridos mesmo após o histórico ser limpo
    def test_modificacao_historico_reuso(self):
        calc = Calculadora()
        calc.somar(2, 2)
        calc.multiplicar(3, 3)
        self.assertEqual(len(calc.historico), 2)

        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)

        calc.subtrair(10, 5)
        self.assertEqual(len(calc.historico), 1)
        self.assertIn("10 - 5 = 5", calc.historico)

    def test_limite_inferior(self):
        calc = Calculadora()
        # Teste com zero
        resultado = calc.somar(0, 5)
        self.assertEqual(resultado, 5)
        # Teste com números negativos muito pequenos
        resultado = calc.multiplicar(-1e-10, 2)
        self.assertEqual(resultado, -2e-10)

    # Teste adicional que verifica operações com números muito próximos a zero
    def test_limite_inferior_proximo_zero(self):
        calc = Calculadora()
        resultado = calc.subtrair(1e-308, 1e-308)
        self.assertEqual(resultado, 0)

        resultado = calc.dividir(1e-308, 1)
        self.assertEqual(resultado, 1e-308)

    def test_limite_superior(self):
        calc = Calculadora()
        # Teste com números grandes
        resultado = calc.somar(1e10, 1e10)
        self.assertEqual(resultado, 2e10)

    # Teste adicional que teste potência com valores altos, levando a overflow
    def test_limite_superior_potencia(self):
        calc = Calculadora()
        max_float = sys.float_info.max
        
        with self.assertRaises(OverflowError):
            resultado = calc.potencia(max_float, 2)  

    def test_limite_superior_proximo_float_max(self):
        calc = Calculadora()
        max_float = sys.float_info.max

        resultado = calc.somar(max_float, max_float)
        self.assertTrue(resultado == float("inf"))

        resultado = calc.multiplicar(max_float, 2)
        self.assertTrue(resultado == float("inf"))

    def test_divisao_por_zero(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

    # Teste adicional de divisão de um número por float("inf"), que deve resultar em 0
    def test_valores_fora_intervalo_divisao_infinito(self):
        calc = Calculadora()
        resultado = calc.dividir(100, float("inf"))
        self.assertEqual(resultado, 0.0)

    def test_fluxos_divisao(self):
        calc = Calculadora()
        # Caminho normal
        resultado = calc.dividir(10, 2)
        self.assertEqual(resultado, 5)
        # Caminho de erro
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

    # Teste de caminho alternativo que testa potência com expoente 0
    def test_fluxos_potencia_expoente_zero(self):
        calc = Calculadora()
        # Caminho normal
        resultado = calc.potencia(10, 2)
        self.assertEqual(resultado, 100)
        # Caminho alternativo
        resultado = calc.potencia(999999, 0)
        self.assertEqual(resultado, 1)

    def test_mensagens_erro(self):
        calc = Calculadora()
        try:
            calc.dividir(5, 0)
        except ValueError as e:
            self.assertEqual(str(e), "Divisao por zero nao permitida")
    
    def test_mensagens_erro_tipagem_bool(self):
        calc = Calculadora()
        try:
            calc.somar(True, 5)
        except TypeError as e:
            self.assertEqual(str(e), "Argumentos devem ser numeros (por mais que bool seja considerado instância de int, não é valido)")

if __name__ == '__main__':
    unittest.main()