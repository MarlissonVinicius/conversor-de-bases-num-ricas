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
        
    print(f"{entrada}₂ = {hexa}₁₆") 


bina_hexa("111100010000")