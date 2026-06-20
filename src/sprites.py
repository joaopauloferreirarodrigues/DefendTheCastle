import pygame


def carregar_sprite(caminho, escala=1):
    """
    Carrega a imagem de um personagem (PNG ja com fundo transparente).
    Parametros:
        caminho (str): endereco do arquivo .png (veja os IMAGEM_* no config).
        escala (float): tamanho final. 1 mantem o original, 0.5 deixa metade,
            2 deixa o dobro.
    Retorno:
        Surface: a imagem pronta para desenhar, ja no tamanho da escala.
    """
    imagem = pygame.image.load(caminho).convert_alpha()
    if escala != 1:
        nova_largura = int(imagem.get_width() * escala)
        nova_altura = int(imagem.get_height() * escala)
        imagem = pygame.transform.scale(imagem, (nova_largura, nova_altura))
    return imagem
