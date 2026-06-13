from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    pode_atirar,
)


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
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
    """Deve permitir atirar quando ja passou o tempo de intervalo."""
    assert pode_atirar(1000, 400, 500) is True


def test_pode_atirar_quando_ainda_nao_passou():
    """Nao deve permitir atirar antes do intervalo terminar."""
    assert pode_atirar(700, 400, 500) is False
