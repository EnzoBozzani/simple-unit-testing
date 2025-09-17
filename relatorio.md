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
