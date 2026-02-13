# anagramas

palavra1 = input('Digite a primeira palavra: ').lower()
palavra2 = input('Digite a segunda palavra: ').lower()

if len(palavra1) != len(palavra2):
    print(f'a palavra {palavra1} e a palavra {palavra2} NÃO são um anagrama!')
else:
    if sorted(palavra1) != sorted(palavra2):
        print(f'a palavra {palavra1} e a palavra {palavra2} NÃO são um anagrama!')
    else:
        print(f'a palavra {palavra1} e a palavra {palavra2} SÃO SIM anagramas!')
