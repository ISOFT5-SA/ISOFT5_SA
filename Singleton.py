class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Dolce_vita(metaclass=SingletonMeta):

    def __init__(self):
        self.items = [
            {'id': '1', 'name': 'Pizza Margherita', 'description': 'Pizza clásica con tomate, mozzarella y albahaca', 'price': '150.00', 'category': 'Comida', 'available': 'True'},
            {'id': '2', 'name': 'Lasagna Bolognese', 'description': 'Lasaña al horno con salsa boloñesa', 'price': '180.00', 'category': 'Comida', 'available': 'True'},
            {'id': '3', 'name': 'Risotto ai Funghi', 'description': 'Risotto cremoso con champiñones', 'price': '170.00', 'category': 'Comida', 'available': 'True'},
            {'id': '4', 'name': 'Carbonara', 'description': 'Espagueti con salsa de huevo, queso y panceta', 'price': '160.00', 'category': 'Comida', 'available': 'True'},
            {'id': '5', 'name': 'Pollo al Marsala', 'description': 'Pollo en salsa de vino Marsala', 'price': '200.00', 'category': 'Comida', 'available': 'True'},
            {'id': '6', 'name': 'Saltimbocca', 'description': 'Ternera con jamón y salvia en vino blanco', 'price': '220.00', 'category': 'Comida', 'available': 'True'},
            {'id': '7', 'name': 'Melanzane alla Parmigiana', 'description': 'Berenjenas horneadas con queso parmesano', 'price': '140.00', 'category': 'Comida', 'available': 'True'},
            {'id': '8', 'name': 'Osso Buco', 'description': 'Estofado de ternera con gremolata', 'price': '250.00', 'category': 'Comida', 'available': 'True'},
            {'id': '9', 'name': 'Gnocchi al Pesto', 'description': 'Ñoquis con salsa de pesto genovés', 'price': '130.00', 'category': 'Comida', 'available': 'True'},
            {'id': '10', 'name': 'Arancini', 'description': 'Croquetas de arroz rellenas con queso', 'price': '90.00', 'category': 'Comida', 'available': 'True'},
            {'id': '11', 'name': 'Espresso', 'description': 'Café espresso italiano auténtico', 'price': '40.00', 'category': 'Bebida', 'available': 'True'},
            {'id': '12', 'name': 'Cappuccino', 'description': 'Café con espuma de leche', 'price': '60.00', 'category': 'Bebida', 'available': 'True'},
            {'id': '13', 'name': 'Limoncello', 'description': 'Licor italiano de limón', 'price': '80.00', 'category': 'Bebida', 'available': 'True'},
            {'id': '14', 'name': 'Aperol Spritz', 'description': 'Cóctel refrescante con Aperol, Prosecco y agua mineral', 'price': '120.00', 'category': 'Bebida', 'available': 'True'},
            {'id': '15', 'name': 'San Pellegrino', 'description': 'Agua mineral gasificada', 'price': '50.00', 'category': 'Bebida', 'available': 'True'},
            {'id': '16', 'name': 'Negroni', 'description': 'Cóctel clásico con ginebra, vermú rojo y Campari', 'price': '150.00', 'category': 'Bebida', 'available': 'True'},
            {'id': '17', 'name': 'Tiramisú', 'description': 'Postre clásico de café con queso mascarpone', 'price': '100.00', 'category': 'Postre', 'available': 'True'},
            {'id': '18', 'name': 'Panna Cotta', 'description': 'Flan de crema con salsa de frutas', 'price': '90.00', 'category': 'Postre', 'available': 'True'},
            {'id': '19', 'name': 'Cannoli', 'description': 'Rollo de masa frita relleno de ricotta', 'price': '80.00', 'category': 'Postre', 'available': 'True'},
            {'id': '20', 'name': 'Gelato', 'description': 'Helado artesanal italiano', 'price': '70.00', 'category': 'Postre', 'available': 'True'}
        ]
        self.users = []

    # ------------------------------
    # Métodos de validación
    # ------------------------------
    def validar_nombre_simple(self, nombre):
        return nombre.replace(' ', '').isalpha()

    def validar_correo_simple(self, correo):
        if not correo:
            return False
        if "@" not in correo or "." not in correo:
            return False
        caracteres_permitidos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@.-_"
        for caracter in correo:
            if caracter not in caracteres_permitidos:
                return False
        return True

    # ------------------------------
    # Menú principal
    # ------------------------------
    def menu(self):
        print("""
 ☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡    

           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
          |              Dolce Vita            |
          |                                    |
          |           Menu Principal           |
          |━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|
          |                                    |
          |  [1] - Registrar nuevo usuario     |
          |  [2] - Ubicacion.                  |
          |  [3] - Precios.                    |
          |  [4] - Salir.                      |
           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """)
        opcion = int(input("\nIngresa el numero de la opcion -> "))
        if opcion == 1:
            self.anadir()
        elif opcion == 2:
            self.venta()
        elif opcion == 3:
            self.mostrar()
        elif opcion == 4:
            self.salir()
        else:
            print("\n!Opcion incorrecta¡")
        self.menu()

    def anadir(self):
        print("""
           ╔══════════════════╗
            Registrar usuario
           ╚══════════════════╝
        """)
        while True:
            nombre = input("Ingresa tu nombre: ")
            if self.validar_nombre_simple(nombre):
                break
            print("Nombre inválido. Solo debe contener letras y espacios.")
        
        while True:
            correo = input("Ingresa tu correo electrónico: ")
            if self.validar_correo_simple(correo):
                break
            print("Correo electrónico inválido. Debe contener '@', '.', y solo caracteres permitidos.")
        
        self.users.append({'nombre': nombre, 'correo': correo})
        print("\n╔══════════════════════════════╗")
        print("  Usuario registrado con éxito!")
        print("╚══════════════════════════════╝")
        print(f"\nNombre: {nombre}")
        print(f"Correo: {correo}")
        input("\nPresiona Enter para continuar...")

    def mostrar(self):
        print("""
           ╔══════════════════╗
                Inventario
           ╚══════════════════╝
        """)
        print("\n--------------------------------------------------------------------------------------------------------------------------------")
        print("| ID     | Name                      | Description                                            | Price     | Category  | Available |")
        print("----------------------------------------------------------------------------------------------------------------------------------")
        for x in self.items:
            print(f"| {x['id']:<6}| {x['name']:<25}| {x['description']:<55}| {x['price']:<10}| {x['category']:<10}| {x['available']:<11}|")
        print("----------------------------------------------------------------------------------------------------------------------------------")

    def venta(self):
        print("""
           ╔══════════════════╗
                Ubicacion 
           ╚══════════════════╝
        """)
        print("="*60)
        print(f"{'📍 BIENVENIDO A':^60}")
        print(f"{'🌟 Ristorante Dolce Vita 🌟':^60}")
        print("="*60)
        print("📌 Dirección: Av. México #123, Colonia Centro")
        print("🏙 Ciudad: Tepic, Nayarit, México")
        print("📮 Código Postal: 63000")
        print("☎ Teléfono: 📞 311-123-4567")
        print("🕒 Horario de Atención: Lunes a Domingo, 12:00 p.m. - 10:00 p.m.")
        print("="*60)
        print("✨ ¡Te esperamos pronto! ✨")
        print("="*60)

    def salir(self):
        opc = input('\n¿Desea salir del programa? (si/no): ').lower()
        if opc == 'si':
            print("Saliendo del programa......")
            exit()
        else:
            self.menu()


# ------------------------------
# Ejecución del programa
# ------------------------------
if __name__ == "__main__":
    r1 = Dolce_vita()
    r2 = Dolce_vita()
    print(f"¿r1 es r2? -> {r1 is r2}")  # DEberia ser True gracias al singleton
    r1.menu()
