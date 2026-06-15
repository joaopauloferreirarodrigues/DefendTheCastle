def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


def pode_atirar(tempo_atual, tempo_ultimo_tiro, intervalo):
    """Indica se já passou o tempo para atirar outra flecha"""
    return tempo_atual - tempo_ultimo_tiro >= intervalo


def quantidade_de_morcegos(numero_onda, base):
    """Quantidade de morcegos de uma onda cresce a cada três"""
    return base + numero_onda // 3


def venceu_o_jogo(numero_onda, ondas_totais):
    """Indica se o jogador passou de todas as ondas."""
    return numero_onda > ondas_totais


def calcular_posicao_central(largura_tela, largura_objeto):
    return (largura_tela - largura_objeto) // 2


def calcular_espaco_entre_morcegos(largura_tela, quantidade):
    """Retorna o espaçamento entre os morcegos de uma onda"""
    return largura_tela // quantidade
