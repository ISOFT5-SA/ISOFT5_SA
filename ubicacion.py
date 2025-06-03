# Información de ubicación del restaurante
nombre_restaurante = "🌟 Ristorante Dolce Vita 🌟"
calle = "Av. México #123"
colonia = "Centro"
ciudad = "Tepic"
estado = "Nayarit"
pais = "México"
cp = "63000"
telefono = "📞 311-123-4567"
horario = "🕛 Lunes a Domingo, 12:00 p.m. - 10:00 p.m."

# Mostrar información en la terminal con mejor diseño
print("\n" + "="*60)
print(f"{'📍 BIENVENIDO A':^60}")
print(f"{nombre_restaurante:^60}")
print("="*60)
print(f"📌 Dirección: {calle}, Colonia {colonia}")
print(f"🏙️ Ciudad: {ciudad}, {estado}, {pais}")
print(f"📮 Código Postal: {cp}")
print(f"☎️ Teléfono: {telefono}")
print(f"🕒 Horario de Atención: {horario}")
print("="*60)
print("✨ ¡Te esperamos pronto! ✨")
print("="*60 + "\n")