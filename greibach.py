
def para_fng(producoes):
    from copy import deepcopy

    gr = deepcopy(producoes)
    novas_vars = {}
    
    def terminal_para_variavel(p, dicionario):
        if p and p[0].islower():
            nome = f"T_{p[0]}"
            if nome not in dicionario:
                dicionario[nome] = [p[0]]
            return nome + p[1:]
        return p

    producoes_temp = {}
    for nt, regras in gr.items():
        producoes_temp[nt] = []
        for r in regras:
            nova = terminal_para_variavel(r, novas_vars)
            producoes_temp[nt].append(nova)

    gr = producoes_temp

    alterado = True
    while alterado:
        alterado = False
        atualizadas = {}
        for nt, regras in gr.items():
            atualizadas[nt] = []
            for r in regras:
                if r and r[0].isupper():
                    alterado = True
                    if r[0] not in gr:
                        atualizadas[nt].append(r)
                        continue
                    for subst in gr[r[0]]:
                        atualizadas[nt].append(subst + r[1:])
                else:
                    atualizadas[nt].append(r)
        gr = atualizadas

    for nt, regras in novas_vars.items():
        gr[nt] = regras

    return gr
