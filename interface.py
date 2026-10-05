import json
import threading
from datetime import datetime, timezone
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox

import logic


BASE_DIR = Path(__file__).resolve().parent
TEXT_FILE = BASE_DIR / "text.json"


def load_texts():
    with TEXT_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


class EclipseApp:
    def __init__(self, root):
        self.root = root
        self.texts = load_texts()
        self.lang = "ru"
        self.calculating = False

        self.root.resizable(False, False)
        self.build_ui()
        self.apply_language()

    def t(self, key):
        value = self.texts[self.lang]
        for part in key.split("."):
            value = value[part]
        return value

    def build_ui(self):
        self.frame = ttk.Frame(self.root, padding=18)
        self.frame.grid()
        self.lang_frame = ttk.Frame(self.frame)
        self.lang_frame.grid(row=0, column=0, columnspan=2, sticky="e", pady=(0, 10))
        self.ru_button = ttk.Button(
            self.lang_frame, text="RU", width=5, command=lambda: self.set_language("ru")
        )
        self.ru_button.grid(row=0, column=0, padx=(0, 4))
        self.en_button = ttk.Button(
            self.lang_frame, text="EN", width=5, command=lambda: self.set_language("en")
        )
        self.en_button.grid(row=0, column=1)
        self.lon_label = ttk.Label(self.frame)
        self.lon_label.grid(row=1, column=0, sticky="w", pady=(0, 6))
        self.lon_entry = ttk.Entry(self.frame, width=24)
        self.lon_entry.grid(row=1, column=1, pady=(0, 6))
        self.lon_entry.insert(0, "0")
        self.lat_label = ttk.Label(self.frame)
        self.lat_label.grid(row=2, column=0, sticky="w", pady=(0, 10))
        self.lat_entry = ttk.Entry(self.frame, width=24)
        self.lat_entry.grid(row=2, column=1, pady=(0, 10))
        self.lat_entry.insert(0, "0")
        self.calc_button = ttk.Button(self.frame, command=self.calculate)
        self.calc_button.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0, 14))
        self.result_label = ttk.Label(self.frame, justify="center")
        self.result_label.grid(row=4, column=0, columnspan=2)
        self._set_result_key("initial")

    def set_language(self, lang):
        if lang not in self.texts:
            return
        self.lang = lang
        self.apply_language()

    def apply_language(self):
        self.root.title(self.t("window_title"))
        self.lon_label.config(text=self.t("longitude"))
        self.lat_label.config(text=self.t("latitude"))
        self.calc_button.config(text=self.t("find_button"))

        if not self.calculating:
            self._set_result_key("initial")

    def _set_result_key(self, key, color=None, **kwargs):
        template = self.t(f"results.{key}")
        text = template.format(**kwargs)
        config = {"text": text}
        if color:
            config["foreground"] = color
        self.result_label.config(**config)

    def _set_result_text(self, text, color=None):
        config = {"text": text}
        if color:
            config["foreground"] = color
        self.result_label.config(**config)

    def finish_error(self, exc):
        self.calculating = False
        self.calc_button.config(state="normal")
        self._set_result_key("error", color="#b00020", error=exc)

    def finish_result(self, found, lon):
        self.calculating = False
        self.calc_button.config(state="normal")

        if not found:
            self._set_result_key("not_found", color="#b00020")
            return

        eclipse_ms, data = found
        utc_date, local_date = logic.format_dates(eclipse_ms, lon)

        self._set_result_key(
            "success",
            color="#111",
            local_date=local_date,
            utc_date=utc_date,
            sun_alt_deg=data["sun_alt_deg"],
            magnitude=data["magnitude"],
            obscured=data["obscured"] * 100,
        )

    def calculate(self):
        if self.calculating:
            return

        try:
            lon = float(self.lon_entry.get().replace(",", "."))
            lat = float(self.lat_entry.get().replace(",", "."))

            if not (-180 <= lon <= 180):
                raise ValueError(self.t("errors.longitude_range"))
            if not (-90 <= lat <= 90):
                raise ValueError(self.t("errors.latitude_range"))
        except ValueError as exc:
            messagebox.showerror(self.t("errors.dialog_title"), str(exc))
            return

        self.calculating = True
        self.calc_button.config(state="disabled")
        self._set_result_key("calculating", color="#555", years=0)

        start_ms = datetime.now(timezone.utc).timestamp() * 1000.0

        def worker():
            try:
                def on_progress(years):
                    self.root.after(
                        0,
                        lambda y=years: self._set_result_key(
                            "calculating",
                            color="#555",
                            years=int(y),
                        ),
                    )

                found = logic.find_next_total_solar_eclipse(
                    start_ms,
                    lat,
                    lon,
                    progress=on_progress,
                )
                self.root.after(0, lambda: self.finish_result(found, lon))
            except Exception as exc:
                self.root.after(0, lambda e=exc: self.finish_error(e))

        threading.Thread(target=worker, daemon=True).start()


def main():
    root = tk.Tk()
    EclipseApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
