class Dolce_vita:

    def __init__(self):
        self.items=[
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
        self.p=1
       #self.user=[()]
    def menu(self):
        print("""
 ☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡    

           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
          |              Dolce Vita            |
          |                                    |
          |           Menu Principal           |
          |━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|
          |                                    |
          |  [1] - Registrar nuevo usuario.not found    |
          |  [2] - Ubicacion.                  |
          |  [3] - Precios.                    |
          |  [4] - Salir.                      |
           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """)
        opcion=int(input("\nIngresa el numero de la opcion -> "))
        if opcion==1:
            self.anadir()
        elif opcion==2:
            self.venta()
        elif opcion==3:
            self.mostrar()
        elif opcion==4:
            self.salir()
        else:
            print("\n!Opcion Incorrecta¡")
        self.menu()
    
    def anadir(self):
        self.mostrar()
        print("""
           ╔══════════════════╗
            Registrar usuario
           ╚══════════════════╝
           not avaibleeeeee
        """)
        code=input(  "Ingresa el Codigo            : ")
        pizza=input( "Ingresa el nombre: ")
        info=input(  "Ingresa      : ")
        precio=input("Ingresa el precio            : ")
        unidad=input("Unidades                     : ")
        self.items.append({'code':code,'Pizza':pizza, 'info':info, 'precio':precio,'Unidades':unidad})
        print("Usuario registrado con exito")
        
            
    def mostrar(self):
        print("""
        
           ╔══════════════════╗
                Inventario
           ╚══════════════════╝
        """)
        print("\n-------------------------------------------------------------------------------------------------------")
        print("| ID     | Name                      | Description                                            | Price     | Category  | Available |")
        print("-------------------------------------------------------------------------------------------------------")
        for x in range(len(self.items)):
                print(f"| {self.items[x]['id']}{' ' * (6 - len(self.items[x]['id']))} |{self.items[x]['name']}{' ' * (25 - len(self.items[x]['name']))}  | {self.items[x]['description']}{' ' * (55 - len(self.items[x]['description']))}| {self.items[x]['price']}{' ' * (10 - len(self.items[x]['price']))}| {self.items[x]['category']}{' ' * (10 - len(self.items[x]['category']))}|{self.items[x]['available']}{' ' * (11 - len(self.items[x]['available']))}|")
            
        print("-------------------------------------------------------------------------------------------------------")
        
    def venta(self):
        print("""
        
           ╔══════════════════╗
                Ubicacion 
           ╚══════════════════╝
        """)
        nombre_restaurante = "🌟 Ristorante Dolce Vita 🌟"
        calle = "Av. México #123"
        colonia = "Centro"
        ciudad = "Tepic"
        estado = "Nayarit"
        pais = "México"
        cp = "63000"
        telefono = "📞 311-123-4567"
        horario = "🕛 Lunes a Domingo, 12:00 p.m. - 10:00 p.m."
        print("\n" + "="*60)
        print(f"{'📍 BIENVENIDO A':^60}")
        print(f"{nombre_restaurante:^60}")
        print("="*60)
        print(f"📌 Dirección: {calle}, Colonia {colonia}")
        print(f"🏙 Ciudad: {ciudad}, {estado}, {pais}")
        print(f"📮 Código Postal: {cp}")
        print(f"☎ Teléfono: {telefono}")
        print(f"🕒 Horario de Atención: {horario}")
        print("="*60)
        print("✨ ¡Te esperamos pronto! ✨")
        print("="*60)
    
    def salir(self):
        opc = 'No'
        opc = input('\n¿Desea salir del programa? (Si/No): ').lower()
        if opc == 'si':
            print("Saliendo del programa......")
            exit()
        else:
            self.menu()

pizzeria=Dolce_vita()
pizzeria.menu()