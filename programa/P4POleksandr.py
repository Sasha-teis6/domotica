"Programa 4"
"Autor: Dementiev Oleksasndr"
"Data: 30/04/2025"

from microbit import *


servo = pin2
angulo = 0

while True:
    if button_b.is_pressed():
        angulo += 10
        servo.write_analog(angulo)
        if angulo >= 90:
            angulo = 0
            servo.write_analog(angulo)

