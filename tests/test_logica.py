import pygame

from src.funcoes import (
    # regras
    calcular_pontos,
    tomar_dano,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    pode_atirar,
    calcular_posicao_central,
    posicao_inicial_x,
    quantidade_de_inimigos,
    calcular_espaco_entre_inimigos,
    tipo_da_onda,
    venceu_o_jogo,
    nome_valido,
    adicionar_caractere,
    remover_caractere,
    eh_novo_recorde,
    adicionar_ao_ranking,
    pontos_da_entrada,
    melhor_pontuacao,
    formatar_entrada_ranking,
    interpretar_linha_ranking,
    criar_inimigo,
    gerar_onda,
    iniciar_partida,
    primeiro_inimigo_atingido,
    processar_acertos,
    processar_inimigos_no_castelo,
)
from src.arqueiro import Arqueiro
from src.esqueleto import Esqueleto
from src.morcego import Morcego
from src.orc import Orc
from src.flecha import Flecha
from src.dados import (
    salvar_recorde,
    carregar_recorde,
    salvar_ranking,
    carregar_ranking,
)
from src.config import (
    LARGURA_TELA,
    LINHA_CASTELO,
    JOGADOR_VELOCIDADE,
    JOGADOR_VIDAS,
    ESQUELETO_VELOCIDADE,
    MORCEGO_VELOCIDADE,
    ORC_VELOCIDADE,
    ORC_VIDA,
    ESQUELETO_PONTOS,
    ORC_PONTOS,
    ORDEM_DOS_INIMIGOS,
)


# Imagem falsa (so um quadrado) para criar personagens nos testes.
def imagem_falsa(largura=40, altura=40):
    return pygame.Surface((largura, altura))


# Dicionario de imagens falsas (mesmo formato que carregar_imagens devolve).
def imagens_falsas():
    return {
        "arqueiro": imagem_falsa(),
        "esqueleto": imagem_falsa(),
        "morcego": imagem_falsa(),
        "orc": imagem_falsa(),
        "flecha": imagem_falsa(10, 40),
    }


# ============================================================================
#  PARTE 1 - REGRAS (PONTOS E VIDAS)
# ============================================================================
def test_calcular_pontos_varios_casos():
    assert calcular_pontos(0, 10) == 10
    assert calcular_pontos(50, 20) == 70
    assert calcular_pontos(100, 0) == 100


def test_tomar_dano_varios_casos():
    assert tomar_dano(3, 1) == 2
    assert tomar_dano(2, 2) == 0
    assert tomar_dano(1, 0) == 1


def test_jogador_perdeu_com_zero_ou_menos():
    assert jogador_perdeu(0) is True
    assert jogador_perdeu(-1) is True


def test_jogador_nao_perdeu_com_vidas():
    assert not jogador_perdeu(1)
    assert not jogador_perdeu(3)


# ----- movimento e colisao --------------------------------------------------
def test_limitar_valor_abaixo_do_minimo():
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    assert limitar_valor(50, 0, 100) == 50


def test_verificar_colisao_quando_encostam():
    a = pygame.Rect(0, 0, 50, 50)
    b = pygame.Rect(25, 25, 50, 50)
    assert verificar_colisao(a, b) is True


def test_verificar_colisao_quando_estao_longe():
    a = pygame.Rect(0, 0, 10, 10)
    b = pygame.Rect(500, 500, 10, 10)
    assert not verificar_colisao(a, b)


def test_pode_atirar_quando_passou_o_intervalo():
    assert pode_atirar(1000, 500, 400) is True


def test_nao_pode_atirar_antes_do_intervalo():
    assert not pode_atirar(700, 500, 400)


# ----- posicao inicial do arqueiro ------------------------------------------
def test_calcular_posicao_central():
    assert calcular_posicao_central(800, 40) == 380


def test_posicao_inicial_esquerda():
    assert posicao_inicial_x("esquerda", 800, 40) == 0


def test_posicao_inicial_direita():
    assert posicao_inicial_x("direita", 800, 40) == 760


def test_posicao_inicial_centro():
    assert posicao_inicial_x("centro", 800, 40) == 380


def test_posicao_inicial_esquerda_nao_e_centro():
    assert not posicao_inicial_x("esquerda", 800, 40) == posicao_inicial_x("centro", 800, 40)


# ----- ondas de inimigos ----------------------------------------------------
def test_quantidade_de_inimigos_cresce_por_onda():
    assert quantidade_de_inimigos(1, 2) == 2
    assert quantidade_de_inimigos(3, 2) == 3
    assert quantidade_de_inimigos(6, 2) == 4


def test_calcular_espaco_entre_inimigos():
    assert calcular_espaco_entre_inimigos(800, 4) == 200
    assert calcular_espaco_entre_inimigos(800, 2) == 400


def test_tipo_da_onda_segue_a_ordem():
    ordem = ["esqueleto", "morcego", "orc"]
    assert tipo_da_onda(1, ordem) == "esqueleto"   # esqueleto e o primeiro
    assert tipo_da_onda(2, ordem) == "morcego"     # depois os morcegos
    assert tipo_da_onda(3, ordem) == "orc"
    assert tipo_da_onda(4, ordem) == "esqueleto"   # a lista recomeca


def test_primeira_onda_nao_e_morcego():
    # O esqueleto deve ser o primeiro inimigo, nao o morcego.
    assert not tipo_da_onda(1, ORDEM_DOS_INIMIGOS) == "morcego"


def test_venceu_o_jogo_apos_ultima_onda():
    assert venceu_o_jogo(11, 10) is True


def test_nao_venceu_durante_o_jogo():
    assert not venceu_o_jogo(5, 10)


# ----- velocidade dos inimigos (regra pedida) -------------------------------
def test_ordem_de_velocidade_dos_inimigos():
    # O orc e o mais lento de todos; o morcego e o mais rapido.
    # Ordem: orc < esqueleto < morcego.
    assert ORC_VELOCIDADE < ESQUELETO_VELOCIDADE
    assert ESQUELETO_VELOCIDADE < MORCEGO_VELOCIDADE


# ----- nome do jogador ------------------------------------------------------
def test_nome_valido_com_texto():
    assert nome_valido("Joao") is True


def test_nome_invalido_quando_vazio_ou_espacos():
    assert not nome_valido("")
    assert not nome_valido("    ")


def test_adicionar_caractere():
    assert adicionar_caractere("Joa", "o", 10) == "Joao"


def test_adicionar_caractere_respeita_limite():
    cheio = "ABCDEFGHIJ"   # 10 letras
    assert adicionar_caractere(cheio, "K", 10) == cheio


def test_remover_caractere():
    assert remover_caractere("Joao") == "Joa"
    assert remover_caractere("") == ""


# ----- ranking --------------------------------------------------------------
def test_eh_novo_recorde_com_ranking_vazio():
    assert eh_novo_recorde(10, []) is True


def test_eh_novo_recorde_quando_supera_o_menor():
    ranking = [("A", 100), ("B", 30)]
    assert eh_novo_recorde(50, ranking) is True


def test_nao_e_recorde_com_pontuacao_zero():
    assert not eh_novo_recorde(0, [])


def test_nao_e_recorde_quando_nao_supera_o_menor():
    ranking = [("A", 100), ("B", 80)]
    assert not eh_novo_recorde(50, ranking)


def test_adicionar_ao_ranking_ordena_do_maior_para_o_menor():
    ranking = [("A", 100), ("B", 50)]
    novo = adicionar_ao_ranking(ranking, "C", 80, 5)
    assert novo[0] == ("A", 100)
    assert novo[1] == ("C", 80)
    assert novo[2] == ("B", 50)


def test_adicionar_ao_ranking_respeita_o_limite():
    ranking = [("A", 100), ("B", 90), ("C", 80)]
    novo = adicionar_ao_ranking(ranking, "D", 10, 3)
    assert len(novo) == 3
    assert not ("D", 10) in novo   # nao cabe no top 3


def test_pontos_da_entrada():
    assert pontos_da_entrada(("Joao", 120)) == 120
    assert pontos_da_entrada(("Maria", 0)) == 0


def test_melhor_pontuacao_com_ranking_vazio():
    assert melhor_pontuacao([]) == ("", 0)


def test_melhor_pontuacao_pega_o_primeiro():
    assert melhor_pontuacao([("A", 100), ("B", 50)]) == ("A", 100)


def test_formatar_entrada_ranking():
    assert formatar_entrada_ranking("Joao", 120) == "Joao;120"


def test_interpretar_linha_ranking_valida():
    assert interpretar_linha_ranking("Joao;120") == ("Joao", 120)


def test_interpretar_linha_ranking_invalida():
    assert interpretar_linha_ranking("linha sem ponto e virgula") is None
    assert interpretar_linha_ranking("Joao;abc") is None


# ============================================================================
#  PARTE 2 - FLUXO DA PARTIDA
# ============================================================================
def test_criar_inimigo_cria_o_tipo_certo():
    imagens = imagens_falsas()
    assert isinstance(criar_inimigo("esqueleto", imagens, 0, 0), Esqueleto)
    assert isinstance(criar_inimigo("morcego", imagens, 0, 0), Morcego)
    assert isinstance(criar_inimigo("orc", imagens, 0, 0), Orc)


def test_criar_esqueleto_nao_e_orc():
    inimigo = criar_inimigo("esqueleto", imagens_falsas(), 0, 0)
    assert not isinstance(inimigo, Orc)


def test_gerar_onda_tem_a_quantidade_certa():
    inimigos = gerar_onda(1, imagens_falsas())
    assert len(inimigos) == 2
    inimigos = gerar_onda(6, imagens_falsas())
    assert len(inimigos) == 4


def test_gerar_primeira_onda_e_de_esqueletos():
    inimigos = gerar_onda(1, imagens_falsas())
    assert isinstance(inimigos[0], Esqueleto)


def test_iniciar_partida_tem_o_estado_certo():
    jogo = iniciar_partida(imagens_falsas(), 0)
    assert jogo["pontos"] == 0
    assert jogo["vidas"] == JOGADOR_VIDAS
    assert jogo["onda"] == 1
    assert jogo["flechas"] == []
    assert not jogo["venceu"]


def test_primeiro_inimigo_atingido_quando_acerta():
    esqueleto = Esqueleto(imagem_falsa(), 100, 100)
    flecha = Flecha(imagem_falsa(10, 40), esqueleto.rect.centerx, esqueleto.rect.centery + 20)
    assert primeiro_inimigo_atingido(flecha, [esqueleto]) is esqueleto


def test_primeiro_inimigo_atingido_quando_erra():
    morcego = Morcego(imagem_falsa(), 0, 0)
    flecha = Flecha(imagem_falsa(10, 40), 700, 500)   # bem longe
    assert primeiro_inimigo_atingido(flecha, [morcego]) is None


def test_processar_acertos_quando_acerta_esqueleto():
    esqueleto = Esqueleto(imagem_falsa(), 100, 100)
    flecha = Flecha(imagem_falsa(10, 40), esqueleto.rect.centerx, esqueleto.rect.centery + 20)
    flechas, inimigos, pontos = processar_acertos([flecha], [esqueleto])
    assert pontos == ESQUELETO_PONTOS
    assert len(inimigos) == 0      # esqueleto morre com 1 tiro
    assert len(flechas) == 0       # flecha some ao acertar


def test_processar_acertos_quando_erra():
    morcego = Morcego(imagem_falsa(), 0, 0)
    flecha = Flecha(imagem_falsa(10, 40), 700, 500)   # bem longe
    flechas, inimigos, pontos = processar_acertos([flecha], [morcego])
    assert pontos == 0
    assert len(inimigos) == 1      # morcego continua
    assert len(flechas) == 1       # flecha continua


def test_orc_sobrevive_a_um_tiro():
    orc = Orc(imagem_falsa(), 100, 100)
    flecha = Flecha(imagem_falsa(10, 40), orc.rect.centerx, orc.rect.centery + 20)
    flechas, inimigos, pontos = processar_acertos([flecha], [orc])
    assert pontos == 0             # ainda nao morreu, nao deu pontos
    assert len(inimigos) == 1      # orc continua vivo
    assert inimigos[0].vida == 1   # perdeu 1 de vida (de 2 para 1)
    assert not len(flechas) == 1   # a flecha foi consumida no acerto


def test_orc_morre_com_dois_tiros():
    orc = Orc(imagem_falsa(), 100, 100)
    # primeiro tiro
    f1 = Flecha(imagem_falsa(10, 40), orc.rect.centerx, orc.rect.centery + 20)
    _, inimigos, pontos1 = processar_acertos([f1], [orc])
    assert pontos1 == 0
    # segundo tiro
    f2 = Flecha(imagem_falsa(10, 40), orc.rect.centerx, orc.rect.centery + 20)
    _, inimigos, pontos2 = processar_acertos([f2], inimigos)
    assert pontos2 == ORC_PONTOS   # agora sim deu pontos
    assert len(inimigos) == 0      # orc morreu no segundo tiro


def test_processar_inimigos_no_castelo():
    perto = Morcego(imagem_falsa(), 0, LINHA_CASTELO)   # ja chegou
    longe = Morcego(imagem_falsa(), 0, 0)               # ainda no topo
    continuam, chegaram = processar_inimigos_no_castelo([perto, longe])
    assert chegaram == 1
    assert len(continuam) == 1


def test_nenhum_inimigo_chega_quando_estao_no_topo():
    inimigos = [Morcego(imagem_falsa(), 0, 0), Esqueleto(imagem_falsa(), 50, 0)]
    continuam, chegaram = processar_inimigos_no_castelo(inimigos)
    assert chegaram == 0
    assert len(continuam) == 2


# ============================================================================
#  PARTE 3 - CLASSES (ARQUEIRO, ESQUELETO, MORCEGO, ORC, FLECHA)
# ============================================================================
def test_arqueiro_move_para_a_direita():
    arqueiro = Arqueiro(imagem_falsa())
    x_antes = arqueiro.rect.x
    teclas = {pygame.K_RIGHT: True, pygame.K_d: False, pygame.K_LEFT: False, pygame.K_a: False}
    arqueiro.mover(teclas)
    assert arqueiro.rect.x == x_antes + JOGADOR_VELOCIDADE


def test_arqueiro_move_para_a_esquerda():
    arqueiro = Arqueiro(imagem_falsa())
    x_antes = arqueiro.rect.x
    teclas = {pygame.K_LEFT: True, pygame.K_a: False, pygame.K_RIGHT: False, pygame.K_d: False}
    arqueiro.mover(teclas)
    assert arqueiro.rect.x == x_antes - JOGADOR_VELOCIDADE


def test_arqueiro_nao_sai_da_tela_pela_esquerda():
    arqueiro = Arqueiro(imagem_falsa())
    arqueiro.rect.x = 0
    teclas = {pygame.K_LEFT: True, pygame.K_a: False, pygame.K_RIGHT: False, pygame.K_d: False}
    arqueiro.mover(teclas)
    assert not arqueiro.rect.x < 0


def test_arqueiro_nao_sai_da_tela_pela_direita():
    arqueiro = Arqueiro(imagem_falsa())
    arqueiro.rect.right = LARGURA_TELA
    teclas = {pygame.K_RIGHT: True, pygame.K_d: False, pygame.K_LEFT: False, pygame.K_a: False}
    arqueiro.mover(teclas)
    assert not arqueiro.rect.right > LARGURA_TELA


# ----- esqueleto ------------------------------------------------------------
def test_esqueleto_desce():
    esqueleto = Esqueleto(imagem_falsa(), 0, 0)
    y_antes = esqueleto.rect.y
    esqueleto.mover()
    assert esqueleto.rect.y > y_antes


def test_esqueleto_chegou_ao_castelo():
    esqueleto = Esqueleto(imagem_falsa(), 0, LINHA_CASTELO)
    assert esqueleto.chegou_ao_castelo() is True


def test_esqueleto_ainda_nao_chegou_ao_castelo():
    esqueleto = Esqueleto(imagem_falsa(), 0, 0)
    assert not esqueleto.chegou_ao_castelo()


# ----- morcego --------------------------------------------------------------
def test_morcego_desce():
    morcego = Morcego(imagem_falsa(), 0, 0)
    y_antes = morcego.rect.y
    morcego.mover()
    assert morcego.rect.y > y_antes


def test_morcego_chegou_ao_castelo():
    morcego = Morcego(imagem_falsa(), 0, LINHA_CASTELO)
    assert morcego.chegou_ao_castelo() is True


def test_morcego_ainda_nao_chegou_ao_castelo():
    morcego = Morcego(imagem_falsa(), 0, 0)
    assert not morcego.chegou_ao_castelo()


# ----- orc ------------------------------------------------------------------
def test_orc_desce():
    orc = Orc(imagem_falsa(), 0, 0)
    y_antes = orc.rect.y
    orc.mover()
    assert orc.rect.y > y_antes


def test_orc_comeca_com_duas_vidas():
    orc = Orc(imagem_falsa(), 0, 0)
    assert orc.vida == ORC_VIDA
    assert orc.vida == 2


def test_orc_chegou_ao_castelo():
    orc = Orc(imagem_falsa(), 0, LINHA_CASTELO)
    assert orc.chegou_ao_castelo() is True


# ----- flecha ---------------------------------------------------------------
def test_flecha_sobe():
    flecha = Flecha(imagem_falsa(10, 40), 100, 300)
    y_antes = flecha.rect.y
    flecha.mover()
    assert flecha.rect.y < y_antes


def test_flecha_saiu_da_tela():
    flecha = Flecha(imagem_falsa(10, 40), 100, 0)
    assert flecha.saiu_da_tela() is True


def test_flecha_ainda_na_tela():
    flecha = Flecha(imagem_falsa(10, 40), 100, 300)
    assert not flecha.saiu_da_tela()


# ============================================================================
#  PARTE 4 - DADOS (ARQUIVOS DE RECORDE E RANKING)
# ============================================================================
def test_salvar_e_carregar_recorde(tmp_path):
    caminho = tmp_path / "recorde.txt"
    salvar_recorde(str(caminho), 150)
    assert carregar_recorde(str(caminho)) == 150


def test_carregar_recorde_sem_arquivo_retorna_zero(tmp_path):
    caminho = tmp_path / "nao_existe.txt"
    assert carregar_recorde(str(caminho)) == 0


def test_salvar_e_carregar_ranking(tmp_path):
    caminho = tmp_path / "ranking.txt"
    ranking = [("Joao", 120), ("Maria", 90)]
    salvar_ranking(str(caminho), ranking)
    assert carregar_ranking(str(caminho)) == ranking


def test_carregar_ranking_sem_arquivo_retorna_lista_vazia(tmp_path):
    caminho = tmp_path / "nao_existe.txt"
    assert carregar_ranking(str(caminho)) == []
