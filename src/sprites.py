import pygame


def pegar_sprite(local_arquivo, x, y, largura, altura, escala=1):
    sheet = pygame.image.load(local_arquivo).convert()
    imagem = pygame.Surface((largura, altura))
    imagem.blit(sheet, (0, 0), (x, y, largura, altura))
    cor_do_fundo = imagem.get_at((0, 0))
    imagem.set_colorkey(cor_do_fundo)
    if escala != 1:
        nova_largura = int(largura * escala)
        nova_altura = int(altura * escala)
        imagem = pygame.transform.scale(imagem, (nova_largura, nova_altura))
    return imagem


def eh_fundo(cor):
    vermelho, verde, azul = cor[0], cor[1], cor[2]
    maior = max(vermelho, verde, azul)
    menor = min(vermelho, verde, azul)
    neutro = (maior - menor) <= 22
    claro = menor >= 95
    return neutro and claro


def limpar_fundo(imagem, largura, altura):
    transparente = (0, 0, 0, 0)
    visitados = set()
    pilha = [(0, 0), (largura - 1, 0), (0, altura - 1), (largura - 1, altura - 1)]
    while len(pilha) > 0:
        ponto = pilha.pop()
        px, py = ponto
        dentro = 0 <= px < largura and 0 <= py < altura
        if dentro and ponto not in visitados:
            visitados.add(ponto)
            if eh_fundo(imagem.get_at((px, py))):
                imagem.set_at((px, py), transparente)
                pilha.append((px + 1, py))
                pilha.append((px - 1, py))
                pilha.append((px, py + 1))
                pilha.append((px, py - 1))


def caixa_do_desenho(imagem, largura, altura):
    menor_x = largura
    menor_y = altura
    maior_x = -1
    maior_y = -1
    py = 0
    while py < altura:
        px = 0
        while px < largura:
            if imagem.get_at((px, py))[3] > 0:
                if px < menor_x:
                    menor_x = px
                if px > maior_x:
                    maior_x = px
                if py < menor_y:
                    menor_y = py
                if py > maior_y:
                    maior_y = py
            px = px + 1
        py = py + 1
    return menor_x, menor_y, maior_x, maior_y


def pegar_sprite_sem_fundo(local_arquivo, x, y, largura, altura, escala=1):
    base = pegar_sprite(local_arquivo, x, y, largura, altura, 1)

    imagem = pygame.Surface((largura, altura), pygame.SRCALPHA)
    imagem.blit(base, (0, 0))

    limpar_fundo(imagem, largura, altura)

    menor_x, menor_y, maior_x, maior_y = caixa_do_desenho(imagem, largura, altura)
    if maior_x >= menor_x and maior_y >= menor_y:
        largura_real = maior_x - menor_x + 1
        altura_real = maior_y - menor_y + 1
        recorte = pygame.Surface((largura_real, altura_real), pygame.SRCALPHA)
        recorte.blit(imagem, (0, 0), (menor_x, menor_y, largura_real, altura_real))
        imagem = recorte

    if escala != 1:
        nova_largura = int(imagem.get_width() * escala)
        nova_altura = int(imagem.get_height() * escala)
        imagem = pygame.transform.scale(imagem, (nova_largura, nova_altura))

    return imagem
