class Nota:

    def __init__(self, nota):
        self.nota = nota

    def comprobar(self):

        if self.nota < 1.0:
            return "Perdida la materia en", self.nota, "sin tener recuperación"
        elif self.nota <= 2.5:
            return "Perdido la materia en", self.nota, "pero se puede nivelar máximo nota final 3.0"
        elif self.nota <= 2.9:
            return "Perdido la materia en:", self.nota, "pero se puede nivelar máximo nota final 3.5"
        elif self.nota <= 3.5:
            return "Aceptable:", self.nota, "por recuperación"
        elif self.nota <= 3.9:
            return "Aceptable:", self.nota, "te recomiendo que sigas mejorando, vas bien"
        elif self.nota <= 4.5:
            return "Excelente:", self.nota, "vas por un buen camino hacia el éxito"
        else:
            return "Científico:", self.nota, "tienes un gran futuro adelante"

nota = float(input("Introduce la nota: "))
nota_objeto = Nota(nota)
print(nota_objeto.comprobar())