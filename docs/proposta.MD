# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Escreva aqui o nome provisório do jogo.

Defend the Castle

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1:Dimitry Gonzales
- Nome 2: João Paulo Ferreira Rodrigues
- Nome 3: Pedro Henrique Soares Silva
- Nome 4: Samuel Ferreira Guimarães

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo: 

Jogo de defesa com ondas de inimigos(estilo Space Invaders)

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:

Na tela aparece um castelo abaixo que o jogador deve proteger. O jogador controla um arqueiro, se move para a esquerda ou direita na frente do castelo. O arqueiro dispara flechas automaticamente na direção dos inimigos. O jogador precisa se posicionar para eliminar os inimigos. Cada onda de inimigos fica mais rápida e numerosa, aumentando a dificuldade progressivamente.

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

Sobreviver ao maior número de ondas possível, eliminando todos os inimigos.

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

- Regra 1: O arqueiro dispara automaticamente a cada intervalo fixo de tempo.
- Regra 2: A cada onda concluída, a velocidade e a quantidade de inimigos aumentam
- Regra 3: O arqueiro começa com 3 vidas
- Regra 4: Cada ataque inimigo que toca o arqueiro remove 1 vida
- Regra 5: A partida termina quando o arqueiro perde todas as suas vidas.

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

Sobreviver a 15 hordas

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

O jogo termina quando o arqueiro perde todas as suas 3 vidas

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

Um arqueiro

Descrição:

Controlado pelas teclas A e D (ou setas para esquerda/direita), ele atira flechas em um intervalo de tempo regular

## Obstáculos, inimigos ou desafios

Exemplo:

Morcego: rápido, fraco (1 ponto de vida)
Esqueleto: velocidade média, resistência média (2 pontos de vida)
Orc: lento, resistente (3 pontos de vida)


Descrição:

Três tipos diferentes de inimigos podem surgir em ondas, atirando na direção do arqueiro

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

Flechas disparadas automaticamente pelo arqueiro
Poção de vida que restaura vida do arqueiro
Inimigos derrotados somam pontos ao placar

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

O arqueiro começa com 3 vidas exibidas na tela. A pontuação é acumulada a cada inimigo eliminado. O número da onda atual é exibido no topo da tela.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Tecla/comando: A ou Seta para esquerda: Movem o personagem para esquerda
- Tecla/comando: D ou Seta para direita: Movem o personagem para direita
- Tecla/comando: Esc: Menu de pausa

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

main.py — inicia o jogo e executa o loop principal;
src/config.py — configurações globais (tamanho da tela, cores, FPS, velocidades);
src/jogador.py — arqueiro (movimento e disparo automático);
src/inimigos.py — inimigos (Morcego, Orc, Esqueleto) com comportamentos distintos;
src/flecha.py — classe da flecha e lógica de colisão;
src/ondas.py — geração e progressão das ondas;
src/hud.py — exibição de pontuação, vidas do arqueiro e número da onda;
src/dados.py — leitura e escrita do ranking em arquivo



## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

- Modelos gratuitos de arqueiro, morcego, orc e esqueleto
- Imagem de castelo medieval como parte do cenário
- Sons de flecha disparada 

Caso não pretenda utilizar recursos externos, escreva:

> Não pretendemos utilizar recursos externos.

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1: Implementar o disparo automático
- Dificuldade 2: Detectar o dano causado e sofido
- Dificuldade 3: Criar as ondas progressivas 
- Dificuldade 4: "Balancear" o jogo 

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

A versão mínima do jogo terá: um arqueiro controlado pelo teclado, disparo automático de flechas, três tipos de inimigos com vidas diferentes, ondas de inimigos, sistema de 3 vidas para o arqueiro, pontuação exibida na tela e tela de fim de jogo com pontuação final.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1:
- Melhoria 2:
- Melhoria 3: