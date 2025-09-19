# Relatório

### Resultado da execução dos testes

-   **Executados**: 28
-   **Passaram**: 28
-   **Falharam**: 0

### Cobertura de código obtida

| Name                     | Stmts | Miss | Cover |
| ------------------------ | ----- | ---- | ----- |
| src/calculadora.py       | 47    | 0    | 100%  |
| tests/test_integracao.py | 45    | 0    | 100%  |
| tests/test_unidade.py    | 147   | 0    | 100%  |
| TOTAL                    | 237   | 0    | 100%  |

### Quais problemas foram encontrados

Nenhum

### Correções do código da calculadora

Para a validação dos tipos foi criado um novo método que é reutilizado em todos os métodos de operações matemáticas. **Também foi adicionada uma verificação se o tipo do operando é bool, que no caso é instância de int então a verificação anterior não era suficiente para valores booleanos**:

```python
def _validar_operandos(self, *args):
    for valor in args:
        if not isinstance(valor, (int, float)):
            raise TypeError("Argumentos devem ser numeros")
        if isinstance(valor, bool):
            raise TypeError("Argumentos devem ser numeros (por mais que bool seja considerado instância de int, não é valido)")
```

## Descrição dos testes 

### Teste de unidade:
**Teste de soma (utilizado (5+3=8)**
```python 
    def test_entrada_saida_soma(self):
        calc = Calculadora()
        resultado = calc.somar(5, 3)
        self.assertEqual(resultado, 8)
        self.assertEqual(calc.obter_ultimo_resultado(), 8)
```

**Teste de subtração (utilizado 5-3=2)**
```python
def test_entrada_saida_subtracao(self):
        calc = Calculadora()
        resultado = calc.subtrair(5, 3)
        self.assertEqual(resultado, 2)
        self.assertEqual(calc.obter_ultimo_resultado(), 2)
```

**Teste de multiplicação (utilizado 5*3=15)**
```python
def test_entrada_saida_multiplicacao(self):
        calc = Calculadora()
        resultado = calc.multiplicar(5, 3)
        self.assertEqual(resultado, 15)
        self.assertEqual(calc.obter_ultimo_resultado(), 15)
```
**Teste de divisão (utilizado 6/3=2)**
```python
def test_entrada_saida_divisao(self):
        calc = Calculadora()
        resultado = calc.dividir(6, 3)
        self.assertEqual(resultado, 2)
        self.assertEqual(calc.obter_ultimo_resultado(), 2)
```
**Teste de potência (utilizado 3^2=9)**
```python
    def test_entrada_saida_potencia(self):
        calc = Calculadora()
        resultado = calc.potencia(3, 2)
        self.assertEqual(resultado, 9)
        self.assertEqual(calc.obter_ultimo_resultado(), 9)
```
**Teste de erro da calculadora com a tipagem inválida (utilizado em todas as operações)**
```python
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
```
**Teste adicional que verifica entrada booleana**
```python
def test_tipagem_invalida_bool(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar(True, 3) 
```
**Teste para verificar a consistência do histórico dos resultados da calculadora (utilizado as operações de soma e multiplicação)**
```python
def test_consistencia_historico(self):
        calc = Calculadora()
        calc.somar(2, 3)
        calc.multiplicar(4, 5)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 + 3 = 5", calc.historico)
        self.assertIn("4 * 5 = 20", calc.historico)
```
**Teste adicional que verifica se o histórico está vazio após ser limpo (utilizado a operação de multiplicação)**
```python
    def test_consistencia_historico_vazio(self):
        calc = Calculadora()
        calc.multiplicar(4, 5)
        self.assertEqual(len(calc.historico), 1)
        self.assertIn("4 * 5 = 20", calc.historico)
        calc.limpar_historico()
        self.assertNotIn("4 * 5 = 20", calc.historico)
        self.assertEqual(len(calc.historico), 0)
```
**Teste se a calculadora aparece algum resultado após ser inicalizada (saída deve ser 0)**
```python
def test_inicializacao(self):
        calc = Calculadora()
        self.assertEqual(calc.resultado, 0)
        self.assertEqual(len(calc.historico), 0)
```
**Teste adicional que verifica se os tipos são corretos após inicialização**
```python
def test_inicializacao_tipos(self):
        calc = Calculadora()
        self.assertIsInstance(calc.resultado, int)
        self.assertIsInstance(calc.historico, list)
        self.assertEqual(calc.historico, [])
```
**Teste se a calculadora aparece 0 após o histórico ser limpado (saída deve ser 0)**
```python
    def test_modificacao_historico(self):
        calc = Calculadora()
        calc.somar(1, 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)

```
**Teste adicional que verifica se os dados são inseridos mesmo após o histórico ser limpo**
```python
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
```
**Teste de operação de soma e multiplicação com números muito pequenos**
```python
    def test_limite_inferior(self):
        calc = Calculadora()
        # Teste com zero
        resultado = calc.somar(0, 5)
        self.assertEqual(resultado, 5)
        # Teste com números negativos muito pequenos
        resultado = calc.multiplicar(-1e-10, 2)
        self.assertEqual(resultado, -2e-10)
```
**Teste adicional que verifica operações com números muito próximos a zero**
```python
    def test_limite_inferior_proximo_zero(self):
        calc = Calculadora()
        resultado = calc.subtrair(1e-308, 1e-308)
        self.assertEqual(resultado, 0)

        resultado = calc.dividir(1e-308, 1)
        self.assertEqual(resultado, 1e-308)
```
**Teste de operação de soma com números muito grandes**
```python
def test_limite_superior(self):
        calc = Calculadora()
        # Teste com números grandes
        resultado = calc.somar(1e10, 1e10)
        self.assertEqual(resultado, 2e10)
```
**Teste adicional que teste potência com valores altos, levando a overflow**
```python
    def test_limite_superior_potencia(self):
        calc = Calculadora()
        max_float = sys.float_info.max
        
        with self.assertRaises(OverflowError):
            resultado = calc.potencia(max_float, 2)  
```
**Teste com valores próximos ao máximo de float (operação de soma)**
```python
def test_limite_superior_proximo_float_max(self):
        calc = Calculadora()
        max_float = sys.float_info.max

        resultado = calc.somar(max_float, max_float)
        self.assertTrue(resultado == float("inf"))

        resultado = calc.multiplicar(max_float, 2)
        self.assertTrue(resultado == float("inf"))
```
**Teste se aparece Erro após fazer uma divisão por 0**
```python
def test_divisao_por_zero(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)
```
**Teste adicional de divisão de um número por float("inf"), que deve resultar em 0**
```python
 def test_valores_fora_intervalo_divisao_infinito(self):
        calc = Calculadora()
        resultado = calc.dividir(100, float("inf"))
        self.assertEqual(resultado, 0.0)
```
**Teste do fluxos de divisão (divisão por número positivo e divisão por 0)**
```python
def test_fluxos_divisao(self):
        calc = Calculadora()
        # Caminho normal
        resultado = calc.dividir(10, 2)
        self.assertEqual(resultado, 5)
        # Caminho de erro
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)
```
**Teste de caminho alternativo que testa potência com expoente 0**
```python
    def test_fluxos_potencia_expoente_zero(self):
        calc = Calculadora()
        # Caminho normal
        resultado = calc.potencia(10, 2)
        self.assertEqual(resultado, 100)
        # Caminho alternativo
        resultado = calc.potencia(999999, 0)
        self.assertEqual(resultado, 1)
```
**Teste se aparece alguma mensagem de erro após um except**
```python
    def test_mensagens_erro(self):
        calc = Calculadora()
        try:
            calc.dividir(5, 0)
        except ValueError as e:
            self.assertEqual(str(e), "Divisao por zero nao permitida")
```
**Teste de mensagem específica para entradas booleanas (utilizado a operação soma**
```python
 def test_mensagens_erro_tipagem_bool(self):
        calc = Calculadora()
        try:
            calc.somar(True, 5)
        except TypeError as e:
            self.assertEqual(str(e), "Argumentos devem ser numeros (por mais que bool seja considerado instância de int, não é valido)")

```

### Teste de integração:

**Teste para verificar se a calculadora faz as operações sequenciais, ou seja, se faz cálculos em sequência utilizando o último resultado.**
```python
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

```

No teste foi utilizado a soma (2+3), depois a multiplicação (5*4), e, por último, a divisão (20/2).

**Teste adicional de operações sequenciais, porém utilizando potência**
```python
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
```

**Teste para obter o histórico de resultados da calculadora**
```python
    def test_integracao_historico_resultado(self):
        calc = Calculadora()
        calc.potencia(2, 3)  # 2^3 = 8
        calc.somar(calc.obter_ultimo_resultado(), 2)  # 8 + 2 = 10

        self.assertEqual(calc.obter_ultimo_resultado(), 10)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 ^ 3 = 8", calc.historico)
        self.assertIn("8 + 2 = 10", calc.historico)
```
**Teste adicional se o resultado de uma divisão pode ser usado diretamente numa multiplicação subsequente**
```python 
def test_integracao_resultado_divisao_em_multiplicacao(self):
        calc = Calculadora()
        calc.dividir(20, 5)  # resultado = 4
        calc.multiplicar(calc.obter_ultimo_resultado(), 7)  # 4 * 7 = 28

        self.assertEqual(calc.obter_ultimo_resultado(), 28)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("20 / 5 = 4.0", calc.historico)
        self.assertIn("4.0 * 7 = 28.0", calc.historico)
```



