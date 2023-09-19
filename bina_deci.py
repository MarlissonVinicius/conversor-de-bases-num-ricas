'''Conversão de Binário para Decimal
Esta função converte um número binário em um número decimal. Ela itera pelos dígitos do número binário da direita para a esquerda, multiplicando cada dígito pela potência de 2 correspondente à sua posição e, em seguida, soma todos os resultados para obter o número decimal correspondente.'''

def bin_deci(bina):
    bina = str(bina)
    deci = 0
    bina_invertido = bina[::-1]
    for posicao,bit in enumerate(bina_invertido):
        poten = 2**posicao
        deci += int(bit) * poten
    print(f"{bina}₂ = {deci}₁₀")
