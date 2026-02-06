from machine import Pin         #           Importa         #
from time import sleep          #         bibliotecas       #

verde = Pin (2, Pin.OUT)        #           Define          #
amarelo = Pin (4, Pin.OUT)      #             as            #
vermelho = Pin (16, Pin.OUT)    #           saídas          #

verde.off()                     #      Inicia com todos     #
amarelo.off()                   #       todos os leds       #
vermelho.off()                  #        apagados           #

while True: 
    vermelho.off()              #   Apaga o led vermelho    #
    verde.on()                  #   Acende o led verde      #
    sleep(10)                   #   Espera 10 segundos      #

    verde.off()                 #   Apaga o led verde       #
    amarelo.on()                #   Acende o led amarelo    #
    sleep(4)                    #   Espera 4 segundos       #

    amarelo.off()               #   Apaga o led amarelo     #
    vermelho.on()               #   Acende o led vermelho   #
    sleep(10)                   #   Espera 10 segundos      #