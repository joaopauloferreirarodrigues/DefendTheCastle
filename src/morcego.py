from src.config import (
    MORCEGO_VELOCIDADE,
    MORCEGO_VIDA,
    MORCEGO_PONTOS,
    LINHA_CASTELO,
)


class Morcego:
    def __init__(self, imagem, x, y):
        """
        Cria um morcego na posicao (x, y).
        Parametros:
            imagem (Surface): figura do morcego, ja carregada.
            x (int): posicao horizontal onde ele nasce.
            y (int): posicao vertical onde ele nasce.
        """
        self.imagem = imagem
        self.rect = imagem.get_rect(topleft=(x, y))

        self.pos_y = float(y)
        self.velocidade_y = MORCEGO_VELOCIDADE   
        self.vida = MORCEGO_VIDA                 
        self.pontos = MORCEGO_PONTOS             

    def mover(self):
        """
        Faz o morcego descer um pouco, em linha reta.
        Retorno:
            Nenhum. A funcao apenas muda a posicao do morcego.
        """
        self.pos_y += self.velocidade_y
        self.rect.y = round(self.pos_y)

    def chegou_ao_castelo(self):
        """
        Indica se o morcego ja alcancou o castelo.
        Retorno:
            bool: True se ele chegou na altura do castelo.
        """
        return self.rect.bottom >= LINHA_CASTELO

    def desenhar(self, tela):
        """
        Desenha o morcego na tela.
        Parametros:
            tela (Surface): a tela onde desenhar.
        Retorno:
            Nenhum. A funcao apenas desenha na tela.
        """
        tela.blit(self.imagem, self.rect)
