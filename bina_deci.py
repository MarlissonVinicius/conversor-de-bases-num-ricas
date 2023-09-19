def bin_deci(bina):
    bina = str(bina)
    deci = 0
    bina_invertido = bina[::-1]
    for posicao,bit in enumerate(bina_invertido):
        poten = 2**posicao
        deci += int(bit) * poten
    print(f"{bina}₂ = {deci}₁₀")