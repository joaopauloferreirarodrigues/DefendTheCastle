# Código-fonte (`src/`)

Organização dos arquivos:

- `config.py`: todos os valores ajustáveis do jogo (tela, cores, velocidades, ondas, ranking, caminhos e sprites). É o lugar para mudar como o jogo se comporta.
- `funcoes.py`: todas as funções do jogo, divididas em três partes:
    1. **Regras**: contas simples e puras (pontos, vidas, colisão, ondas, nome, ranking). São as funções testadas pelo pytest.
    2. **Fluxo da partida**: monta as ondas, inicia e atualiza o estado do jogo.
    3. **Desenho**: tudo que aparece na tela.
- `arqueiro.py`, `esqueleto.py`, `morcego.py`, `orc.py`, `flecha.py`: uma classe por arquivo. Os três inimigos (esqueleto, morcego e orc) funcionam do mesmo jeito — descem em linha reta até o castelo. O que muda são os números (velocidade, vida e pontos), que vêm do `config.py`.
- `sprites.py`: carrega a imagem de um personagem e aplica uma escala.
- `dados.py`: lê e grava o recorde e o ranking nos arquivos da pasta `data/`.
- `jogo.py`: o loop principal. Cria a janela, lê o teclado e, a cada quadro, chama as funções de `funcoes.py`.

As classes são importadas no fim de `funcoes.py` para evitar importação circular (as classes usam funções de regra que estão no topo do arquivo).
