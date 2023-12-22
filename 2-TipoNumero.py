class Numero:
    def __init__(self, numero):
        self.numero = numero

    def es_par(self):
        return self.numero % 2 == 0

    def es_primo(self):
        if self.numero < 2:
            return False
        for i in range(2, int(self.numero**0.5) + 1):
            if self.numero % i == 0:
                return False
        return True

    def generar_mensaje(self):
        if self.es_par():
            if self.es_primo():
                return "El número {} es primo por que solo es divisible por el mismo y par porque es el único número primo par.".format(self.numero)
            else:
                return "El número {} es par por que es divisible por 2 pero no es primo porque es divisible por otros numeros.".format(self.numero)
        else:
            if self.es_primo():
                return "El número {} es primo por que solo es divisible por el mismo e impar porque no es divisible por 2.".format(self.numero)
            else:
                return "El número {} es impar porque no es divisible por 2 y no es primo pporque es divisible por otros numeros.".format(self.numero)

try:
    numero = int(input("Introduce un número: "))
    numero_objeto = Numero(numero)
    print(numero_objeto.generar_mensaje())
except ValueError:
    print("Por favor, ingrese un número entero válido.")
