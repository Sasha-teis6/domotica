"Programa 5"
"Autor: Dementiev Oleksasndr"
"Data: 30/04/2025"

from microbit import *
import neopixel

led = pin14
np = neopixel.NeoPixel(pin13, 1)
pir = pin15

while True:
    if pir.read_digital() == 1:

        for i in range(0, 1, 1):
            music.play(music.RINGTONE)

       for i in range(0, 4, 1):
            np = (255, 0, 0)
            np.show()
            sleep(500)
            np = (0, 0, 0)
            np.clear()
            sleep(500)

        for i in range(0, 4, 1):
            led.write_digital(1)
            sleep(500)
            led.write_digital(0)
            sleep(500)

        display.show(Image.ANGRY)
        sleep(5000)
        display.clear()





    else:
        music.stop()
    sleep(100)


