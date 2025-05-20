"Programa 4: Abrir y serar la puerta"
"Autor: Dementiev Oleksasndr"
"Data: 30/04/2025"
from microbit import *



if button_b.is_pressed():        # Se se preme o botón B
        if porta == 0:               # Se a porta está pechada
            pin2.write_analog(90)    # Abrímosla
            porta = 1                # Actualizamos o estado
        else:                        # Se xa está aberta
            pin2.write_analog(1)     # Pechámosla
            porta = 0                # Actualizamos o estado
            sleep(500) 



"""pin2.set_analog_period(20)
servo = pin2
angulo_de_puerta = 0

while True:
    
    if button_b.is_pressed():
        angulo_de_puerta += 10
        servo.write_analog(angulo_de_puerta)
         
        if angulo_de_puerta >= 90:
            angulo_de_puerta = 0
            servo.write_analog(angulo_de_puerta)"""


