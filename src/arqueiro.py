import pygame

from src.config import (
    LARGURA_TELA,
    JOGADOR_VELOCIDADE,
    LINHA_CASTELO,
    ARQUEIRO_POSICAO_INICIAL,
)
from src.funcoes import limitar_valor, posicao_inicial_x


class Arqueiro:

    def __init__(self, imagem):
        """Cria o arqueiro e o posiciona na frente do castelo"""
        self.imagem = imagem
        self.rect = imagem.get_rect()
        self.rect.x = posicao_inicial_x(
            ARQUEIRO_POSICAO_INICIAL, LARGURA_TELA, self.rect.width
        )
        self.rect.bottom = LINHA_CASTELO + 30

    def mover(self, teclas):
        """Move o arqueiro para os lados conforme as setas ou as teclas A / D."""
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.rect.x -= JOGADOR_VELOCIDADE
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.rect.x += JOGADOR_VELOCIDADE
        self.rect.x = limitar_valor(self.rect.x, 0, LARGURA_TELA - self.rect.width)

    def desenhar(self, tela):
        """Desenha o arqueiro na tela."""
        tela.blit(self.imagem, self.rect)
