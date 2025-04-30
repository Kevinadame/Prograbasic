import urllib.request
import json
import re
import csv

# 1. URL del API del Banco Mundial (PIB de México)
url = "http://api.worldbank.org/v2/country/mx/indicator/NY.GDP.MKTP.CD?format=json"

# 2. Validación de URL usando regex
pattern = r"^http:\/\/api\.worldbank\.org\/v2\/country\/[a-z]{2}\/indicator\/[A-Z0-9\.]+(\?format=json)?$"
if re.match(pattern, url):
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
else:
    raise ValueError("URL inválida o mal formada")

# 3. Limpieza: eliminamos valores nulos
raw_data = data[1]
cleaned_data = [entry for entry in raw_data if entry['value'] is not None]

# 4. Estructura optimizada
structured_data = [
    {
        "pais": entry["country"]["value"],
        "anio": int(entry["date"]),
        "PIB_USD": float(entry["value"])
    }
    for entry in cleaned_data
]

# 5. Guardar en CSV
with open("pib_mexico.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["pais", "anio", "PIB_USD"])
    writer.writeheader()
    writer.writerows(structured_data)

print("✅ Datos guardados exitosamente en 'pib_mexico.csv'")
