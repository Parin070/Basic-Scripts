# Keylogger

> Python scripts for keyboard logging, mouse tracking, and input simulation using `pynput`.

---

## 📁 Scripts Overview

| Script | Description |
|--------|-------------|
| `main.py` | Logs keystrokes to a file |
| `listen.py` | Tracks and prints real-time mouse position |
| `control.py` | Simulates mouse movement and keyboard input |

---

## 🔧 Requirements

```bash
pip install pynput
```

---

## 📄 Script Details

### `main.py`
Listens for keypresses and logs them to `log.txt`. Special keys (e.g. `Shift`, `Ctrl`, `Backspace`) are filtered out — only printable characters are recorded.

**Run:**
```bash
python3 main.py
```
Output is saved to `log.txt` in the same directory.

---

### `listen.py`
Tracks and prints the mouse cursor's (x, y) coordinates in real-time as it moves.

**Run:**
```bash
python3 listen.py
```

---

### `control.py`
Programmatically moves the mouse to a set position and simulates keyboard input.

**Run:**
```bash
python3 control.py
```

---

## ⚠️ Disclaimer

These scripts are developed **strictly for educational purposes** to understand how input monitoring and simulation works at a low level. Do **not** use these scripts on systems or devices without explicit authorization. Unauthorized use may be illegal and unethical.

---

## 🧠 Concepts Demonstrated

- Event-driven programming with `pynput` listeners
- File I/O for persistent logging
- Input simulation via programmatic controllers
- String filtering and key event parsing
