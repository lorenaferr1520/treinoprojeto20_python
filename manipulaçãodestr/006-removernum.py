# remover todos os números de uma str
numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

string = input('digite algo: ')
strigsemnum = ""

for i in string:
    if i not in numeros:
        strigsemnum += i
        
print(strigsemnum)