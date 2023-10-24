while True: 
    posicaoBob = int(input("Insira a posição do BOB: "))
    posicaoRex = int(input("Insira a posição do REX: "))
    posicaoOli = int(input("Insira a posição do OLI: "))

    if posicaoBob >= 0 and posicaoRex >= 0 and posicaoOli >= 0: 
        if posicaoBob == posicaoOli or posicaoRex == posicaoOli:
            print("Oli não pode iniciar na mesma casa que algum dos cachorros. Insira um número válido.")
        else:

            if posicaoBob > posicaoOli:
                 distanciaBobOli = posicaoBob - posicaoOli
            elif posicaoOli > posicaoBob:
                 distanciaBobOli = posicaoOli - posicaoBob

            if posicaoRex > posicaoOli:
                distanciaRexOli = posicaoRex - posicaoOli
            elif posicaoOli > posicaoRex:
                distanciaRexOli = posicaoOli - posicaoRex

            if distanciaBobOli < distanciaRexOli:
                print("Bob pegará o gato.")
            elif distanciaBobOli > distanciaRexOli:
                print("Rex pegará o gato.")
            else:
                print("Bob e Rex chegarão ao mesmo tempo, portanto, Oli conseguirá fugir.")
        
        break
    else:
        print("As posições devem ser números inteiros não-negativos. Tente novamente.")
