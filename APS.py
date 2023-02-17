def titulo(txt):
    print('=' * 50)
    print('{:^50}'.format(txt))
    print('=' * 50)


titulo('APLICAÇÃO DA CRIPTOGRAFIA DE POLÍBIO')

polibio = {'A':'11', 'B':'12', 'C':'13', 'D':'14', 'E':'15', 'F':'16',
        'G':'21', 'H':'22', 'I':'23', 'J':'24', 'K':'25', 'L':'26',
        'M':'31', 'N':'32', 'O':'33', 'P':'34', 'Q':'35', 'R':'36',
        'S':'41', 'T':'42', 'U':'43', 'V':'44', 'W':'45', 'X':'46',
        'Y':'51', 'Z':'52', '0':'53', '1':'54', '2':'55', '3':'56',
        '4':'61', '5':'62', '6':'63', '7':'64', '8':'65', '9':'66'}

while True:

    decisao = str(input('''Para CRIPTOGRAFAR digite "1"
Para DESCRIPTOGRAFAR digite "2"
'''))
    print('=' * 50)

    while ((decisao != '1') and (decisao != '2')):
        decisao = str(input('''OPÇÃO INVÁLIDA!
Para CRIPTOGRAFAR digite "1"
Para DESCRIPTOGRAFAR digite "2"
'''))
        print('=' * 50)

    if decisao == '1':
        mensagem_crip=input('Digite a mensagem a ser CRIPTOGRAFADA:').upper().replace(' ', '')
        mensagem_crip=list(mensagem_crip)

        for i in range(0, len(mensagem_crip)):
            mensagem_crip[i] = polibio[mensagem_crip[i]]

        while True:
            cripto=''
            for rep in mensagem_crip:
                cripto += rep + " "
            print(f'Mensagem CRIPTOGRAFADA: {cripto}')
            print('=' * 50)
            break

    if decisao == '2':
        descripto=''
        final = input('Digite a mensagem a ser DESCRIPTOGRAFADA:')
        while True:
            for i in polibio:
                if final[:2] == polibio[i]:
                    descripto += i
                    final = final[2:]
                    break
                else:
                    continue
            if final == '':break
        print(f'Mensagem DESCRIPTOGRAFADA: {descripto}')
        print('=' * 50)

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        print('=' * 50)
    if resp == 'N':
        break

print('Programa encerrado!')