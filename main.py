
from simplificacao import simplificar_gramatica
from chomsky import para_fnc
from greibach import para_fng

def imprimir_gramatica(gr):
    for nt, regras in gr.items():
        print(f"{nt} -> {' | '.join(regras)}")

if __name__ == "__main__":
    gramatica = {
        "S": ["aAa", "bBv"],
        "A": ["a", "aA"]
    }

    print("Original:")
    imprimir_gramatica(gramatica)

    print("\nSimplificada:")
    gramatica = simplificar_gramatica(gramatica)
    imprimir_gramatica(gramatica)

    print("\nForma Normal de Chomsky:")
    fnc = para_fnc(gramatica)
    imprimir_gramatica(fnc)

    print("\nForma Normal de Greibach:")
    fng = para_fng(gramatica)
    imprimir_gramatica(fng)
