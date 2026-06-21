# Defend the Castle

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

O jogador controla um arqueiro que defende um castelo. As flechas saem sozinhas para cima, e os inimigos descem em ondas cada vez maiores. São três tipos: esqueleto (fraco, aparece primeiro), morcego (o mais rápido e fraco) e orc (o mais lento e resistente, aguenta 2 flechas). O objetivo é sobreviver às 10 ondas marcando o maior número de pontos.

## Integrantes do grupo

- Dimitry Gonzales
- João Paulo Ferreira Rodrigues
- Pedro Henrique Soares Silva
- Samuel Ferreira Guimarães

## Como executar

```bash
pip install -r requirements.txt
python main.py
```

## Como rodar os testes

```bash
python -m pytest
```

## Controles

- Setas ou A / D: mover o arqueiro.
- Na tela inicial: digite o nome e aperte ENTER para jogar.
- ESPAÇO (na tela de fim): jogar de novo.

## Estrutura do projeto

- `main.py`: ponto de entrada (só chama o jogo).
- `src/config.py`: painel de controle  todos os valores que dá pra mudar.
- `src/funcoes.py`: todas as funções do jogo (regras, fluxo da partida e desenho).
- `src/arqueiro.py`, `src/esqueleto.py`, `src/morcego.py`, `src/orc.py`, `src/flecha.py`: uma classe por arquivo.
- `src/sprites.py`: carrega as imagens dos personagens.
- `src/dados.py`: lê e grava o recorde e o ranking em arquivo.
- `src/jogo.py`: o loop principal (liga tudo).
- `assets/`: imagens (arqueiro, esqueleto, morcego, orc e flecha já prontos em PNG).
- `data/`: arquivos salvos (`recorde.txt` e `ranking.txt`).
- `tests/`: testes automáticos com pytest.
- `docs/`: documentação e proposta inicial.

## Como alterar o jogo (mexa em `src/config.py`)

Quase tudo se ajusta mudando um valor no `config.py`:

- Onde o arqueiro nasce: `ARQUEIRO_POSICAO_INICIAL = "esquerda"`, `"centro"` ou `"direita"`.
- Velocidade do arqueiro: `JOGADOR_VELOCIDADE`.
- Vidas iniciais: `JOGADOR_VIDAS`.
- Velocidade de tiro: `INTERVALO_DISPARO` (menor = atira mais rápido).
- Inimigos (velocidade, vida e pontos de cada um): `ESQUELETO_VELOCIDADE`, `ESQUELETO_VIDA`, `ESQUELETO_PONTOS` e os equivalentes `MORCEGO_*` e `ORC_*`. A velocidade aceita número quebrado (ex.: `1.5`).
- Ordem em que os inimigos aparecem nas ondas: `ORDEM_DOS_INIMIGOS` (ex.: `["esqueleto", "morcego", "orc"]`).
- Quantidade de ondas: `ONDA_MAXIMA`.
- Tamanho dos personagens: `ESCALA_ARQUEIRO`, `ESCALA_ESQUELETO`, `ESCALA_MORCEGO`, `ESCALA_ORC` e `ESCALA_FLECHA`.
- Cores e tamanho da tela: seções de cores e de tela no início do arquivo.

Para trocar o desenho de um personagem, basta substituir o arquivo `.png` correspondente em `assets/imagens/` (`arqueiro.png`, `esqueleto.png`, `morcego.png`, `orc.png` ou `flecha.png`).

## Ranking

Antes de jogar, o jogador digita o nome. Ao fim da partida, se a pontuação for boa o bastante, o nome e os pontos entram no ranking (placar dos melhores), salvo em `data/ranking.txt`. O ranking aparece na tela inicial e na tela de fim.
