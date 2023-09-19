#função para corrigir erros de entrada 
def obter_opcao_valida():
    while True:
        try:
            opcao = int(input("║   Digite sua opção: "))
            if opcao in [1, 2, 3, 4, 5, 6]:
                return opcao
            else:
                print("╟────────────────────────────────╢")
                print("║   Opção inválida.              ║")
        except ValueError:
            print("╟────────────────────────────────╢")
            print("║   Opção inválida.              ║")


class Converter:
    def bina_deci(bina):
        deci = 0
        bina_invertido = bina[::-1]
        for posicao,bit in enumerate(bina_invertido):
            poten = 2**posicao
            deci += int(bit) * poten
        print(f"      {bina}₂ = {deci}₁₀")
        
    def bina_hexa(bina):
        hex_digit = {
            '0000': '0',
            '0001': '1',
            '0010': '2',
            '0011': '3',
            '0100': '4',
            '0101': '5',
            '0110': '6',
            '0111': '7',
            '1000': '8',
            '1001': '9',
            '1010': 'A',
            '1011': 'B',
            '1100': 'C',
            '1101': 'D',
            '1110': 'E',
            '1111': 'F'
        }
        entrada = bina
        hexa = ""
        qtnd_0 = 4 - (len(bina) % 4)
        
        if qtnd_0 != 4:
            bina = "0"*qtnd_0 + bina

        for i in range(0,len(bina),4):
            hexa += hex_digit[bina[i:i+4]]
            
        print(f"      {entrada}₂ = {hexa}₁₆")
      
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
        print(f"      {entrada}₁₆ = {deci}₁₀")  

    def hexa_bina(hexa):
        hex_dic = {
            '0': '0000',
            '1': '0001',
            '2': '0010',
            '3': '0011',
            '4': '0100',
            '5': '0101',
            '6': '0110',
            '7': '0111',
            '8': '1000',
            '9': '1001',
            'A': '1010',
            'B': '1011',
            'C': '1100',
            'D': '1101',
            'E': '1110',
            'F': '1111'
        }

        entrada = hexa
        bina = ""

        for i in str(hexa):
            i = i.upper() if i.isalpha() else i  # i receberá o próprio conteúdo maiúsculo, caso ele seja uma letra 
            hexa = hex_dic[i] 
            bina += hexa     
        print(f"      {entrada}₁₆ = {bina}₂")    
        
    def deci_bina(deci):
        
        entrada = deci
        deci = int(deci)
        bina = ""

        while deci > 1:
            bina = str(deci%2) + bina
            deci//=2
        print(f"      {entrada}₁₀ = {str(deci)+bina}₂")

    def deci_hexa(deci):   
        deci_dic = {
            0: '0',
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'
        }
        deci = int(deci)
        entrada = deci
        hexa = ""
        while deci >= 16:
            resto = deci % 16
            deci //= 16 
            hexa = deci_dic[resto] + hexa 
        hexa = deci_dic[deci] + hexa
        print(f"      {entrada}₁₀ = {hexa}₁₆")
    
enfeite = '-='*50
print(f"{enfeite}"
      f"\n {' Bem-vindo ao conversor de bases numéricas':^100}"
      f"\n{'Para converter, basta selecionar a opção desejada e entrar com o número':^100}"
      f"\n{enfeite}")

print("╔════════════════════════════════╗")
print("║  Selecione a opção desejada:   ║")
print("╟────────────────────────────────╢")
print("║  [1] Binário para Decimal      ║")
print("║  [2] Binário para Hexadecimal  ║")
print("║  [3] Hexadecimal para Decimal  ║")
print("║  [4] Hexadecimal para Binário  ║")
print("║  [5] Decimal para Binário      ║")
print("║  [6] Decimal para Hexadecimal  ║")
print("╟────────────────────────────────╢")
opcao = obter_opcao_valida()
print("╟────────────────────────────────╢")
entrada = str(input("╟   Digite um número: "))
print("╚════════════════════════════════╝")
match opcao:
    case 1:
        Converter.bina_deci(entrada)
    case 2:
        Converter.bina_hexa(entrada)
    case 3:
        Converter.hexa_deci(entrada)
    case 4:
        Converter.hexa_bina(entrada)
    case 5:
        Converter.deci_bina(entrada)  
    case 6:
        Converter.deci_hexa(entrada)      
