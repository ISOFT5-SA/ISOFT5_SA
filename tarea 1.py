
def validar_nombre_simple(nombre):
  return nombre.isalpha()

def validar_correo_simple(correo):
  if not correo:
    return False
  if "@" not in correo or "." not in correo:
    return False

  caracteres_permitidos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@."
  for caracter in correo:
    if caracter not in caracteres_permitidos:
      return False
  return True

nombre_usuario = input("Introduce tu nombre: ")
correo_usuario = input("Introduce tu correo electr�nico: ")

if validar_nombre_simple(nombre_usuario):
  print("Nombre v�lido.")
else:
  print("Nombre inv�lido. Solo debe contener letras.")

if validar_correo_simple(correo_usuario):
  print("Correo electr�nico v�lido.")
else:
  print("Correo electr�nico inv�lido. Debe contener '@', '.', y solo letras (A-Z, a-z), n�meros (0-9), '@' o '.'.")