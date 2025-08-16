
#? Este proyecto representa la versión 2 de la aplicación Scorpions Foods:

#* 1.- Aqui se realiza el mensaje de bienvenida y el menú de la aplicación.
#* 2.- Se registra al usuario solicitando su nombre y correo electrónico con una validación sencilla.

import time 

MENU_ITEMS=[
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

import time

def imprimir_bienvenida_y_menu():
    print("Bienvenido(a) a Dolce Vita!!\n")
    time.sleep(1)
    print("El menú es el siguiente:\n")
    for item in MENU_ITEMS:
        print(f"{item['id']}. {item['name']} - {item['description']} - ${item['price']}")

#! validar_email_simple recibe un parámetro email que debería ser un str (cadena) y devuelve un valor de tipo (booleano).
## Debe contener exactamente un '@'.
## Parte local y dominio no vacíos.
## El dominio debe tener al menos un punto '.'.
## En el dominio solo se permiten letras, números, guiones '-' y puntos '.'.

def validar_email(email: str) -> bool:

    if email.count("@") != 1: #! exactamente un '@'
        return False
    
    parte_local, parte_dominio = email.split("@", 1)

    if not parte_local or not parte_dominio: #! no puede estar vacío
        return False

    if "." not in parte_dominio: #! dominio debe tener al menos un punto
        return False

    #! for c in parte_dominio: #! caracteres permitidos en el dominio
    ## c.isalnum() --> metodo que verifica si el carácter es alfanumérico (letra o número).
    ## c i n "-." --> verifica si el carácter es un guion o un punto.
    ## (c.isalnum() or c in "-.") verifica si el carácter es alfanumérico o un guion/punto.
    ## if not (c.isalnum() or c in "-.") detecta si hay un carácter no permitido.
    for c in parte_dominio:     
        if not (c.isalnum() or c in "-."):
            return False

    #! TLD no vacío (lo que va después del último punto)
    ## 1.- Genericos (gTLD): .com, .net, .org, .info, .xyz
    ## 2.- Nacionales (ccTLD): .mx, .es, .fr, .uk, .jp
    ## 3.- Patrocinados (sTLD): .edu, .gov, .mil, .int
    if not parte_dominio.split(".")[-1]:
        return False
    return True

#! prompt: str) -> str: Recibe un parametro llamado prompt que debe ser una cadena de texto (str)
#! prompt es un mensaje que se muestra al usuario para solicitarle una entrada input ()

#todo: ¿que hace strip()?

def pedir_no_vacio(prompt: str) -> str:
    while True:
        val = input(prompt).strip() 
        if val:
            return val
        print("⚠️  Este campo no puede estar vacío. Intenta de nuevo.\n")

def registrar_usuario() -> None:
    nombre = pedir_no_vacio("Ingresa tu nombre: ")
    email = pedir_no_vacio("Ingresa tu correo electrónico: ")
    while not validar_email(email):
        print("⚠️ Correo electrónico no es valido. Inténtalo de nuevo.")
        print("   Reglas:")
        print("   - Debe tener exactamente un '@'")
        print("   - El dominio debe tener al menos un punto (ej. dominio.com)")
        print("   - Después de '@' usa solo letras, números, '-' y '.'\n")
        email = pedir_no_vacio("Ingresa tu correo electrónico: ")
    print(f"✅ Usuario '{nombre}' registrado con éxito. Correo: {email}")

def main() -> None:
    imprimir_bienvenida_y_menu()
    registrar_usuario()
    print("\nGracias por visitar ScorpionsFood. ¡Buen provecho! 🦂")

#todo: ¿que hace aqui)?
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaliendo... ¡Hasta pronto!")

#scarlet elizabeth lamas villalobos 
