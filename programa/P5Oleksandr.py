"Programa 5: Cosita para ladrones"
"Autor: Dementiev Oleksasndr"
"Data: 30/04/2025"

from microbit import *
import neopixel

led = pin14
np = neopixel.NeoPixel(pin13, 1) # Configurar el neopixel en el pin 13
pir = pin15 # Configurar el pin 15 para el sensor PIR

while True:
    if pir.read_digital() == 1: # Si el sensor PIR detecta movimiento?

        for i in range(0, 1, 1): # Reproducir el tono RINGTONE una vez
            music.play(music.RINGTONE)
       
# Hacer parpadear el neopixel (rojo) 4 veces
       for i in range(0, 4, 1):
            np = (255, 0, 0)
            np.show()
            sleep(500)
            np = (0, 0, 0)
            np.clear()
            sleep(500)


# Hacer parpadear el LED 4 veces
        for i in range(0, 4, 1):
            led.write_digital(1)
            sleep(500)
            led.write_digital(0)
            sleep(500)

# Mostrar una imagen de "enojado" en la pantalla
        display.show(Image.ANGRY)
        sleep(5000)
        display.clear()



 # Si no hay movimiento, detener cualquier música que esté sonando
    else:
        music.stop()
    sleep(100)


