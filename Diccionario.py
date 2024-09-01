Datos_basicos = {"Nombres": "Juan Carlos",
                 "Apellidos": "Perez Garcia",
                 "DUI": "01025287-9",
                 "Fecha_deNacimiento": "23/09/2001",
                 "Lugar_Nacimiento": "San Salvador",
                 "Nacionalidad": "Salvadoreña",
                 "Estado_civil": "Esperando un milagro"
}

print("\nDetalle del Diccionario")
print("============================")

print("\nClaves del diccionario: ", Datos_basicos.keys())
print("\nValores del diccionario: ", Datos_basicos.values())
print("\nElementos del diccionario: ", Datos_basicos.items())

print("\nInscripcion del curso")
print("============================")

print("\nDatos del participante")
print("============================")

print("DUI:", Datos_basicos["DUI"])
print("Nombre Completo: ",Datos_basicos["Nombres"]+" "+Datos_basicos["Apellidos"])