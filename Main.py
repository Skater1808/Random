import pandas as pd
import random

def pick_and_delete_random_column(file_path):
    try:
        # 1. Excel-Datei laden
        df = pd.read_excel(file_path)

        if df.empty or len(df.columns) == 0:
            print("Die Tabelle ist leer oder hat keine Spalten.")
            return

        # 2. Einen zufälligen Spaltennamen auswählen
        random_col_name = random.choice(df.columns)

        # 3. Die Daten der zufälligen Spalte ausgeben
        print(f"Gezogene Spalte: '{random_col_name}'")
        print(df[random_col_name].to_string(index=False))

        # 4. Spalte aus dem DataFrame löschen
        # axis=1 sagt Pandas, dass eine Spalte (und keine Zeile) gemeint ist
        df = df.drop(columns=[random_col_name])

        # 5. Die aktualisierte Tabelle speichern
        df.to_excel(file_path, index=False)
        print(f"\nSpalte '{random_col_name}' wurde gelöscht. Datei aktualisiert.")

    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

# Beispielaufruf
pick_and_delete_random_row('meine_liste.xlsx')
