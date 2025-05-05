"Programa 4: Abrir y serar la puerta"
"Autor: Dementiev Oleksasndr"
"Data: 30/04/2025"
from microbit import *

pin2.set_analog_period(20)
servo = pin2
angulo = 0

while True:
    if button_b.is_pressed():
        angulo += 10
        servo.write_analog(angulo)
        if angulo >= 90:
            angulo = 0
            servo.write_analog(angulo)

