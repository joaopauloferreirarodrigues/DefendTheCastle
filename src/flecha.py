from src.config import FLECHA_VELOCIDADE


class Flecha:
    def __init__(self, imagem, x_centro, y_base):
        """
        Cria a flecha logo acima do arqueiro.
        Parametros:
            imagem (Surface): figura da flecha, ja carregada.
            x_centro (int): x do centro do arqueiro
            y_base (int): y do topo do arqueiro
        """
        self.imagem = imagem
        self.rect = imagem.get_rect()
        self.rect.centerx = x_centro
        self.rect.bottom = y_base

    def mover(self):
        """
        Move a flecha para cima.
        Retorno:
            A função apenas muda a posicao da flecha.
        """
        self.rect.y -= FLECHA_VELOCIDADE

    def saiu_da_tela(self):
        """
        Indica se a flecha ja saiu pela parte de cima da tela.
        Retorno:
            Um booleano True se a flecha passou do topo da tela.
        """
        return self.rect.bottom <= 0

    def desenhar(self, tela):
        """
        Desenha a flecha na tela.
        Parametros:
            tela (Surface): a tela onde desenhar.
        Retorno:
            A função apenas desenha na tela.
        """
        tela.blit(self.imagem, self.rect)
