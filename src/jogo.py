import pygame

from src.config import (
    ALTURA_TELA,
    CAMINHO_RANKING,
    CAMINHO_RECORDE,
    ESCALA_ARQUEIRO,
    ESCALA_ESQUELETO,
    ESCALA_FLECHA,
    ESCALA_MORCEGO,
    ESCALA_ORC,
    FPS,
    IMAGEM_ARQUEIRO,
    IMAGEM_ESQUELETO,
    IMAGEM_FLECHA,
    IMAGEM_MORCEGO,
    IMAGEM_ORC,
    LARGURA_TELA,
    MAX_RANKING,
    TAMANHO_MAX_NOME,
    TITULO_JOGO,
)
from src.dados import (
    carregar_ranking,
    salvar_ranking,
    salvar_recorde,
)
from src.funcoes import (
    adicionar_ao_ranking,
    adicionar_caractere,
    atualizar_partida,
    desenhar_partida,
    desenhar_tela_fim,
    desenhar_tela_nome,
    eh_novo_recorde,
    iniciar_partida,
    melhor_pontuacao,
    nome_valido,
    remover_caractere,
)
from src.sprites import carregar_sprite


def carregar_imagens():
    """
    Carrega as imagens de todos os personagens.
    O caminho e a escala de cada imagem vem do config (IMAGEM_* e ESCALA_*).
    Retorno:
        dict: imagens prontas, com as chaves "arqueiro", "esqueleto",
        "morcego", "orc" e "flecha".
    """
    return {
        "arqueiro": carregar_sprite(IMAGEM_ARQUEIRO, ESCALA_ARQUEIRO),
        "esqueleto": carregar_sprite(IMAGEM_ESQUELETO, ESCALA_ESQUELETO),
        "morcego": carregar_sprite(IMAGEM_MORCEGO, ESCALA_MORCEGO),
        "orc": carregar_sprite(IMAGEM_ORC, ESCALA_ORC),
        "flecha": carregar_sprite(IMAGEM_FLECHA, ESCALA_FLECHA),
    }


def executar_jogo():
    """
    Liga o jogo e roda o loop principal ate o jogador fechar a janela.
    A cada quadro, este loop: le o teclado, atualiza a partida (chamando as
    funcoes de funcoes.py) e desenha a tela certa conforme o estado atual
    ("nome", "jogando" ou "fim").
    Retorno:
        Nenhum. A funcao roda o jogo e so termina quando a janela e fechada.
    """
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()
    fonte = pygame.font.SysFont(None, 28)
    fonte_grande = pygame.font.SysFont(None, 64)

    imagens = carregar_imagens()

    ranking = carregar_ranking(CAMINHO_RANKING)
    nome = ""
    estado = "nome"  # estados possiveis: "nome", "jogando", "fim"
    jogo = None
    rodando = True

    while rodando:
        relogio.tick(FPS)
        tempo_atual = pygame.time.get_ticks()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            elif evento.type == pygame.KEYDOWN:
                if estado == "nome":
                    if evento.key == pygame.K_RETURN and nome_valido(nome):
                        jogo = iniciar_partida(imagens, tempo_atual)
                        estado = "jogando"
                    elif evento.key == pygame.K_BACKSPACE:
                        nome = remover_caractere(nome)
                    elif evento.unicode != "" and evento.unicode.isprintable():
                        nome = adicionar_caractere(
                            nome, evento.unicode, TAMANHO_MAX_NOME
                        )

                elif estado == "fim" and evento.key == pygame.K_SPACE:
                    nome = ""
                    estado = "nome"

        teclas = pygame.key.get_pressed()

        if estado == "jogando":
            estado = atualizar_partida(jogo, teclas, tempo_atual)
            if estado == "fim" and eh_novo_recorde(jogo["pontos"], ranking):
                ranking = adicionar_ao_ranking(
                    ranking, nome, jogo["pontos"], MAX_RANKING
                )
                salvar_ranking(CAMINHO_RANKING, ranking)
                salvar_recorde(CAMINHO_RECORDE, melhor_pontuacao(ranking)[1])

        if estado == "nome":
            desenhar_tela_nome(tela, fonte_grande, fonte, nome, ranking)
        elif estado == "jogando":
            recorde_nome, recorde_pontos = melhor_pontuacao(ranking)
            desenhar_partida(tela, fonte, jogo, recorde_nome, recorde_pontos)
        elif estado == "fim":
            desenhar_tela_fim(
                tela, fonte_grande, fonte, jogo["venceu"], nome, jogo["pontos"], ranking
            )

        pygame.display.flip()

    pygame.quit()
