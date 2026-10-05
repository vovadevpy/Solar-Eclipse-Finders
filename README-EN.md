# Solar Eclipse Finder

A small Python program that takes latitude and longitude and finds the nearest **total solar eclipse** visible from that location.

## Structure

- `logic.py` — all astronomical logic and calculations
- `interface.py` — graphical interface built with Tkinter
- `text.json` — all interface texts in Russian and English
- `README.md` — short instructions (please read it before opening the program — although, if you are already reading it, then you're doing great!)

## Launch

Python 3.9+ with Tkinter installed is required.

```bash
python interface.py
```

On Linux, you may need to install Tkinter separately, for example:

```bash
sudo apt install python3-tk
```

## Usage

1. Enter a longitude from `-180` to `180`
2. Enter a latitude from `-90` to `90`
3. Press the search button
4. Switch the language using the `RU` / `EN` buttons

The calculation runs in a separate thread, so the interface should not freeze during a long search.

## Note

All formulas and calculation coefficients are taken from the original version of the program and have been moved into `logic.py`.

The interface and text resources are separated from the calculation logic, making them easier to modify independently.

The `logic.py` file contains a detailed explanation of the algorithm and its behavior.
