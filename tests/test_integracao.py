import unittest

from src.calculadora import Calculadora

class TestInterface(unittest.TestCase):
    def test_operacoes_sequenciais(self):
        calc = Calculadora()
        # Sequência: 2 + 3 = 5, depois 5 * 4 = 20, depois 20 / 2 = 10
        calc.somar(2, 3)
        resultado1 = calc.obter_ultimo_resultado()

        calc.multiplicar(resultado1, 4)
        resultado2 = calc.obter_ultimo_resultado()

        calc.dividir(resultado2, 2)
        resultado_final = calc.obter_ultimo_resultado()

        self.assertEqual(resultado_final, 10)
        self.assertEqual(len(calc.historico), 3)

    # Teste adicional de Operações Sequenciais, com potência no meio
    def test_operacoes_sequenciais_com_potencia(self):
        calc = Calculadora()
        # Sequência: (3 - 1 = 2), depois 2 ^ 3 = 8, depois 8 + 10 = 18, depois 18 / 3 = 6
        calc.subtrair(3, 1)
        resultado1 = calc.obter_ultimo_resultado()

        calc.potencia(resultado1, 3)
        resultado2 = calc.obter_ultimo_resultado()

        calc.somar(resultado2, 10)
        resultado3 = calc.obter_ultimo_resultado()

        calc.dividir(resultado3, 3)
        resultado_final = calc.obter_ultimo_resultado()

        self.assertEqual(resultado_final, 6)
        self.assertEqual(len(calc.historico), 4)
        self.assertIn("3 - 1 = 2", calc.historico)
        self.assertIn("2 ^ 3 = 8", calc.historico)
        self.assertIn("8 + 10 = 18", calc.historico)
        self.assertIn("18 / 3 = 6.0", calc.historico)

    def test_integracao_historico_resultado(self):
        calc = Calculadora()
        calc.potencia(2, 3)  # 2^3 = 8
        calc.somar(calc.obter_ultimo_resultado(), 2)  # 8 + 2 = 10

        self.assertEqual(calc.obter_ultimo_resultado(), 10)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 ^ 3 = 8", calc.historico)
        self.assertIn("8 + 2 = 10", calc.historico)

    # Teste adicional se o resultado de uma divisão pode ser usado diretamente em uma multiplicação subsequente
    def test_integracao_resultado_divisao_em_multiplicacao(self):
        calc = Calculadora()
        calc.dividir(20, 5)  # resultado = 4
        calc.multiplicar(calc.obter_ultimo_resultado(), 7)  # 4 * 7 = 28

        self.assertEqual(calc.obter_ultimo_resultado(), 28)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("20 / 5 = 4.0", calc.historico)
        self.assertIn("4.0 * 7 = 28.0", calc.historico)

if __name__ == '__main__':
    unittest.main()