# Defend the Castle

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Versão atual: **Protótipo da Semana 2** — primeira versão executável do jogo.

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

O jogador controla um arqueiro que defende um castelo na parte inferior da tela. O arqueiro dispara flechas automaticamente em direção aos inimigos que aparecem na parte superior. O objetivo é eliminar o maior número possível de inimigos antes que eles encostem no arqueiro.

> Nesta versão (Semana 2 — protótipo), o jogo possui apenas um inimigo (morcego) se movendo horizontalmente, sem ondas progressivas. Os demais tipos de inimigos e o sistema de ondas serão implementados nas próximas semanas.

## Objetivo do jogador

Acertar os inimigos com as flechas do arqueiro, marcando o maior número de pontos possível antes de perder todas as vidas.

## Regras do jogo

- O arqueiro começa com 3 vidas.
- O arqueiro dispara flechas automaticamente em intervalos fixos de tempo.
- Cada inimigo atingido por uma flecha vale 10 pontos.
- Quando o inimigo encosta no arqueiro, o arqueiro perde 1 vida.
- A partida termina quando o arqueiro perde todas as vidas.

## Controles

- Seta para esquerda **ou** tecla **A**: mover o arqueiro para a esquerda.
- Seta para direita **ou** tecla **D**: mover o arqueiro para a direita.
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

- `config.py`: constantes globais (tamanho da tela, cores, velocidades, FPS, caminhos de arquivos).
- `funcoes.py`: funções de lógica pura (pontuação, vidas, colisão, limite de valor, controle de tiro).
- `sprites.py`: função para recortar imagens da spritesheet.
- `dados.py`: leitura e gravação do recorde em arquivo de texto.
- `jogo.py`: loop principal e funções de criação, atualização e desenho dos elementos do jogo.

## Status das entregas

- [x] **Semana 1** — Proposta inicial preenchida em `docs/proposta.MD`.
- [x] **Semana 2** — Protótipo executável: arqueiro com movimento horizontal, disparo automático de flechas, um inimigo (morcego), colisão e sistema de pontos/vidas.
- [ ] **Semana 3** — Ondas de inimigos, três tipos de inimigos e ajustes de regras.
- [ ] **Semana 4** — Versão final, testes completos e apresentação.

## Recursos externos utilizados

- Spritesheet localizada em `assets/imagens/spritesheet.bmp` (template da disciplina).
