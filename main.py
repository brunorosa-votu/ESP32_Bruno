from machine import Pin         #           Importa         #
from time import sleep          #         bibliotecas       #

verde = Pin (2, Pin.OUT)        #           Define          #
amarelo = Pin (4, Pin.OUT)      #             as            #
vermelho = Pin (16, Pin.OUT)    #           saídas          #

verde.off()                     #      Inicia com todos     #
amarelo.off()                   #       todos os leds       #
vermelho.off()                  #        apagados           #

while True: 
    contador = 0                # Cria uma variável chamada "contador" e iguala a 0 #

    vermelho.off()              #   Apaga o led vermelho    #

    print("VERDE")              #   Exibe "VERDE" no terminal    #
    verde.on()                  #   Acende o led verde      #
    sleep(10)                   #   Espera 10 segundos      #

    verde.off()                 #   Apaga o led verde       #

    print("AMARELO")            #   Exibe "AMARELO" no terminal  #
    while contador < 20:        #    Enquanto "contador"    #
        amarelo.on()            #     for menor que 20      #
        sleep(0.1)              #      o led amarelo        #
        amarelo.off()           #        vai piscar         #
        sleep(0.1)              #     totalizando no fim    #
        contador += 1           #   um tempo de 4 segundos  #
          
    print("VERMELHO")           #   Exibe "VERMELHO" no terminal #
    vermelho.on()               #   Acende o led vermelho   #
    sleep(10)                   #   Espera 10 segundos      #