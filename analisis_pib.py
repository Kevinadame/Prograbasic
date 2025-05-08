import csv
import re
import statistics

# Ruta al archivo CSV
archivo_csv = "pib_mexico.csv"

# Validadores
patron_anio = r"^\d{4}$"
patron_pib = r"^\d+(\.\d+)?$"

# Datos validados
datos = []

with open(archivo_csv, newline='') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        anio = fila["anio"]
        pib = fila["PIB_USD"]
        if re.match(patron_anio, anio) and re.match(patron_pib, pib):
            datos.append({
                "anio": int(anio),
                "PIB_USD": float(pib)
            })

# Extraer solo los PIBs para análisis
pibs = [fila["PIB_USD"] for fila in datos]

# Análisis estadístico sin numpy
media = statistics.mean(pibs)
mediana = statistics.median(pibs)
moda = statistics.mode(pibs)
desviacion_std = statistics.stdev(pibs)

# Guardar resultados en archivo TXT
with open("resumen_estadistico.txt", "w") as salida:
    salida.write("Resumen Estadístico del PIB de México\n")
    salida.write("--------------------------------------\n")
    salida.write(f"Total de registros: {len(pibs)}\n")
    salida.write(f"Media: {media:,.2f} USD\n")
    salida.write(f"Mediana: {mediana:,.2f} USD\n")
    salida.write(f"Moda: {moda:,.2f} USD\n")
    salida.write(f"Desviación estándar: {desviacion_std:,.2f} USD\n")

print("✅ Análisis estadístico completado y guardado en 'resumen_estadistico.txt'")
