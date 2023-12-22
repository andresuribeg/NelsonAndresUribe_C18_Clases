import time

class Reloj:
    def obtener_tiempo_actual(self):
        tiempo_actual = time.localtime()
        return tiempo_actual.tm_hour, tiempo_actual.tm_min, tiempo_actual.tm_sec

    def mostrar_tiempo(self):
        horas, minutos, segundos = self.obtener_tiempo_actual()
        print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

reloj = Reloj()

while True:
    reloj.mostrar_tiempo()
    time.sleep(1)
