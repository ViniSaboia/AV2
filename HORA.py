def converter_hora(hora):
    return (hora -12)

def imprime_hora():
    hora = int(input("Digite a hora: "))
    minuto = int(input("Digite os minutos: "))
    if(hora <= 12):
        print(hora,minuto,"AM")
    else:
        print(converter_hora(hora), minuto, "PM")

opcao = 1

while opcao:
    print("Deseja converter a hora ?")
    print("1 para sim")
    print("0 para não")

    opcao = int(input("Digite aqui: "))



    if (opcao == 1):
        imprime_hora()
    if (opcao < 0):
        break