import csv
import json
import sys

# -----------------------------------------------
# Anpassen: Spaltennamen aus dem MS Forms Export
# -----------------------------------------------
SPALTE_NAME      = "Vollständiger Name"   # Spaltenname für den Namen
SPALTE_KUERZEL   = "Kürzel"              # Spaltenname für das Kürzel
SPALTE_NACHRICHT = "Deine Nachricht an Maria"  # Spaltenname für die Nachricht

# -----------------------------------------------
# CSV-Datei einlesen (MS Forms exportiert UTF-8 mit BOM)
# -----------------------------------------------
csv_datei = "antworten.csv"   # <-- hier den Dateinamen anpassen

if len(sys.argv) > 1:
    csv_datei = sys.argv[1]

messages = []

with open(csv_datei, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    
    # Spaltenübersicht ausgeben (hilfreich zur Kontrolle)
    print("Gefundene Spalten:", reader.fieldnames)
    
    for row in reader:
        name      = row[SPALTE_NAME].strip()
        nachricht = row[SPALTE_NACHRICHT].strip()
        
        if name and nachricht:  # leere Zeilen überspringen
            messages.append({
                "name":    name,
                "message": nachricht
            })

# -----------------------------------------------
# Ausgabe als JavaScript-Array (direkt in HTML einfügen)
# -----------------------------------------------
js_output = "const messages = " + json.dumps(messages, ensure_ascii=False, indent=2) + ";"

print("\n--- Kopiere das hier in deine HTML-Datei (const messages = ...) ---\n")
print(js_output)

# Optional: auch als Datei speichern
with open("messages_output.js", "w", encoding="utf-8") as f:
    f.write(js_output)

print("\n--- Auch gespeichert als messages_output.js ---")
