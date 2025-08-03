
# Transformador de Gramáticas

Este projeto realiza transformações em gramáticas formais, incluindo:

- **Simplificação**
  - Remoção de símbolos inalcançáveis
  - Remoção de produções vazias
- **Formas Normais**
  - Forma Normal de Chomsky
  - Forma Normal de Greibach

## Exemplo de Uso

```python
python main.py
```

Entrada (exemplo):

```
S -> aAa | bBv
A -> a | aA
```

## Estrutura

- `main.py`: script principal
- `simplificacao.py`: regras de simplificação
- `chomsky.py`: conversão para FNC
- `greibach.py`: conversão para FNG


