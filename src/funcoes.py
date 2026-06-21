import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    BRANCO,
    CEU,
    PEDRA,
    MARROM,
    VERMELHO,
    AMARELO,
    VERDE,
    JOGADOR_VIDAS,
    INTERVALO_DISPARO,
    INIMIGOS_BASE,
    ORDEM_DOS_INIMIGOS,
    ONDA_MAXIMA,
    LINHA_CASTELO,
)

def calcular_pontos(pontos_atual, pontos_ganhos):
    """
    Soma os pontos ganhos a pontuacao atual.
    Parametros:
        pontos_atual (int): pontuacao que o jogador ja tem
        pontos_ganhos (int): pontos que ele ganhou que vão somar na pontuação dele
    Retorno:
        int: nova pontuacao.
    """
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """
    Diminui a vida com base no dano recebido.
    Serve tanto pro arqueiro quanto para os inimigos.
    Parametros:
        vida atual (int): vida antes do dano.
        dano (int): quanto de vida sera perdido.
    Retorno:
        int: a vida dele
    """
    return vida_atual - dano


def jogador_perdeu(vidas):
    """
    Fala se o jogador não tem mais vidas
    Parametros:
        vidas (int): vidas atuais do jogador
    Retorno:
        booleano True se as vidas chegaram a zero (ou menos)
    """
    return vidas <= 0

def limitar_valor(valor, minimo, maximo):
    """
    Mantem um valor dentro de um intervalo
    Usada para impedir o arqueiro de sair da tela
    Parametros:
        valor (int): valor a ser ajustado.
        minimo (int): menor valor permitido.
        maximo (int): maior valor permitido.
    Retorno:
        int: o valor preso entre minimo e maximo.
    """
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """
    Verifica se dois retangulos do Pygame estao se tocando.
    Parametros:
        retangulo_1 (Rect): primeiro retangulo.
        retangulo_2 (Rect): segundo retangulo.
    Retorno:
        bool: True se eles se sobrepoem.
    """
    return retangulo_1.colliderect(retangulo_2)


def pode_atirar(tempo_atual, tempo_ultimo_tiro, intervalo):
    """
    Indica se ja passou tempo suficiente para atirar outra flecha
    Parametros:
        tempo atual (int): tempo de agora, em milissegundos.
        tempo ultimo_tiro (int): tempo do ultimo tiro, em milissegundos.
        intervalo (int): espera minima entre tiros, em milissegundos.
    Retorno:
        bool: True se ja da para atirar de novo.
    """
    return tempo_atual - tempo_ultimo_tiro >= intervalo

def calcular_posicao_central(largura_tela, largura_objeto):
    """
    Calcula o x que deixa um objeto centralizado na horizontal.
    Parametros:
        largura_tela (int): largura da tela em pixels.
        largura_objeto (int): largura do objeto em pixels.
    Retorno:
        int: o x do canto esquerdo do objeto para ele ficar no centro.
    """
    return (largura_tela - largura_objeto) // 2


def posicao_inicial_x(posicao, largura_tela, largura_arqueiro):
    """
    Decide o x onde o arqueiro nasce.
    Parametros:
        posicao (str): "esquerda", "centro" ou "direita"
            (vem de ARQUEIRO_POSICAO_INICIAL no config).
        largura_tela (int): largura da tela em pixels.
        largura_arqueiro (int): largura do arqueiro em pixels.
    Retorno:
        int: o x do canto esquerdo do arqueiro. Qualquer valor diferente de
        "esquerda" e "direita" cai no centro.
    """
    if posicao == "esquerda":
        return 0
    if posicao == "direita":
        return largura_tela - largura_arqueiro
    return calcular_posicao_central(largura_tela, largura_arqueiro)

def quantidade_de_inimigos(numero_onda, base):
    """
    Calcula quantos inimigos uma onda tem.
    A quantidade aumenta de 1 em 1 a cada tres ondas, deixando o jogo mais
    dificil aos poucos.
    Parametros:
        numero_onda (int): numero da onda (comeca em 1).
        base (int): quantidade de inimigos da primeira onda.
    Retorno:
        int: quantos inimigos a onda tera.
    """
    return base + numero_onda // 3


def calcular_espaco_entre_inimigos(largura_tela, quantidade):
    """
    Calcula o espacamento horizontal entre os inimigos de uma onda.
    Parametros:
        largura_tela (int): largura da tela em pixels.
        quantidade (int): quantos inimigos tem na onda.
    Retorno:
        int: a distancia, em pixels, reservada para cada inimigo.
    """
    return largura_tela // quantidade

def tipo_da_onda(numero_onda, ordem):
    """
    Diz qual tipo de inimigo aparece em uma onda.
    A lista 'ordem' define a sequencia; quando ela acaba, recomeca do inicio.
    Parametros:
        numero onda (int): numero da onda (comeca em 1).
        ordem (list): lista de tipos, ex.: ["esqueleto", "morcego", "orc"]
            (vem de ORDEM_DOS_INIMIGOS no config).
    Retorno:
        str: o tipo do inimigo daquela onda ("esqueleto", "morcego" ou "orc").
    """
    indice = (numero_onda - 1) % len(ordem)
    return ordem[indice]


def venceu_o_jogo(numero_onda, ondas_totais):
    """
    Indica se o jogador passou de todas as ondas.
    Parametros:
        numero onda (int): onda em que o jogador esta.
        ondas totais (int): total de ondas do jogo (ONDA_MAXIMA no config).
    Retorno:
        bool: True se o jogador venceu (passou da ultima onda).
    """
    return numero_onda > ondas_totais

def nome_valido(nome):
    """
    Indica se o nome digitado pode ser usado.
    Parametros:
        nome (str): nome digitado pelo jogador.
    Retorno:
        bool: True se o nome nao e vazio nem so espacos.
    """
    return len(nome.strip()) > 0

def adicionar_caractere(nome, caractere, limite):
    """
    Acrescenta uma letra ao nome, respeitando o limite de tamanho.
    Parametros:
        nome (str): nome digitado ate agora.
        caractere (str): letra a acrescentar.
        limite (int): numero maximo de letras permitido.
    Retorno:
        str: o nome com a letra nova, ou o nome igual se ja atingiu o limite.
    """
    if len(nome) >= limite:
        return nome
    return nome + caractere


def remover_caractere(nome):
    """
    Apaga a ultima letra do nome (tecla backspace).
    Parametros:
        nome (str): nome digitado ate agora.
    Retorno:
        str: o nome sem a ultima letra (texto vazio continua vazio).
    """
    return nome[:-1]

def eh_novo_recorde(pontos, ranking):
    """
    Indica se uma pontuacao deve entrar no placar.
    Entra se o ranking estiver vazio, ou se a pontuacao for maior que a menor
    pontuacao que ja esta no ranking. Pontuacao zero ou negativa nunca entra.
    Parametros:
        pontos (int): pontuacao da partida.
        ranking (list): lista de (nome, pontos), do maior para o menor.
    Retorno:
        bool: True se a pontuacao deve entrar no placar.
    """
    if pontos <= 0:
        return False
    if len(ranking) == 0:
        return True
    menor_pontuacao = ranking[-1][1] 
    return pontos > menor_pontuacao


def pontos_da_entrada(entrada):
    """
    Pega os pontos de uma entrada do ranking. Serve para ordenar o placar.
    Parametros:
        entrada (tuple): uma dupla (nome, pontos).
    Retorno:
        int: os pontos dessa entrada.
    """
    return entrada[1]


def adicionar_ao_ranking(ranking, nome, pontos, limite):
    """
    Cria um novo ranking com (nome, pontos) incluido.
    O resultado fica ordenado do maior para o menor e cortado no limite.
    Parametros:
        ranking (list): ranking atual, lista de (nome, pontos).
        nome (str): nome do jogador.
        pontos (int): pontuacao do jogador.
        limite (int): quantas entradas o ranking guarda (MAX_RANKING no config).
    Retorno:
        list: o novo ranking ordenado e cortado no limite.
    """
    novo = list(ranking)
    novo.append((nome, pontos))
    novo.sort(key=pontos_da_entrada, reverse=True)
    return novo[:limite]


def melhor_pontuacao(ranking):
    """
    Pega o primeiro lugar do ranking.
    Parametros:
        ranking (list): lista de (nome, pontos), do maior para o menor.
    Retorno:
        tuple: (nome, pontos) do primeiro lugar, ou ("", 0) se estiver vazio.
    """
    if len(ranking) == 0:
        return ("", 0)
    return ranking[0]


def formatar_entrada_ranking(nome, pontos):
    """
    Monta a linha de texto que sera salva no arquivo do ranking.
    Parametros:
        nome (str): nome do jogador.
        pontos (int): pontuacao do jogador.
    Retorno:
        str: o texto no formato "nome;pontos".
    """
    return nome + ";" + str(pontos)


def interpretar_linha_ranking(linha):
    """
    Transforma uma linha do arquivo de volta em (nome, pontos).
    Parametros:
        linha (str): uma linha lida do arquivo, no formato "nome;pontos".
    Retorno:
        tuple: (nome, pontos), ou None se a linha estiver mal formada.
    """
    partes = linha.strip().split(";")
    if len(partes) != 2:
        return None
    nome = partes[0]
    if not partes[1].isdigit():
        return None
    return (nome, int(partes[1]))

def criar_inimigo(tipo, imagens, x, y):
    """
    Cria um inimigo do tipo pedido, na posicao (x, y).
    Parametros:
        tipo (str): "esqueleto", "morcego" ou "orc".
        imagens (dict): imagens ja carregadas (veja carregar_imagens em jogo.py).
        x (int): posicao horizontal onde o inimigo nasce.
        y (int): posicao vertical onde o inimigo nasce.
    Retorno:
        Esqueleto, Morcego ou Orc: o inimigo criado. Tipos desconhecidos viram
        morcego.
    """
    if tipo == "esqueleto":
        return Esqueleto(imagens["esqueleto"], x, y)
    if tipo == "orc":
        return Orc(imagens["orc"], x, y)
    return Morcego(imagens["morcego"], x, y)


def gerar_onda(numero_onda, imagens):
    """
    Cria a lista de inimigos de uma onda, espalhados na largura da tela.
    O tipo de inimigo (esqueleto, morcego ou orc) depende do numero da onda.
    Parametros:
        numero_onda (int): numero da onda (comeca em 1).
        imagens (dict): imagens ja carregadas dos inimigos.
    Retorno:
        list: a lista de inimigos da onda.
    """
    tipo = tipo_da_onda(numero_onda, ORDEM_DOS_INIMIGOS)
    quantidade = quantidade_de_inimigos(numero_onda, INIMIGOS_BASE)
    espaco = calcular_espaco_entre_inimigos(LARGURA_TELA, quantidade)

    inimigos = []
    for i in range(quantidade):
        x = espaco * i + (espaco // 2) - 20
        y = -60   
        inimigos.append(criar_inimigo(tipo, imagens, x, y))
    return inimigos

def iniciar_partida(imagens, tempo_atual):
    """
    Monta o estado inicial da partida.
    O estado e um dicionario que guarda tudo que o jogo precisa para funcionar
    (arqueiro, inimigos, flechas, pontos, vidas, onda, etc.).
    Parametros:
        imagens (dict): imagens ja carregadas de todos os personagens.
        tempo_atual (int): tempo de agora, em milissegundos.
    Retorno:
        dict: o estado inicial da partida.
    """
    return {
        "arqueiro": Arqueiro(imagens["arqueiro"]),
        "inimigos": gerar_onda(1, imagens),
        "flechas": [],
        "pontos": 0,
        "vidas": JOGADOR_VIDAS,
        "onda": 1,
        "tempo_ultimo_tiro": tempo_atual,
        "venceu": False,
        "imagens": imagens,
    }

def primeiro_inimigo_atingido(flecha, inimigos):
    """
    Procura o primeiro inimigo vivo que a flecha esta tocando.
    Parametros:
        flecha (Flecha): a flecha a verificar.
        inimigos (list): lista de inimigos na tela.
    Retorno:
        o inimigo atingido, ou None se a flecha nao acertou ninguem.
    """
    for inimigo in inimigos:
        if inimigo.vida > 0 and verificar_colisao(flecha.rect, inimigo.rect):
            return inimigo
    return None


def processar_acertos(flechas, inimigos):
    """
    Confere a colisao das flechas com os inimigos.
    Cada flecha atinge no maximo um inimigo e some ao acertar. Cada acerto tira
    1 de vida; o inimigo so morre (e da pontos) quando a vida chega a zero. Por
    isso o orc, que tem 2 de vida, precisa de 2 flechas.
    Parametros:
        flechas (list): flechas que estao na tela.
        inimigos (list): inimigos que estao na tela.
    Retorno:
        tuple: (flechas que continuam, inimigos vivos, pontos ganhos).
    """
    flechas_que_continuam = []
    pontos_ganhos = 0

    for flecha in flechas:
        inimigo = primeiro_inimigo_atingido(flecha, inimigos)
        if inimigo is None:
            flechas_que_continuam.append(flecha)
        else:
            inimigo.vida = tomar_dano(inimigo.vida, 1)
            if inimigo.vida <= 0:
                pontos_ganhos = pontos_ganhos + inimigo.pontos

    inimigos_vivos = []
    for inimigo in inimigos:
        if inimigo.vida > 0:
            inimigos_vivos.append(inimigo)

    return flechas_que_continuam, inimigos_vivos, pontos_ganhos

def processar_inimigos_no_castelo(inimigos):
    """
    Separa os inimigos que chegaram ao castelo dos que continuam descendo.
    Parametros:
        inimigos (list): inimigos que estao na tela.
    Retorno:
        tuple: (lista dos que continuam descendo, quantidade dos que chegaram).
    """
    continuam = []
    chegaram = 0
    for inimigo in inimigos:
        if inimigo.chegou_ao_castelo():
            chegaram = chegaram + 1
        else:
            continuam.append(inimigo)
    return continuam, chegaram

def atualizar_partida(jogo, teclas, tempo_atual):
    """
    Atualiza um quadro do jogo (movimento, tiros, acertos, ondas e vidas).
    Parametros:
        jogo (dict): estado atual da partida (veja iniciar_partida).
        teclas: teclas pressionadas agora (pygame.key.get_pressed()).
        tempo_atual (int): tempo de agora, em milissegundos.
    Retorno:
        str: "jogando" se a partida continua, ou "fim" se acabou.
    """
    jogo["arqueiro"].mover(teclas)

    if pode_atirar(tempo_atual, jogo["tempo_ultimo_tiro"], INTERVALO_DISPARO):
        x_centro = jogo["arqueiro"].rect.centerx
        y_base = jogo["arqueiro"].rect.top
        jogo["flechas"].append(Flecha(jogo["imagens"]["flecha"], x_centro, y_base))
        jogo["tempo_ultimo_tiro"] = tempo_atual

    for flecha in jogo["flechas"]:
        flecha.mover()
    flechas_na_tela = []
    for flecha in jogo["flechas"]:
        if not flecha.saiu_da_tela():
            flechas_na_tela.append(flecha)
    jogo["flechas"] = flechas_na_tela

    for inimigo in jogo["inimigos"]:
        inimigo.mover()

    jogo["flechas"], jogo["inimigos"], ganhos = processar_acertos(
        jogo["flechas"], jogo["inimigos"]
    )
    jogo["pontos"] = calcular_pontos(jogo["pontos"], ganhos)

    jogo["inimigos"], chegaram = processar_inimigos_no_castelo(jogo["inimigos"])
    jogo["vidas"] = tomar_dano(jogo["vidas"], chegaram)

    if jogador_perdeu(jogo["vidas"]):
        return "fim"
    
    if len(jogo["inimigos"]) == 0:
        jogo["onda"] = jogo["onda"] + 1
        if venceu_o_jogo(jogo["onda"], ONDA_MAXIMA):
            jogo["venceu"] = True
            return "fim"
        jogo["inimigos"] = gerar_onda(jogo["onda"], jogo["imagens"])

    return "jogando"

def desenhar_cenario(tela):
    """
    Desenha o ceu, o castelo parte de baixo da tela
    Parametros:
        tela (Surface): a tela onde o jogo e desenhado
    Retorno:
        A função só desenha na tela
    """
    tela.fill(CEU)
    pygame.draw.rect(tela, PEDRA, (0, LINHA_CASTELO, LARGURA_TELA, ALTURA_TELA - LINHA_CASTELO))
    for x in range(0, LARGURA_TELA, 52):
        pygame.draw.rect(tela, PEDRA, (x, LINHA_CASTELO - 18, 26, 18))
    pygame.draw.rect(tela, MARROM, (0, ALTURA_TELA - 24, LARGURA_TELA, 24))


def desenhar_texto_central(tela, fonte, texto, y, cor):
    """
    Desenha um texto centralizado na horizontal.
    Parametros:
        tela (Surface): a tela onde o texto e desenhado.
        fonte (Font): a fonte usada para escrever.
        texto (str): o texto a mostrar.
        y (int): altura (em pixels) onde o texto fica.
        cor (tuple): cor do texto, no formato (R, G, B).
    Retorno:
        Nenhum. A funcao apenas desenha na tela.
    """
    imagem_texto = fonte.render(texto, True, cor)
    rect_texto = imagem_texto.get_rect(center=(LARGURA_TELA // 2, y))
    tela.blit(imagem_texto, rect_texto)


def desenhar_hud(tela, fonte, pontos, recorde_nome, recorde_pontos, vidas, onda):
    """
    Mostra pontos, recorde, onda e vidas no topo da tela.
    Parametros:
        tela (Surface): a tela onde desenhar.
        fonte (Font): fonte usada nos textos.
        pontos (int): pontuacao atual.
        recorde_nome (str): nome do primeiro lugar do ranking.
        recorde_pontos (int): pontuacao do primeiro lugar.
        vidas (int): vidas atuais do jogador.
        onda (int): numero da onda atual.
    Retorno:
        Nenhum. A funcao apenas desenha na tela.
    """
    tela.blit(fonte.render(f"Pontos: {pontos}", True, BRANCO), (10, 10))
    tela.blit(fonte.render(f"Recorde: {recorde_nome} {recorde_pontos}", True, AMARELO), (10, 35))
    tela.blit(fonte.render(f"Onda: {onda}/{ONDA_MAXIMA}", True, BRANCO), (LARGURA_TELA - 150, 10))
    for i in range(vidas):
        pygame.draw.rect(tela, VERMELHO, (10 + i * 26, 62, 18, 18))


def desenhar_ranking(tela, fonte, ranking, y_inicial):
    """
    Desenha o placar (lista de nomes e pontos), uma linha embaixo da outra.
    Parametros:
        tela (Surface): a tela onde desenhar.
        fonte (Font): fonte usada nos textos.
        ranking (list): lista de (nome, pontos), do maior para o menor.
        y_inicial (int): altura (em pixels) onde o titulo "RANKING" comeca.
    Retorno:
        Nenhum. A funcao apenas desenha na tela.
    """
    desenhar_texto_central(tela, fonte, "RANKING", y_inicial, AMARELO)
    for i in range(len(ranking)):
        nome, pontos = ranking[i]
        linha = f"{i + 1}. {nome} - {pontos}"
        desenhar_texto_central(tela, fonte, linha, y_inicial + 30 + i * 26, BRANCO)

def desenhar_tela_nome(tela, fonte_grande, fonte, nome_digitado, ranking):
    """
    Desenha a tela inicial, onde o jogador digita o nome antes de comecar.
    Parametros:
        tela (Surface): a tela onde desenhar.
        fonte_grande (Font): fonte dos titulos.
        fonte (Font): fonte dos textos menores.
        nome_digitado (str): nome que o jogador esta digitando.
        ranking (list): ranking a mostrar embaixo.
    Retorno:
        Nenhum. A funcao apenas desenha na tela.
    """
    tela.fill(CEU)
    desenhar_texto_central(tela, fonte_grande, "DEFEND THE CASTLE", 110, BRANCO)
    desenhar_texto_central(tela, fonte, "Digite seu nome e aperte ENTER para jogar:", 190, BRANCO)
    desenhar_texto_central(tela, fonte_grande, nome_digitado + "_", 240, VERDE)
    desenhar_ranking(tela, fonte, ranking, 330)


def desenhar_tela_fim(tela, fonte_grande, fonte, venceu, nome, pontos, ranking):
    """
    Desenha a tela de fim de jogo, com o resultado e o placar.
    Parametros:
        tela (Surface): a tela onde desenhar.
        fonte_grande (Font): fonte dos titulos.
        fonte (Font): fonte dos textos menores.
        venceu (bool): True se o jogador venceu, False se perdeu.
        nome (str): nome do jogador.
        pontos (int): pontuacao final.
        ranking (list): ranking a mostrar.
    Retorno:
        Nenhum. A funcao apenas desenha na tela.
    """
    tela.fill(CEU)
    if venceu:
        desenhar_texto_central(tela, fonte_grande, "VITORIA!", 110, VERDE)
    else:
        desenhar_texto_central(tela, fonte_grande, "FIM DE JOGO", 110, VERMELHO)
    desenhar_texto_central(tela, fonte, f"{nome}, voce fez {pontos} pontos", 180, BRANCO)
    desenhar_ranking(tela, fonte, ranking, 250)
    desenhar_texto_central(tela, fonte, "Aperte ESPACO para jogar de novo", 540, AMARELO)


def desenhar_partida(tela, fonte, jogo, recorde_nome, recorde_pontos):
    """
    Desenha a cena de uma partida em andamento.
    Parametros:
        tela (Surface): a tela onde desenhar.
        fonte (Font): fonte usada no HUD.
        jogo (dict): estado atual da partida.
        recorde_nome (str): nome do primeiro lugar do ranking.
        recorde_pontos (int): pontuacao do primeiro lugar.
    Retorno:
        Nenhum. A funcao apenas desenha na tela.
    """
    desenhar_cenario(tela)
    for inimigo in jogo["inimigos"]:
        inimigo.desenhar(tela)
    for flecha in jogo["flechas"]:
        flecha.desenhar(tela)
    jogo["arqueiro"].desenhar(tela)
    desenhar_hud(tela, fonte, jogo["pontos"], recorde_nome, recorde_pontos, jogo["vidas"], jogo["onda"])

from src.arqueiro import Arqueiro
from src.esqueleto import Esqueleto
from src.morcego import Morcego
from src.orc import Orc
from src.flecha import Flecha
