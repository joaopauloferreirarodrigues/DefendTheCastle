from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    pode_atirar,
    tomar_dano,
    quantidade_de_morcegos,
    venceu_o_jogo,
    calcular_posicao_central,
    calcular_espaco_entre_morcegos,
)


def test_calcular_pontos():
    """Deve somar os pontos atuais com os pontos ganhos"""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando a vida é 0"""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando ainda tem pelo menos 1 vida"""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


def test_pode_atirar_quando_passou_o_intervalo():
    """Deve permitir atirar quando ja passou o tempo de intervalo"""
    assert pode_atirar(1000, 400, 500) is True


def test_pode_atirar_quando_ainda_nao_passou():
    """Nao deve permitir atirar antes do intervalo terminar"""
    assert pode_atirar(700, 400, 500) is False


def test_tomar_dano():
    """Deve subtrair corretamente o dano da vida atual"""
    assert tomar_dano(3, 1) == 2


def test_quantidade_de_morcegos_cresce_por_onda():
    """Deve ter mais morcegos conforme as ondas avançam"""
    assert quantidade_de_morcegos(1, 2) == 2
    assert quantidade_de_morcegos(6, 2) == 4


def test_venceu_o_jogo_apos_ultima_onda():
    """Deve indicar vitoria quando o numero de onda passar do total"""
    assert venceu_o_jogo(11, 10) is True


def test_nao_venceu_durante_o_jogo():
    """Nao deve indicar vitoria enquanto ainda não chegar nas 10 ondas"""
    assert venceu_o_jogo(10, 10) is False


def test_calcular_posicao_central():
    """Deve centralizar corretamente um objeto de 100px numa tela de 800px."""
    assert calcular_posicao_central(800, 100) == 350


def test_calcular_espaco_entre_morcegos():
    """Deve dividir a tela igualmente entre os morcegos."""
    assert calcular_espaco_entre_morcegos(800, 4) == 200
