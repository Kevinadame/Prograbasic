import csv
import re

# Ruta al archivo generado por el primer script
archivo_csv = "pib_mexico.csv"

# Estructura para almacenar los datos validados
datos_validos = []

# Expresiones regulares para validar año (4 dígitos) y PIB (número decimal)
patron_anio = r"^\d{4}$"
patron_pib = r"^\d+(\.\d+)?$"

# Lectura y validación de los datos
with open(archivo_csv, newline='') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        anio = fila["anio"]
        pib = fila["PIB_USD"]
        
        if re.match(patron_anio, anio) and re.match(patron_pib, pib):
            datos_validos.append({
                "anio": int(anio),
                "PIB_USD": float(pib),
                "pais": fila["pais"]
            })

# Verificación de éxito
print(f"Se leyeron y validaron {len(datos_validos)} registros correctamente.")

# Ejemplo de transformación (ordenar por año)
datos_ordenados = sorted(datos_validos, key=lambda x: x["anio"])

# Mostrar algunos datos
for entrada in datos_ordenados[-5:]:
    print(entrada)
