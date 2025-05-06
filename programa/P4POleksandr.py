"Programa 4: Abrir y serar la puerta"
"Autor: Dementiev Oleksasndr"
"Data: 30/04/2025"
from microbit import *

pin2.set_analog_period(20)
servo = pin2
angulo_de_puerta = 0

while True:
    
    if button_b.is_pressed():
        angulo_de_puerta += 10
        servo.write_analog(angulo_de_puerta)
         
        if angulo_de_puerta >= 90:
            angulo_de_puerta = 0
            servo.write_analog(angulo_de_puerta)

