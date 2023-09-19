'''Conversão de Decimal para Binário
Esta função converte um número decimal em um número binário. Ela utiliza a técnica de divisão sucessiva por 2, obtendo os restos em cada etapa e concatenando-os da direita para a esquerda para formar o número binário.'''

def deci_bina( deci):
    entrada = deci
    bina = ""

    while deci > 1:
        bina = str(deci%2) + bina
        deci//=2
    print(f"{entrada}₁₀ = {str(deci)+bina}₂")


