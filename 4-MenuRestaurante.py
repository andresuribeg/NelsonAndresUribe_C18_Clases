class ItemMenu:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Menu:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def mostrar_menu(self):
        print("Menú:")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item.nombre} - ${item.precio}")

class ItemPedido:
    def __init__(self, item, cantidad):
        self.item = item
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.item.precio * self.cantidad

class Pedido:
    def __init__(self):
        self.items_pedido = []

    def agregar_item_pedido(self, item, cantidad):
        item_pedido = ItemPedido(item, cantidad)
        self.items_pedido.append(item_pedido)

    def generar_resumen(self):
        print("Resumen del pedido:")
        total = 0
        for item_pedido in self.items_pedido:
            subtotal = item_pedido.calcular_subtotal()
            total += subtotal
            print(f"{item_pedido.cantidad} {item_pedido.item.nombre}(s) - ${subtotal}")
        print(f"Total del pedido: ${total}")


menu = Menu()
menu.agregar_item(ItemMenu("Hamburguesa", 10))
menu.agregar_item(ItemMenu("Pizza", 12))
menu.agregar_item(ItemMenu("Ensalada", 8))

pedido = Pedido()

while True:
    menu.mostrar_menu()
    try:
        opcion = int(input("Seleccione un número del menú (o '0' para finalizar): "))
        if opcion == 0:
            break
        cantidad = int(input("Ingrese la cantidad: "))
        item_seleccionado = menu.items[opcion - 1]
        pedido.agregar_item_pedido(item_seleccionado, cantidad)
    except (ValueError, IndexError):
        print("Por favor, ingrese una opción válida.")

pedido.generar_resumen()
