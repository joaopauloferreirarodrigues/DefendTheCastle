import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    BRANCO,
    CEU,
    PEDRA,
    MARROM,
    VERMELHO,
    AMARELO,
    VERDE,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
    JOGADOR_VELOCIDADE,
    JOGADOR_VIDAS,
    INTERVALO_DISPARO,
    FLECHA_LARGURA,
    FLECHA_ALTURA,
    FLECHA_VELOCIDADE,
    MORCEGO_VELOCIDADE_Y,
    ONDA_MAXIMA,
    MORCEGOS_BASE,
    LINHA_CASTELO,
    PONTOS_POR_MORCEGO,
    SPRITE_ARQUEIRO,
    SPRITE_MORCEGO,
    ESCALA_ARQUEIRO,
    ESCALA_MORCEGO,
)
from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
    pode_atirar,
    quantidade_de_morcegos,
    venceu_o_jogo,
    calcular_posicao_central,
    calcular_espaco_entre_morcegos,
)
from src.sprites import pegar_sprite_sem_fundo
from src.dados import salvar_recorde, carregar_recorde




class Arqueiro:
    """Representa o arqueiro controlado pelo jogador."""

    def __init__(self, imagem):
        self.imagem = imagem
        self.rect = imagem.get_rect()
        self.rect.centerx = calcular_posicao_central(LARGURA_TELA, 0) + LARGURA_TELA // 2
        self.rect.bottom = LINHA_CASTELO + 30

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.rect.x -= JOGADOR_VELOCIDADE
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.rect.x += JOGADOR_VELOCIDADE
        self.rect.x = limitar_valor(self.rect.x, 0, LARGURA_TELA - self.rect.width)

    def desenhar(self, tela):
        """Desenha o arqueiro na tela."""
        tela.blit(self.imagem, self.rect)


class Morcego:
    def __init__(self, imagem, x, y):
        self.imagem = imagem
        self.rect = imagem.get_rect(topleft=(x, y))
        self.velocidade_y = MORCEGO_VELOCIDADE_Y
        self.atingido = False

    def mover(self):
        """Faz o morcego descer em linha reta"""
        self.rect.y += self.velocidade_y

    def chegou_ao_castelo(self):
        """Indica se o morcego alcançou o castelo"""
        return self.rect.bottom >= LINHA_CASTELO

    def desenhar(self, tela):
        """Desenha o morcego na tela."""
        tela.blit(self.imagem, self.rect)


class Flecha:
    """Representa uma flecha disparada pelo arqueiro."""

    def __init__(self, x_centro, y_base):
        self.rect = pygame.Rect(0, 0, FLECHA_LARGURA, FLECHA_ALTURA)
        self.rect.centerx = x_centro
        self.rect.bottom = y_base

    def mover(self):
        """Move a flecha para cima."""
        self.rect.y -= FLECHA_VELOCIDADE

    def saiu_da_tela(self):
        """Indica se a flecha saiu pela parte de cima da tela."""
        return self.rect.bottom <= 0

    def desenhar(self, tela):
        """Desenha a flecha como um pequeno retângulo marrom."""
        pygame.draw.rect(tela, MARROM, self.rect)



def gerar_onda(numero_onda, imagem_morcego):
    """Cria a lista de morcegos de uma onda"""
    morcegos = []
    quantidade = quantidade_de_morcegos(numero_onda, MORCEGOS_BASE)
    espaco = calcular_espaco_entre_morcegos(LARGURA_TELA, quantidade)
    i = 0
    while i < quantidade:
        x = espaco * i + (espaco // 2) - 20
        y = -60
        morcegos.append(Morcego(imagem_morcego, x, y))
        i = i + 1
    return morcegos


def processar_acerto_flechas(flechas, morcegos):
    """Confere a colisão das flechas com os morcegos Cada flecha acerta só um morcego e some 
    Retorna as flechas restantes, os morcegos restantes e os pontos"""
    flechas_restantes = []
    pontos_ganhos = 0
    for flecha in flechas:
        acertou = False
        for morcego in morcegos:
            if not acertou and not morcego.atingido and verificar_colisao(flecha.rect, morcego.rect):
                morcego.atingido = True
                acertou = True
                pontos_ganhos = pontos_ganhos + PONTOS_POR_MORCEGO
        if not acertou:
            flechas_restantes.append(flecha)

    morcegos_restantes = []
    for morcego in morcegos:
        if not morcego.atingido:
            morcegos_restantes.append(morcego)

    return flechas_restantes, morcegos_restantes, pontos_ganhos


def processar_morcegos_no_castelo(morcegos):
    """Separa os morcegos que alcançaram o castelo dos que continuam descendo
    Retorna a lista dos que continuam e a contagem dos que chegaram"""
    continuam = []
    chegaram = 0
    for morcego in morcegos:
        if morcego.chegou_ao_castelo():
            chegaram = chegaram + 1
        else:
            continuam.append(morcego)
    return continuam, chegaram


def atualizar_partida(jogo, teclas, tempo_atual):
    jogo["arqueiro"].mover(teclas)

    if pode_atirar(tempo_atual, jogo["tempo_ultimo_tiro"], INTERVALO_DISPARO):
        x_centro = jogo["arqueiro"].rect.centerx
        y_base = jogo["arqueiro"].rect.top
        jogo["flechas"].append(Flecha(x_centro, y_base))
        jogo["tempo_ultimo_tiro"] = tempo_atual

    for flecha in jogo["flechas"]:
        flecha.mover()
    jogo["flechas"] = [f for f in jogo["flechas"] if not f.saiu_da_tela()]

    for morcego in jogo["morcegos"]:
        morcego.mover()

    jogo["flechas"], jogo["morcegos"], ganhos = processar_acerto_flechas(
        jogo["flechas"], jogo["morcegos"]
    )
    jogo["pontos"] = calcular_pontos(jogo["pontos"], ganhos)

    jogo["morcegos"], chegaram = processar_morcegos_no_castelo(jogo["morcegos"])
    jogo["vidas"] = tomar_dano(jogo["vidas"], chegaram)

    if jogador_perdeu(jogo["vidas"]):
        return "fim"

    if len(jogo["morcegos"]) == 0:
        jogo["onda"] = jogo["onda"] + 1
        if venceu_o_jogo(jogo["onda"], ONDA_MAXIMA):
            jogo["venceu"] = True
            return "fim"
        jogo["morcegos"] = gerar_onda(jogo["onda"], jogo["imagem_morcego"])

    return "jogando"



def desenhar_cenario(tela):
    tela.fill(CEU)
    pygame.draw.rect(tela, PEDRA, (0, LINHA_CASTELO, LARGURA_TELA, ALTURA_TELA - LINHA_CASTELO))
    x = 0
    while x < LARGURA_TELA:
        pygame.draw.rect(tela, PEDRA, (x, LINHA_CASTELO - 18, 26, 18))
        x = x + 52
    pygame.draw.rect(tela, MARROM, (0, ALTURA_TELA - 24, LARGURA_TELA, 24))


def desenhar_hud(tela, fonte, pontos, recorde, vidas, onda):
    """Mostra pontos, recorde, onda e vidas no topo da tela."""
    tela.blit(fonte.render(f"Pontos: {pontos}", True, BRANCO), (10, 10))
    tela.blit(fonte.render(f"Recorde: {recorde}", True, AMARELO), (10, 35))
    tela.blit(fonte.render(f"Onda: {onda}/{ONDA_MAXIMA}", True, BRANCO), (LARGURA_TELA - 150, 10))
    i = 0
    while i < vidas:
        pygame.draw.rect(tela, VERMELHO, (10 + i * 26, 62, 18, 18))
        i = i + 1


def desenhar_texto_central(tela, fonte, texto, y, cor):
    """Desenha um texto centralizado na tela."""
    imagem_texto = fonte.render(texto, True, cor)
    rect_texto = imagem_texto.get_rect(center=(LARGURA_TELA // 2, y))
    tela.blit(imagem_texto, rect_texto)


def desenhar_tela_inicial(tela, fonte_grande, fonte, recorde):
    """Desenha a tela de abertura do jogo."""
    tela.fill(CEU)
    desenhar_texto_central(tela, fonte_grande, "DEFEND THE CASTLE", 190, BRANCO)
    desenhar_texto_central(tela, fonte, "Defenda o castelo dos morcegos!", 260, BRANCO)
    desenhar_texto_central(tela, fonte, "Setas ou A/D para mover. As flechas saem sozinhas.", 300, AMARELO)
    desenhar_texto_central(tela, fonte, f"Recorde: {recorde}", 340, AMARELO)
    desenhar_texto_central(tela, fonte, "Pressione ESPACO para comecar", 410, VERDE)


def desenhar_tela_fim(tela, fonte_grande, fonte, venceu, pontos, recorde):
    """Desenha a tela de fim de jogo"""
    tela.fill(CEU)
    if venceu:
        desenhar_texto_central(tela, fonte_grande, "VITORIA!", 200, VERDE)
    else:
        desenhar_texto_central(tela, fonte_grande, "FIM DE JOGO", 200, VERMELHO)
    desenhar_texto_central(tela, fonte, f"Pontos: {pontos}    Recorde: {recorde}", 280, BRANCO)
    desenhar_texto_central(tela, fonte, "Pressione ESPACO para jogar de novo", 360, AMARELO)


def desenhar_partida(tela, fonte, jogo, recorde):
    """Desenha a cena de uma partida que ainda não acabou"""
    desenhar_cenario(tela)
    for morcego in jogo["morcegos"]:
        morcego.desenhar(tela)
    for flecha in jogo["flechas"]:
        flecha.desenhar(tela)
    jogo["arqueiro"].desenhar(tela)
    desenhar_hud(tela, fonte, jogo["pontos"], recorde, jogo["vidas"], jogo["onda"])


def iniciar_partida(imagem_arqueiro, imagem_morcego, tempo_atual):
    """Monta o estado inicial da partida"""
    return {
        "arqueiro": Arqueiro(imagem_arqueiro),
        "morcegos": gerar_onda(1, imagem_morcego),
        "flechas": [],
        "pontos": 0,
        "vidas": JOGADOR_VIDAS,
        "onda": 1,
        "tempo_ultimo_tiro": tempo_atual,
        "venceu": False,
        "imagem_morcego": imagem_morcego,
    }

def carregar_imagens():
    arq_x, arq_y, arq_largura, arq_altura = SPRITE_ARQUEIRO
    mor_x, mor_y, mor_largura, mor_altura = SPRITE_MORCEGO

    imagem_arqueiro = pegar_sprite_sem_fundo(
        CAMINHO_SPRITES, arq_x, arq_y, arq_largura, arq_altura, ESCALA_ARQUEIRO
    )
    imagem_morcego = pegar_sprite_sem_fundo(
        CAMINHO_SPRITES, mor_x, mor_y, mor_largura, mor_altura, ESCALA_MORCEGO
    )
    return imagem_arqueiro, imagem_morcego



def executar_jogo():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()
    fonte = pygame.font.SysFont(None, 28)
    fonte_grande = pygame.font.SysFont(None, 64)

    imagem_arqueiro, imagem_morcego = carregar_imagens()

    recorde = carregar_recorde(CAMINHO_RECORDE)
    estado = "inicio"
    jogo = None
    rodando = True

    while rodando:
        relogio.tick(FPS)
        tempo_atual = pygame.time.get_ticks()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and estado in ("inicio", "fim"):
                    jogo = iniciar_partida(imagem_arqueiro, imagem_morcego, tempo_atual)
                    estado = "jogando"

        teclas = pygame.key.get_pressed()

        if estado == "jogando":
            estado = atualizar_partida(jogo, teclas, tempo_atual)
            if jogo["pontos"] > recorde:
                recorde = jogo["pontos"]
                salvar_recorde(CAMINHO_RECORDE, recorde)

        if estado == "inicio":
            desenhar_tela_inicial(tela, fonte_grande, fonte, recorde)
        elif estado == "jogando":
            desenhar_partida(tela, fonte, jogo, recorde)
        elif estado == "fim":
            desenhar_tela_fim(tela, fonte_grande, fonte, jogo["venceu"], jogo["pontos"], recorde)

        pygame.display.flip()

    pygame.quit()
