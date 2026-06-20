from src.config import (
    ESQUELETO_VELOCIDADE,
    ESQUELETO_VIDA,
    ESQUELETO_PONTOS,
    LINHA_CASTELO,
)


class Esqueleto:
    def __init__(self, imagem, x, y):
        """
        Cria um esqueleto
        """
        self.imagem = imagem
        self.rect = imagem.get_rect(topleft=(x, y))
        self.pos_y = float(y)
        self.velocidade_y = ESQUELETO_VELOCIDADE   
        self.vida = ESQUELETO_VIDA                 
        self.pontos = ESQUELETO_PONTOS           

    def mover(self):
        """
        Faz o esqueleto descer um pouco, em linha reta.
        Retorno:
            A função apenas muda a posicao do esqueleto.
        """
        self.pos_y += self.velocidade_y
        self.rect.y = round(self.pos_y)

    def chegou_ao_castelo(self):
        """
        Indica se o esqueleto ja alcancou o castelo.
        Retorno:
            Um booleano True se ele chegou na altura do castelo.
        """
        return self.rect.bottom >= LINHA_CASTELO

    def desenhar(self, tela):
        """
        Desenha o esqueleto na tela.
        Parametros:
            tela (Surface): a tela onde desenhar.
        Retorno:
            A função apenas desenha na tela.
        """
        tela.blit(self.imagem, self.rect)
