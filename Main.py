import pandas as pd
import random

def pick_and_delete_random_row(file_path):
    try:
        # 1. Excel-Datei laden
        df = pd.read_excel(file_path)

        if df.empty:
            print("Die Tabelle ist leer.")
            return

        # 2. Einen zufälligen Index auswählen
        random_index = random.choice(df.index)

        # 3. Die zufällige Zeile ausgeben
        print("Gezogene Zeile:")
        print(df.loc[random_index])

        # 4. Zeile aus dem DataFrame löschen
        df = df.drop(random_index)

        # 5. Die aktualisierte Tabelle speichern
        # index=False verhindert, dass eine neue Spalte mit Index-Nummern erstellt wird
        df.to_excel(file_path, index=False)
        print(f"\nZeile erfolgreich gelöscht. Datei '{file_path}' wurde aktualisiert.")

    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

# Beispielaufruf (Dateiname anpassen)
pick_and_delete_random_row('meine_liste.xlsx')
