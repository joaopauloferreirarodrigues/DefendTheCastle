# Testes

Esta pasta contem os testes automatizados do projeto, escritos com `pytest`.

## Arquivos

- `test_logica.py`: contem todos os testes de logica do jogo.

## Como executar

```bash
python -m pytest
```
Para ver cada teste individualmente:

```bash
python -m pytest -v
```

## Cobertura

Testes focados em funcoes de logica do jogo, cada teste depende apenas dos argumentos passados para a funcao

Funcoes testadas:

- pontuacao e vida: `calcular_pontos`, `tomar_dano`, `jogador_perdeu`;
- movimento: `limitar_valor`;
- disparo: `pode_atirar`;
- posicionamento: `calcular_posicao_central`, `posicao_inicial_x`;
- ondas: `quantidade_de_inimigos`, `calcular_espaco_entre_inimigos`,
  `tipo_da_onda`, `venceu_o_jogo`;
- nome do jogador: `nome_valido`, `adicionar_caractere`, `remover_caractere`;
- ranking: `eh_novo_recorde`, `adicionar_ao_ranking`, `pontos_da_entrada`,
  `melhor_pontuacao`, `formatar_entrada_ranking`, `interpretar_linha_ranking`;
- constantes do jogo: ordem de velocidade dos inimigos (orc < esqueleto < morcego).

## Boas praticas

- Cada funcao de logica nova deve ganhar um teste aqui.
- Prefira funcoes pequenas e puras (que so dependem dos argumentos), porque sao
  faceis de testar.
- Use `assert` para o que deve ser verdade e `assert not` para o que deve ser
  falso.
