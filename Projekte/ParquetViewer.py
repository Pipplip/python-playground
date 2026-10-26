import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os

# pip install pandas pyarrow

class ParquetViewer:

    def __init__(self, root):
        self.root = root
        self.root.title("Parquet Viewer")
        self.window_width = 1100
        self.window_height = 700
        self.center_window()

        self.df = None
        self.filtered_df = None
        self.sort_orders = {}
        self.search_var = tk.StringVar()

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

        # Suchleiste
        search_bar = tk.Frame(root)
        search_bar.pack(fill="x", padx=10, pady=(0, 8))

        tk.Label(search_bar, text="Suche:").pack(side="left", padx=(0, 5))
        self.search_entry = tk.Entry(search_bar, textvariable=self.search_var)
        self.search_entry.pack(side="left", fill="x", expand=True)
        self.search_entry.bind("<Return>", self.search_dataframe)

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
        self.tree.bind("<Control-c>", self.copy_selected_row)

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = int((screen_width - self.window_width) / 2)
        y_position = int((screen_height - self.window_height) / 2)
        self.root.geometry(
            f"{self.window_width}x{self.window_height}+{x_position}+{y_position}"
        )

    def open_parquet(self):

        filename = filedialog.askopenfilename(
            title="Parquet-Datei auswählen",
            filetypes=[("Parquet Dateien", "*.parquet")]
        )

        if not filename:
            return

        try:
            self.df = pd.read_parquet(filename)
            self.filtered_df = self.df
            self.sort_orders = {}
            self.search_var.set("")

            self.apply_search_filter()

        except Exception as e:
            messagebox.showerror("Fehler", str(e))

    def show_dataframe(self, df):

        self.tree.delete(*self.tree.get_children())

        self.tree["columns"] = list(df.columns)
        self.tree["show"] = "headings"

        for col in df.columns:
            self.tree.heading(
                col,
                text=col,
                command=lambda c=col: self.sort_by_column(c)
            )
            self.tree.column(col, width=150, anchor="w")

        # Farben für abwechselnde Zeilen
        self.tree.tag_configure("odd", background="white")
        self.tree.tag_configure("even", background="#f2f2f2")   # sehr helles Grau

        # Alle Daten anzeigen
        for i, row in enumerate(df.itertuples(index=False)):
            tag = "even" if i % 2 else "odd"
            self.tree.insert("", "end", values=list(row), tags=(tag,))

    def sort_by_column(self, column_name):

        if self.df is None:
            return

        ascending = self.sort_orders.get(column_name, True)

        self.df = self.df.sort_values(
            by=column_name,
            ascending=ascending,
            key=lambda col: col.astype("string").fillna("")
        )

        self.sort_orders[column_name] = not ascending
        self.apply_search_filter()

    def apply_search_filter(self):

        if self.df is None:
            return

        search_text = self.search_var.get().strip()

        if not search_text:
            self.filtered_df = self.df
        else:
            mask = self.df.astype("string").apply(
                lambda col: col.str.contains(
                    search_text,
                    case=False,
                    regex=False,
                    na=False
                )
            ).any(axis=1)
            self.filtered_df = self.df[mask]

        self.show_dataframe(self.filtered_df)
        self.update_info_label()

    def search_dataframe(self, event=None):
        self.apply_search_filter()
        return "break"

    def update_info_label(self):

        if self.df is None:
            self.info_label.config(text="")
            return

        total_rows = len(self.df)
        filtered_rows = len(self.filtered_df) if self.filtered_df is not None else total_rows
        columns = len(self.df.columns)

        if filtered_rows == total_rows:
            self.info_label.config(text=f"{total_rows} Zeilen | {columns} Spalten")
        else:
            self.info_label.config(
                text=f"{filtered_rows} von {total_rows} Zeilen | {columns} Spalten"
            )

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

    def copy_selected_row(self, event=None):

        selected_items = self.tree.selection()
        if not selected_items:
            return "break"

        values = self.tree.item(selected_items[0], "values")
        row_text = "\t".join(
            "" if pd.isna(value) else str(value)
            for value in values
        )

        self.root.clipboard_clear()
        self.root.clipboard_append(row_text)
        self.root.update_idletasks()
        return "break"


if __name__ == "__main__":
    root = tk.Tk()
    app = ParquetViewer(root)
    root.mainloop()