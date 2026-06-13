import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    MARROM,
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
    pode_atirar,
)
from src.sprites import pegar_sprite
from src.dados import (
    salvar_recorde,
    carregar_recorde,
)

"""Funções de criação dos elementos do jogo"""

def criar_arqueiro(imagem):
    """Cria o arqueiro, posicionado ele na parte de baixo no centro da tela."""
    rect = imagem.get_rect()
    rect.centerx = LARGURA_TELA // 2
    rect.bottom = ALTURA_TELA - 20
    return {
        "imagem": imagem,
        "rect": rect,
    }


def criar_morcego(imagem):
    """Cria o morcego com posição inicial e movimentação horizontal."""
    rect = imagem.get_rect(topleft=(50, 50))
    return {
        "imagem": imagem,
        "rect": rect,
        "velocidade_x": VELOCIDADE_MORCEGO,
    }


def criar_flecha(x_centro, y_base):
    """Cria uma flecha saindo da posição do arqueiro"""
    rect = pygame.Rect(0, 0, LARGURA_FLECHA, ALTURA_FLECHA)
    rect.centerx = x_centro
    rect.bottom = y_base
    return {"rect": rect}

"""Funções de atualização"""

def atualizar_arqueiro(arqueiro, teclas):
    """Move o arqueiro pra esquerda ou direita."""
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        arqueiro["rect"].x -= VELOCIDADE_ARQUEIRO
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        arqueiro["rect"].x += VELOCIDADE_ARQUEIRO

    """Mantém o arqueiro na tela"""
    arqueiro["rect"].x = limitar_valor(
        arqueiro["rect"].x, 0, LARGURA_TELA - arqueiro["rect"].width
    )


def atualizar_morcego(morcego):
    """Move o morcego automaticamente."""
    morcego["rect"].x += morcego["velocidade_x"]

    """Se bater na borda esquerda, vai pra direita"""
    if morcego["rect"].left <= 0:
        morcego["velocidade_x"] = abs(morcego["velocidade_x"])

    """Se bateu na borda direita, vai para a esquerda"""
    if morcego["rect"].right >= LARGURA_TELA:
        morcego["velocidade_x"] = -abs(morcego["velocidade_x"])


def atualizar_flechas(flechas):
    """Move as flechas para cima."""
    for flecha in flechas:
        flecha["rect"].y -= VELOCIDADE_FLECHA


def remover_flechas_fora_da_tela(flechas):
    """Nova lista com as flechas que ainda estão na tela."""
    flechas_visiveis = []
    for flecha in flechas:
        if flecha["rect"].bottom > 0:
            flechas_visiveis.append(flecha)
    return flechas_visiveis


def reposicionar_morcego(morcego):
    """Manda o morcego de volta para o topo, em uma nova posição"""
    largura_util = LARGURA_TELA - morcego["rect"].width
    nova_x = (morcego["rect"].x + 250) % largura_util
    morcego["rect"].x = nova_x
    morcego["rect"].y = 50

"""Funções de colisão entre flechas e inimigo"""

def processar_acerto_flechas(flechas, morcego):
    """Verifica colisão entre flechas e morcego.
    Retorna a lista de flechas que NÃO acertaram e quantos acertos houve."""
    flechas_restantes = []
    acertos = 0
    for flecha in flechas:
        if verificar_colisao(flecha["rect"], morcego["rect"]):
            acertos = acertos + 1
        else:
            flechas_restantes.append(flecha)
    return flechas_restantes, acertos

"""Função de desenho da cena"""

def desenhar_cena(tela, arqueiro, morcego, flechas):
    """Coloca os elementos do jogo na tela."""
    tela.fill(CINZA)

    """Morcego"""
    tela.blit(morcego["imagem"], morcego["rect"])

    """Arqueiro"""
    tela.blit(arqueiro["imagem"], arqueiro["rect"])

    """Flechas"""
    for flecha in flechas:
        pygame.draw.rect(tela, MARROM, flecha["rect"])
    pygame.display.flip()



"""Monta o jogo e roda o loop"""


def executar_jogo():
    """Executa o jogo"""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()

    """Carrega as imagens do spritesheet"""
    imagem_arqueiro = pegar_sprite(
        CAMINHO_SPRITES, x=110, y=120, width=190, height=190, scale=0.5
    )
    imagem_morcego = pegar_sprite(
        CAMINHO_SPRITES, x=905, y=1060, width=200, height=130, scale=0.5
    )

    """Criando os elementos do jogo"""
    arqueiro = criar_arqueiro(imagem_arqueiro)
    morcego = criar_morcego(imagem_morcego)
    flechas = [] 

    """Início do jogo"""
    pontos = 0
    vidas = VIDAS_INICIAIS
    recorde = carregar_recorde(CAMINHO_RECORDE)
    tempo_ultimo_tiro = 0
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
        tempo_atual = pygame.time.get_ticks()

        """Fechar a janela"""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        """Movimentação do arqueiro"""
        teclas = pygame.key.get_pressed()
        atualizar_arqueiro(arqueiro, teclas)

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

        """Atualiza recorde"""
        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        """Informações no título da janela"""
        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde} | Vidas: {vidas}"
        )

        """Coloca tudo na tela"""
        desenhar_cena(tela, arqueiro, morcego, flechas)

        # elementos na tela
        tela.blit(inimigo["imagem"], inimigo["rect"])
        tela.blit(jogador["imagem"], jogador["rect"])

        # flechaativa
        if flecha["ativa"]:
            tela.blit(flecha["imagem"], flecha["rect"])

        pygame.display.flip()

    pygame.quit()
