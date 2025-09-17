# Instalar dependencias

```
pip install -r requirements.txt
```

# Executar todos os testes

```
python -m unittest discover tests -v
```

# Executar com cobertura

```
coverage run -m unittest discover tests
coverage report
coverage html
```

# Executar teste especifico

```
python -m unittest tests.test_unidade.TestCalculadora.test_soma -v
```
