class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Nomina:
    def __init__(self, empleados):
        self.empleados = empleados
        self.salario_minimo = 1160000  # Salario mínimo legal vigente

    def calcular_costo_nomina(self):
        costo_total = 0
        for empleado in self.empleados:
            salario_mensual = empleado.salario
            costo_total += self.calcular_costo_empleado(salario_mensual)
        return costo_total

    def calcular_costo_empleado(self, salario_mensual):
        costo_empleado = salario_mensual

        # Prestaciones sociales (10% del salario)
        prestaciones_sociales = salario_mensual * 0.10
        costo_empleado += prestaciones_sociales

        # Aportes a salud (8.5% del salario)
        aportes_salud = salario_mensual * 0.085
        costo_empleado += aportes_salud

        # Aportes a pensión (12% del salario)
        aportes_pension = salario_mensual * 0.12
        costo_empleado += aportes_pension

        # Aportes parafiscales (9% del salario)
        aportes_parafiscales = salario_mensual * 0.09
        costo_empleado += aportes_parafiscales

        return costo_empleado


empleado1 = Empleado("Empleado1", 1160000)  # Salario mínimo
empleado2 = Empleado("Empleado2", 2 * 1160000)  # Dos salarios mínimos

nomina = Nomina([empleado1, empleado2])
costo_total_nomina = nomina.calcular_costo_nomina()

print(f"Costo total de la nómina: ${costo_total_nomina}")
