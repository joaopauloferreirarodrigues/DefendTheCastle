from src.funcoes import (
    calcular_pontos,
    tomar_dano,
    jogador_perdeu,
    limitar_valor,
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
)
from src.config import (
    ESQUELETO_VELOCIDADE,
    MORCEGO_VELOCIDADE,
    ORC_VELOCIDADE,
    ORDEM_DOS_INIMIGOS,
)

def test_calcular_pontos_varios_casos():
    assert calcular_pontos(0, 10) == 10
    assert calcular_pontos(50, 20) == 70
    assert calcular_pontos(100, 0) == 100

def test_tomar_dano_varios_casos():
    assert tomar_dano(3, 1) == 2
    assert tomar_dano(2, 2) == 0
    assert tomar_dano(1, 0) == 1

def test_tomar_dano_quando_dano_passa_da_vida():
    assert tomar_dano(1, 3) == -2

def test_jogador_perdeu_com_zero_ou_menos():
    assert jogador_perdeu(0) is True
    assert jogador_perdeu(-1) is True

def test_jogador_nao_perdeu_com_vidas():
    assert not jogador_perdeu(1)
    assert not jogador_perdeu(3)

def test_limitar_valor_abaixo_do_minimo():
    assert limitar_valor(-5, 0, 100) == 0

def test_limitar_valor_acima_do_maximo():
    assert limitar_valor(150, 0, 100) == 100

def test_limitar_valor_dentro_do_intervalo():
    assert limitar_valor(50, 0, 100) == 50

def test_pode_atirar_quando_passou_o_intervalo():
    assert pode_atirar(1000, 500, 400) is True

def test_nao_pode_atirar_antes_do_intervalo():
    assert not pode_atirar(700, 500, 400)

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

def test_quantidade_de_inimigos_cresce_por_onda():
    assert quantidade_de_inimigos(1, 2) == 2
    assert quantidade_de_inimigos(3, 2) == 3
    assert quantidade_de_inimigos(6, 2) == 4

def test_quantidade_de_inimigos_e_constante_dentro_de_tres_ondas():
    assert quantidade_de_inimigos(1, 2) == quantidade_de_inimigos(2, 2)
    assert quantidade_de_inimigos(3, 2) > quantidade_de_inimigos(2, 2)

def test_calcular_espaco_entre_inimigos():
    assert calcular_espaco_entre_inimigos(800, 4) == 200
    assert calcular_espaco_entre_inimigos(800, 2) == 400

def test_tipo_da_onda_segue_a_ordem():
    ordem = ["esqueleto", "morcego", "orc"]
    assert tipo_da_onda(1, ordem) == "esqueleto"
    assert tipo_da_onda(2, ordem) == "morcego"
    assert tipo_da_onda(3, ordem) == "orc"
    assert tipo_da_onda(4, ordem) == "esqueleto"

def test_primeira_onda_nao_e_morcego():
    assert not tipo_da_onda(1, ORDEM_DOS_INIMIGOS) == "morcego"

def test_venceu_o_jogo_apos_ultima_onda():
    assert venceu_o_jogo(11, 10) is True

def test_nao_venceu_durante_o_jogo():
    assert not venceu_o_jogo(5, 10)

def test_ordem_de_velocidade_dos_inimigos():
    assert ORC_VELOCIDADE < ESQUELETO_VELOCIDADE
    assert ESQUELETO_VELOCIDADE < MORCEGO_VELOCIDADE

def test_nome_valido_com_texto():
    assert nome_valido("Joao") is True

def test_nome_invalido_quando_vazio_ou_espacos():
    assert not nome_valido("")
    assert not nome_valido("    ")

def test_adicionar_caractere():
    assert adicionar_caractere("Joa", "o", 10) == "Joao"

def test_adicionar_caractere_respeita_limite():
    cheio = "ABCDEFGHIJ"   
    assert adicionar_caractere(cheio, "K", 10) == cheio

def test_remover_caractere():
    assert remover_caractere("Joao") == "Joa"
    assert remover_caractere("") == ""

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

def test_nao_e_recorde_quando_empata_com_o_menor():
    ranking = [("A", 100), ("B", 50)]
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
    assert not ("D", 10) in novo  

def test_adicionar_ao_ranking_quando_ranking_esta_vazio():
    novo = adicionar_ao_ranking([], "Joao", 100, 5)
    assert novo == [("Joao", 100)]

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

def test_formatar_e_interpretar_sao_inversos():
    linha = formatar_entrada_ranking("Maria", 250)
    assert interpretar_linha_ranking(linha) == ("Maria", 250)
