numero = int(input("Indique o numero a ser checado: "))

#variaveis do calculo para fibonacci
f3 = 0
f1 = 1
f2 = 1
#0 e 1 sendo numeros de fibonacci
if (numero == 0 or numero == 1):
    print("numero escolhido é de fibonacci")

else:
    # gerando numeros fibonacci ate achar o f3 menor que o numero escolhido para definicao
    while f3 < numero:
        f3 = f1 + f2
        f2 = f1
        f1 = f3
    if f3 == numero:
        print("numero escolhido é de fibonacci")
    else:
        print("numero escolhido não pertence a serie de fibonacci")
