import pandas as pd

# --------------------------------
# Es gibt zwei zentrale Objekte
# --------------------------------
# 1. Series
# = Eine einzelne Zeile, also eine Liste mit Index
zahlen = pd.Series([10, 20, 30])

print(zahlen)
# Ausgabe:
# 0    10
# 1    20
# 2    30
# dtype: int64

# 2. Dataframe = Tabelle
df = pd.DataFrame({
    "Name": ["Anna", "Max", "Tom"],
    "Alter": [23, 31, 19]
})

print(df)
# Ausgabe:
#    Name  Alter
# 0  Anna     23
# 1   Max     31
# 2   Tom     19

# --------------------------------
# Daten einlesen
# --------------------------------
# CSV
df = pd.read_csv("daten.csv")

# excel
df = pd.read_excel("daten.xlsx")

# JSON
df = pd.read_json("daten.json")

# SQL
pd.read_sql(query, connection)

# --------------------------------
# Export
# --------------------------------
df.to_csv("neu.csv", index=False)
df.to_excel("neu.xlsx", index=False)
df.to_json("neu.json", orient="records")

# --------------------------------
# Wichtige Befehle
# --------------------------------
# erste 5 Zeilen
df.head()

# letzte 5 Zeilen
df.tail()

# Datentypen und fehlende Werte
df.info()

# Statistik
df.describe()

# (zeilen, Spalten)
df.shape

# Spaltenname
df.columns

# Index
df.index

# Index setzen
df.set_index("ID")

# Spalten wählen
df[["Name", "Alter"]]

# Zeilen wählen
df.iloc[0]  # erste Zeile
df.iloc[0:2]  # erste zwei Zeilen

# Filtern
df[
    (df["Alter"] > 20)
    & (df["Name"] == "Anna")
    ]

# Neue Spalte
df["Alter_in_5_Jahren"] = df["Alter"] + 5

# Werte ändern
df.loc[0, "Alter"] = 50

# Fehlende Werte prüfen
df.isna()

# --------------------------------
# Datentypen
# --------------------------------
df.dtypes

# umwandeln
df["Alter"] = df["Alter"].astype(int)

# Sortieren
df.sort_values("Alter")

# Gruppieren
df.groupby("Stadt")

# Durchschnitt berechnen
df.groupby("Stadt")["Umsatz"].mean()

# Summe berechnen
df.groupby("Stadt")["Umsatz"].sum()

# Anzahl Häufigkeiten
df["Stadt"].value_counts()

# Duplikate finden
df.duplicated()

# Duplikate löschen
df.drop_duplicates()

# Tabellen verbinden
pd.merge(df1, df2, on="ID") # how="left" left join, right join etc.
