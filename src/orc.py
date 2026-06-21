from src.config import (
    ORC_VELOCIDADE,
    ORC_VIDA,
    ORC_PONTOS,
    LINHA_CASTELO,
)

class Orc:
    def __init__(self, imagem, x, y):
        """
        Cria um orc na posicao (x, y).
        Parametros:
            imagem (Surface): figura do orc, ja carregada.
            x (int): posicao horizontal onde ele nasce.
            y (int): posicao vertical onde ele nasce.
        """
        self.imagem = imagem
        self.rect = imagem.get_rect(topleft=(x, y))
        self.pos_y = float(y)
        self.velocidade_y = ORC_VELOCIDADE   
        self.vida = ORC_VIDA                
        self.pontos = ORC_PONTOS             

    def mover(self):
        """
        Faz o orc descer um pouco, em linha reta.
        Retorno:
            Nenhum. A funcao apenas muda a posicao do orc.
        """
        self.pos_y += self.velocidade_y
        self.rect.y = round(self.pos_y)

    def chegou_ao_castelo(self):
        """
        Indica se o orc ja alcancou o castelo.
        Retorno:
            bool: True se ele chegou na altura do castelo.
        """
        return self.rect.bottom >= LINHA_CASTELO

    def desenhar(self, tela):
        """
        Desenha o orc na tela.
        Parametros:
            tela (Surface): a tela onde desenhar.
        Retorno:
            Nenhum, a funcao apenas desenha na tela.
        """
        tela.blit(self.imagem, self.rect)
