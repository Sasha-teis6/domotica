"Programa 1"
"Autor: Dementiev Oleksasndr"
"Data: 30/04/2025"

from microbit import *
import neopixel


np = neopixel.NeoPixel(pin13, 1)
rele = pin16


while True:
    temperatura = temperature()


    if temperatura > 24:
        np[0] = (255, 0, 0)  # Vermelho
        np[1] = (255, 0, 0)
        np.show()
        rele.write_digital(1)

    elif temperatura > 22 and temperatura <= 24:
        np[0] = (255, 165, 0)  # Laranja
        np[1] = (255, 165, 0)
        np.show()
        rele.write_digital(0)

    elif temperatura > 20 and temperatura <= 22:
        np[0] = (0, 255, 0)  # Verde
        np[1] = (0, 255, 0)
        np.show()
        rele.write_digital(0)

    elif
    temperatura <= 20:
        np[0] = (0, 0, 255)  # Azul
        np[1] = (0, 0, 255)
        np.show()
        rele.write_digital(0)

    else:
        np[0] = (0, 0, 0)
        np[1] = (0, 0, 0)
        np.clear()
        rele.write_digital(0)


    np.show()
    sleep(2000)

