# Testes

Esta pasta contem os testes automatizados do projeto, escritos com `pytest`.

## Arquivos

- `conftest.py`: configura o pygame sem abrir janela, para
  que os testes rodem
- `test_logica.py`: contem todos os testes. 
## Como executar

```bash
python -m pytest
```
Para ver cada teste individualmente:

```bash
python -m pytest -v
```

## Cobertura

Sao 72 testes no total. Toda funcao de `src/funcoes.py` e todas as classes tem
pelo menos um teste, e a maioria tem varios casos (incluindo casos de borda e
varios `assert not` para confirmar o que NAO deve acontecer). Destaques dos
testes novos:

- a ordem das ondas (esqueleto primeiro, depois morcego, depois orc);
- a ordem de velocidade (orc < esqueleto < morcego);
- o orc sobrevive a 1 tiro e so morre no 2.

## Boas praticas

- Cada funcao ou classe nova deve ganhar um teste aqui.
- Prefira funcoes pequenas e puras (que so dependem dos argumentos), porque sao
  faceis de testar.
- Use `assert` para o que deve ser verdade e `assert not` para o que deve ser
  falso.
