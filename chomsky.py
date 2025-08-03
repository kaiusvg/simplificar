
def para_fnc(producoes):
    from copy import deepcopy

    gr = deepcopy(producoes)
    novas_vars = {}
    contador = 1

    def criar_variavel_terminal(terminal):
        nonlocal contador
        nome = f"T_{terminal}"
        if nome not in novas_vars:
            novas_vars[nome] = [terminal]
        return nome

    # Substitui terminais em produções maiores que 1
    novas_producoes = {}
    for nt, regras in gr.items():
        novas_producoes[nt] = []
        for r in regras:
            if len(r) > 1:
                nova_regra = ""
                for simbolo in r:
                    if simbolo.islower():
                        nova_regra += criar_variavel_terminal(simbolo)
                    else:
                        nova_regra += simbolo
                novas_producoes[nt].append(nova_regra)
            else:
                novas_producoes[nt].append(r)

    gr = novas_producoes

    for nt, regras in list(gr.items()):
        for r in regras:
            while len(r) > 2:
                novo_nt = f"X{contador}"
                contador += 1
                gr[nt].remove(r)
                gr[nt].append(r[0] + novo_nt)
                gr[novo_nt] = [r[1:]]
                r = r[0] + novo_nt

    for nt, regras in novas_vars.items():
        gr[nt] = regras

    return gr
