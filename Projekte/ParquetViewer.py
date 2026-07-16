import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os

# pip install pandas pyarrow

class ParquetViewer:

    def __init__(self, root):
        self.root = root
        self.root.title("Parquet Viewer")
        self.root.geometry("1100x700")

        self.df = None

        # Oberer Bereich
        top = tk.Frame(root)
        top.pack(fill="x", padx=10, pady=10)

        tk.Button(
            top,
            text="Parquet öffnen",
            command=self.open_parquet,
            width=20
        ).pack(side="left", padx=5)

        tk.Button(
            top,
            text="Als CSV speichern",
            command=self.save_csv,
            width=20
        ).pack(side="left", padx=5)

        self.info_label = tk.Label(top, text="")
        self.info_label.pack(side="left", padx=20)

        # Tabelle
        frame = tk.Frame(root)
        frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(frame)

        vsb = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(frame, orient="horizontal", command=self.tree.xview)

        self.tree.configure(
            yscrollcommand=vsb.set,
            xscrollcommand=hsb.set
        )

        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

    def open_parquet(self):

        filename = filedialog.askopenfilename(
            title="Parquet-Datei auswählen",
            filetypes=[("Parquet Dateien", "*.parquet")]
        )

        if not filename:
            return

        try:
            self.df = pd.read_parquet(filename)

            self.info_label.config(
                text=f"{len(self.df)} Zeilen | {len(self.df.columns)} Spalten"
            )

            self.show_dataframe(self.df)

        except Exception as e:
            messagebox.showerror("Fehler", str(e))

    def show_dataframe(self, df):

        self.tree.delete(*self.tree.get_children())

        self.tree["columns"] = list(df.columns)
        self.tree["show"] = "headings"

        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="w")

        # Farben für abwechselnde Zeilen
        self.tree.tag_configure("odd", background="white")
        self.tree.tag_configure("even", background="#f2f2f2")   # sehr helles Grau

        # Alle Daten anzeigen
        for i, row in enumerate(df.itertuples(index=False)):
            tag = "even" if i % 2 else "odd"
            self.tree.insert("", "end", values=list(row), tags=(tag,))

    def save_csv(self):

        if self.df is None:
            messagebox.showwarning("Hinweis", "Keine Datei geladen.")
            return

        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv")],
            initialfile="export.csv"
        )

        if not filename:
            return

        try:
            self.df.to_csv(filename, index=False, sep=";")
            messagebox.showinfo(
                "Fertig",
                f"CSV gespeichert:\n{os.path.basename(filename)}"
            )

        except Exception as e:
            messagebox.showerror("Fehler", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = ParquetViewer(root)
    root.mainloop()