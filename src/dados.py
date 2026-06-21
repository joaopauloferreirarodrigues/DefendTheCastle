from src.funcoes import interpretar_linha_ranking, formatar_entrada_ranking

def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuacao recorde em um arquivo de texto.
    Parametros:
        caminho_arquivo (str): caminho do arquivo (CAMINHO_RECORDE no config).
        pontuacao (int): pontuacao a guardar
    Retorno:
        A função apenas grava o arquivo.
    """
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """
    Le a pontuacao recorde salva no arquivo.
    Parametros:
        caminho_arquivo (str): caminho do arquivo (CAMINHO_RECORDE no config).
    Retorno:
        int: o recorde salvo, ou 0 
    """
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            if conteudo == "":
                return 0
            return int(conteudo)
    except (FileNotFoundError, ValueError):
        return 0

def carregar_ranking(caminho_arquivo):
    """
    Le o placar do arquivo.
    Parametros:
        caminho_arquivo (str): caminho do arquivo (CAMINHO_RANKING no config).
    Retorno:
        list: lista de (nome, pontos). Lista vazia se o arquivo nao existir.
    """
    ranking = []
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                entrada = interpretar_linha_ranking(linha)
                if entrada is not None:
                    ranking.append(entrada)
    except FileNotFoundError:
        return []
    return ranking


def salvar_ranking(caminho_arquivo, ranking):
    """
    Grava o placar no arquivo, uma linha por jogador.
    Parametros:
        caminho_arquivo (str): caminho do arquivo (CAMINHO_RANKING no config).
        ranking (list): lista de (nome, pontos) a salvar.
    Retorno:
        A função apenas grava o arquivo.
    """
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        for nome, pontos in ranking:
            arquivo.write(formatar_entrada_ranking(nome, pontos) + "\n")
