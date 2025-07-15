productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def stock_marca(marca):
    total = 0
    for modelo in productos:
        if productos[modelo][0].lower() == marca.lower():
            total += stock[modelo][1]
    print(f"El stock es: {total}")

def buscar_precio(precio_min,precio_max):
    resultados = []
    for modelo in productos:
        marca = productos[modelo][0]
        if precio_min <= stock[modelo][0] <= precio_max and stock[modelo][1] > 0:
            resultados.append(f"{marca}--{modelo}")
        
    print(f"Los notebooks entre los precios consultas son: '{marca.upper()}--{modelo}'")
    if resultados:
        resultados.sort()
        print("modelos encontrados")
        for item in resultados:
            print(item)
    else:
        print("No hay notebooks en ese rango de precios.")


def actualizar_precio(modelo,precio):
    if modelo in stock:
        int(stock[modelo][0].replace(precio))
        return True
    else:
        return False
def main():
    while True:

        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca")
        print("2. Búsqueda por precio.")
        print("3. Actualiza precio.")
        print("4. Salir.")

        op = int(input("Ingrese opción: "))
        if op == 1:
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)
        elif op == 2:
            while True:
                try:
                    precio_min = int(input("Ingrese precio mínimo: "))
                    precio_max = int(input("Ingrese precio máximo: "))
                except ValueError:
                    print("Debe ingresar numeros enteros!!")
                buscar_precio(precio_min,precio_max)
                break
        elif op == 3:
            while True:
                modelo = input("Ingrese modelo a actualizar: ")
                precio = int(input("Ingrese precio nuevo: "))
                if actualizar_precio(modelo,precio):
                    print("Precio actualizado.")
                else:
                    print("No se pudo actualizar el precio")
                    return
                seguir = input("Dese actualizar otro precio (s/n): ").lower()
                if seguir != ["s","si"]:
                    break
                
        elif op == 4:
            print("Programa finalizado.")
            break
main()