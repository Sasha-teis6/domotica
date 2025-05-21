"Programa 3: El timbre"
"Autor: Dementiev Oleksasndr"
"Data: 30/04/2025"

from microbit import *
import music

led = pin14

while True:
    if button_a.is_pressed(): # Si el botón A está presionado?
        led.write_digital(1)  # Enciende el LED en 5 s
        sleep(5000)
        led.write_digital(0) # Apaga el LED 
        sleep(500)
        music.play(music.RINGTONE) # Reproduce musica RINGTONE en el altavoz del micro:bit
        sleep(1000)

"""
while True:
    if button_a.is_pressed():
        for i in range(3):
            led.write_digital(1)
            sleep(500)
            led.write_digital(0)
            sleep(500)

        for i in range(2):
            music.play(music.RINGTONE)
            sleep(1000)
"""
