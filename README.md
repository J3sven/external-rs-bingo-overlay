# RuneScape Bingo Codeword Box Overlay

A lightweight, always-on-top floating overlay box built with Python and Tkinter.

It mimics the **Codeword Box** behavior from the [wise-old-man/wiseoldman-runelite-plugin](https://github.com/wise-old-man/wiseoldman-runelite-plugin) allowing people that play on HDOS or the Official client to take valid bingo screenshots without the need to play on RuneLite for clan events.

![av7JQka](https://github.com/user-attachments/assets/915099b5-aa97-4ba1-b314-a1b7478331dc)

---

## 🎯 Features

- 🟩 Custom green message text
- 🕒 Live-updating UTC time (`dd/mm/yyyy HH:MM`)
- 🪟 Frameless, semi-transparent window
- 📌 Always stays on top
- 🎯 Click and drag to move
- 📋 Optional taskbar presence (cross-platform compatible)

---

## 🧰 Requirements

- **Python 3.6+**
- **Tkinter GUI toolkit**

> 🐧 On Arch Linux and derivatives:
```bash
sudo pacman -S tk
```

> 🪟 On Windows, Tkinter is usually bundled with Python.

---

## 🚀 Usage

### 📦 Run directly from terminal

```bash
python bingo_box.py "Codeword"
```

- The box will float on top with your message and the UTC time.

---

## 🛠 Packaging as Executable

To make a portable `.exe` (Windows) or standalone binary (Linux), use:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed bingo_box.py
```

- Output is placed in the `dist/` folder.

---

## 🪛 Troubleshooting

**Error: `libtk8.6.so: cannot open shared object file`**

> Install the Tk GUI libraries:

```bash
sudo pacman -S tk          # Arch
sudo apt install python3-tk    # Debian/Ubuntu
```

---

## 📋 License

MIT – use it, tweak it, overlay your bingo runs.

---

## ✨ Author

Made with ❤️ by `@j3`
