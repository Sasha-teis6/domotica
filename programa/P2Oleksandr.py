"""Programa 2: Control de luz ambiente
Autor: Dementiev Oleksasndr
Data: 30/04/2025
"""

from microbit import *

led = pin14 # Conectamos Led a pin 14

while True:
    luz = pin1.read_analog()  # Lee el valor de pin 1 
   
    if luz < 700:             # Si valor de luz es menor que 700, enciende LED 
        led.write_digital(1)  # Enciende el LED

    else:
        led.write_digital(0)  # Apaga el LED

    sleep(1000)
