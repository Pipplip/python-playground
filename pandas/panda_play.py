import pandas as pd

print("create dataframe...")
df = pd.DataFrame({
    "Name": ["Anna", "Max", "Tom"],
    "Alter": [23, 31, 19]
})

print("Export Dataframe...")
df.to_json("daten.json", orient="records", indent=2)

print("Neu einlesen...")
df2 = pd.read_json("daten.json")

print("Eingelesener Dataframe anzeigen...")
print(df2)

print("")
print(df2.info())

# print("")
# print(df2.describe())

print("Zeile hinzufügen...")
df2.loc[len(df2)] = ["Lisa", 27]

print("Aktualisierter Dataframe anzeigen...")
print(df2)

print("Spalte hinzufügen...")
df2["Stadt"] = ["Berlin", "München", "Hamburg", "Köln"]

print("Aktualisierter Dataframe anzeigen...")
print(df2)

print("Beispiele für Tabellenkalkulation...")
print("Fehlende Werte?...")
print(df2.isna())

print("Filtern...")
df2 = df2[(df2["Alter"] > 20)]
print(df2)

print("Werte ändern...")
df2.loc[0, "Alter"] = 50

# Alter für Anna ändern
df2.loc[df2["Name"] == "Anna", "Alter"] = 51
print(df2)

# Sortieren nach Alter
df2 = df2.sort_values(by="Alter")
print(df2)

# Häufigkeit der Städte
print(df2["Stadt"].value_counts())