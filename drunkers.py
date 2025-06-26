import time
import random

# Lista de nombres de los borrachos
borrachos = ["Cesar", "Victor", "Alejandro", "Andres", "Jonathan"]

# Registro de acciones pasadas
"""Se realizo el map para que no repitan la misma accion en los diferentes ciclos.
De esta forma se tiene un log de las acciones pasadas de cada uno de los borrachitos."""
acciones_pasadas = {nombre: [] for nombre in borrachos} # Map con las acciones pasadas

# Acciones disponibles
def tomar(nombre):
    print(f"{nombre} está tomando cerveza...")
    time.sleep(1)
    print(f"{nombre} se acabó la cerveza.")

def usar_baño(nombre):
    print(f"{nombre} está orinando....")
    time.sleep(1)
    print(f"{nombre} salió del baño.")

def call_ex(nombre):
    print(f"{nombre} está llamando a su ex llorando...")
    time.sleep(1)
    print(f"{nombre} le colgó su ex y sigue llorando.")

def singing(nombre):
    print(f"{nombre} está cantando a todo pulmón!")
    time.sleep(1)

def main():
    print("¡Inicia la fiesta de los borrachos!\n")

    for ciclo in range(4):
        print(f"\n=== CICLO {ciclo + 1} ===")
        """En los list comprehension de candidatos se realiza para cada borrachito
        en la lista de borrachos tomando como base el diccionario de acciones pasadas
        functiona de tal forma que checa si el borrachito no tiene baño o llamar en acciones pasadas."""
        candidatos_baño = [b for b in borrachos if 'baño' not in acciones_pasadas[b]] # List comprehension
        bañero = random.choice(candidatos_baño) # De forma aleatoria se toma un candidato de baño
        acciones_pasadas[bañero].append('baño') # Se guarda la accion de llamar en el nombre del borrachito

        candidatos_llamar = [b for b in borrachos if b != bañero and 'llamar' not in acciones_pasadas[b]] # List Comprehension
        llamador = random.choice(candidatos_llamar) # De forma aleatoria se toma un candidato de llamar
        acciones_pasadas[llamador].append('llamar') # Se guardan la accion de llamar en el nombre del borrachito

        for borracho in borrachos:
            if borracho == bañero:
                usar_baño(borracho)
            elif borracho == llamador:
                call_ex(borracho)
            else:
                # Acciones alternativas (no se registran porque no son únicas)
                random.choice([tomar, singing])(borracho)

            time.sleep(2)  # Pausa entre los borrachos

        print(f"\n--- Fin del ciclo {ciclo + 1} ---")
        time.sleep(1)

    print("\n¡La fiesta ha terminado! Todos los borrachos se fueron a casa.")

if __name__ == "__main__":
    main()
#Scarlet Lamas 
#Jonathan Ortega
# Alejandro Real
