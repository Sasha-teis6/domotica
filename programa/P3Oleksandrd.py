"Programa 3: El timbre"
"Autor: Dementiev Oleksasndr"
"Data: 30/04/2025"


from microbit import *
import music

led = pin14
i = 0

while True:
    if button_a.is_pressed():
        for i in range(3):
            i = i+1
            led.write_digital(1)
            sleep(500)
            led.write_digital(0)
            sleep(500)

        for i in range(2):
            music.play(music.RINGTONE)
            sleep(1000)
