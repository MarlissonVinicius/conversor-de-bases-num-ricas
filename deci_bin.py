def deci_bina( deci):
    entrada = deci
    bina = ""

    while deci > 1:
        bina = str(deci%2) + bina
        deci//=2
    print(f"{entrada}₁₀ = {str(deci)+bina}₂")


