# Defend the Castle

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Versão atual: **Versão da Semana 3** — jogo jogável do início ao fim, com ondas de inimigos, sistema de progresso e condições de vitória e derrota.

## Integrantes do grupo

- Dimitry Gonzales
- João Paulo Ferreira Rodrigues
- Pedro Henrique Soares Silva
- Samuel Ferreira Guimarães

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo a proposta inicial.

## Descrição do jogo

O jogador controla um arqueiro que defende um castelo na parte inferior da tela. O arqueiro dispara flechas automaticamente para cima, enquanto os morcegos descem do topo em direção ao castelo, em ondas cada vez maiores. O objetivo é sobreviver a todas as ondas sem perder todas as vidas.


## Objetivo do jogador

Acertar os morcegos com as flechas antes que eles cheguem ao castelo, sobrevivendo às 10 ondas e marcando o maior número de pontos possível.

## Regras do jogo

- O arqueiro começa com 3 vidas.
- O arqueiro dispara flechas automaticamente em intervalos fixos de tempo.
- Cada morcego acertado por uma flecha vale 10 pontos.
- Quando um morcego chega ao castelo, o arqueiro perde 1 vida.
- Vitória: sobreviver até o fim da última onda (onda 10).
- Derrota: perder todas as vidas.
- A maior pontuação é salva no arquivo `data/recorde.txt`.

## Controles

- Seta para esquerda ou tecla A: mover o arqueiro para a esquerda.
- Seta para direita ou tecla D: mover o arqueiro para a direita.
- ESPAÇO: iniciar a partida e jogar novamente após o fim.
- Fechar a janela: encerra o jogo.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd Projeto-Final
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Organização do código (`src/`)

- `config.py`: constantes globais (tamanho da tela, cores, velocidades, FPS, ondas e caminhos de arquivos).
- `funcoes.py`: funções de lógica pura (pontuação, vidas, colisão, limite de valor, controle de tiro, ondas e vitória).
- `sprites.py`: funções para recortar imagens da spritesheet (incluindo o recorte sem fundo, com a área de colisão justa).
- `dados.py`: leitura e gravação do recorde em arquivo de texto.
- `jogo.py`: loop principal e funções de criação, atualização e desenho dos elementos do jogo.

## Status das entregas

- [x] **Semana 1** — Proposta inicial preenchida em `docs/proposta.MD`.
- [x] **Semana 2** — Protótipo executável: arqueiro com movimento horizontal, disparo automático de flechas, um inimigo (morcego), colisão e sistema de pontos/vidas.
- [x] **Semana 3** — Ondas de morcegos descendo até o castelo, progresso por ondas, condições de vitória e derrota, telas de início e fim, e primeira versão dos testes.
- [ ] **Semana 4** — Versão final, mais tipos de inimigos, testes completos e apresentação.

## Recursos externos utilizados

- Spritesheet localizada em `assets/imagens/spritesheet.bmp` (template da disciplina).
