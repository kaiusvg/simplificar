
def simplificar_gramatica(gr):
    gr = remover_simbolos_inalcancaveis(gr)
    gr = remover_producoes_vazias(gr)
    return gr

def remover_simbolos_inalcancaveis(gr):
    alcancaveis = set()
    alcancaveis.add("S")

    alterado = True
    while alterado:
        alterado = False
        for nt in list(alcancaveis):
            if nt in gr:
                for r in gr[nt]:
                    for simbolo in r:
                        if simbolo.isupper() and simbolo not in alcancaveis:
                            alcancaveis.add(simbolo)
                            alterado = True

    return {nt: regras for nt, regras in gr.items() if nt in alcancaveis}

def remover_producoes_vazias(gr):
    anulaveis = set(nt for nt, regras in gr.items() if "" in regras)
    novas_gr = {}

    for nt, regras in gr.items():
        novas_regras = []
        for r in regras:
            if r != "":
                novas_regras.append(r)
                for simbolo in r:
                    if simbolo in anulaveis:
                        nova = r.replace(simbolo, "")
                        if nova not in novas_regras and nova:
                            novas_regras.append(nova)
        novas_gr[nt] = novas_regras

    return novas_gr
