import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
    JOGADOR_ALTURA,
    JOGADOR_LARGURA,
    JOGADOR_VELOCIDADE,
    JOGADOR_VIDAS,
    INIMIGO_ALTURA,
    INIMIGO_LARGURA,
    INTERVALO_DISPARO,
    FLECHA_ALTURA,
    FLECHA_LARGURA,
    FLECHA_VELOCIDADE,
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
)
from src.sprites import pegar_sprite
from src.dados import (
    salvar_recorde,
    carregar_recorde,
)


def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True

    # 1. Carregando as imagens recortadas do Spritesheet
    player_image = pegar_sprite(CAMINHO_SPRITES, x=110, y=120, width=190, height=190, scale=0.5)
    bat_image    = pegar_sprite(CAMINHO_SPRITES, x=905, y=1060, width=200, height=130, scale=0.5)
    flecha_image = pegar_sprite(CAMINHO_SPRITES, x=1950, y=685, width=20, height=40, scale=1)


    # 2. Criando a estrutura de Sprites usando Dicionários
    jogador = {
        "imagem": player_image,
        "rect": player_image.get_rect(topleft=(370, 480))
    }

    inimigo = {
        "imagem": bat_image,
        "rect": bat_image.get_rect(topleft=(350, 100))
    }

    # Flecha: um retângulo que sobe pela tela
    flecha = {
        "imagem": flecha_image,
        "rect": flecha_image.get_rect(),
        "ativa": False
    }

    velocidade = 5
    pontos = 0
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        teclas = pygame.key.get_pressed()

        # Movimentação esquerda e direita
        if teclas[pygame.K_LEFT]:
            jogador["rect"].x -= JOGADOR_VELOCIDADE
        if teclas[pygame.K_RIGHT]:
            jogador["rect"].x += JOGADOR_VELOCIDADE

        # Limitando dentro das bordas da tela
        jogador["rect"].x = limitar_valor(jogador["rect"].x, 0, LARGURA_TELA - jogador["rect"].width)

        # Disparando a flecha com o espaço
        if teclas[pygame.K_SPACE] and not flecha["ativa"]:
            flecha["rect"].midbottom = jogador["rect"].midtop
            flecha["ativa"] = True

        # flecha para cima
        if flecha["ativa"]:
            flecha["rect"].y -= FLECHA_VELOCIDADE

            # desativa, ao sair da tele
            if flecha["rect"].bottom < 0:
                flecha["ativa"] = False

            # Quando a flecha atinge o inimigo
            if verificar_colisao(flecha["rect"], inimigo["rect"]):
                pontos = calcular_pontos(pontos, 10)
                flecha["ativa"] = False

                # Troca o inimigo de lugar, para simular o spawn
                inimigo["rect"].x += 80
                if inimigo["rect"].x > LARGURA_TELA - inimigo["rect"].width:
                    inimigo["rect"].x = 50

        # Regras de fim de jogo e recorde
        if jogador_perdeu(vidas):
            rodando = False

        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde} | Vidas: {vidas}"
        )

        tela.fill(CINZA)

        # elementos na tela
        tela.blit(inimigo["imagem"], inimigo["rect"])
        tela.blit(jogador["imagem"], jogador["rect"])

        # flechaativa
        if flecha["ativa"]:
            tela.blit(flecha["imagem"], flecha["rect"])

        pygame.display.flip()

    pygame.quit()
