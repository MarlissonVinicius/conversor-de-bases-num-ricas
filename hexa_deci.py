'''Conversão de Hexadecimal para Decimal
Esta função converte um número hexadecimal em um número decimal. Ela itera pelos dígitos do número hexadecimal da direita para a esquerda, considerando letras maiúsculas ou minúsculas como dígitos hexadecimais, multiplicando cada dígito pelo valor correspondente e, em seguida, soma todos os resultados para obter o número decimal correspondente.'''

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