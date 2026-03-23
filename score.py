def salvar_recorde(novo_tempo):
    try:
        with open("recorde.txt", "r") as f:
            recorde = int(f.read())

    except:
        recorde = 0

    if novo_tempo > recorde:
        with open("recorde.txt", "w") as f:
            f.write(str(novo_tempo))


def carregar_recorde():
    try:
        with open("recorde.txt", "r") as f:
            return int(f.read())
    except:
        return 0
