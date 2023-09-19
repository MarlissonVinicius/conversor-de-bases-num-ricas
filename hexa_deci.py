def hexa_deci(hexa):

    hexa_deci = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    entrada = hexa
    hexa = hexa[::-1]
    deci = 0

    for posicao, digito in enumerate(hexa):
        if digito.isalpha():
            digito = hexa_deci[digito.upper()]
        deci += int(digito) * 16**posicao
    print(f"{entrada}₁₆ = {deci}₁₀")
    
hexa_deci("18ff")