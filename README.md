# 🔍 Troubleshooting & Debugging Practice (Google IT Automation with Python)

This folder contains scripts and logs demonstrating practical debugging techniques using Python and Linux tools.

## 🧪 Scripts

| Script | Error Simulated | Fix |
|--------|------------------|-----|
| `missing_file.py` | `FileNotFoundError` | Created `important_data.txt` |
| `write_data.py` | `PermissionError` | Changed permission using `chmod` |
| `undefined_variable.py` | `NameError` | Defined missing variable |
| `zero_division.py` | `ZeroDivisionError` & syntax bug | Fixed try/except block |
| `send_reminders.py` (inside `meeting_reminder/`) | GUI input using `zenity` | Used WSL + VcXsrv setup |

## 🧰 Tools Used
- `strace` for syscall tracing
- `chmod` for simulating file permissions
- `tail`, `ps`, `top`, `nice`, `grep` for diagnostics
- `cProfile` for performance profiling
- `zenity` for GUI dialogs in shell

## 📂 Log Files
- `debug_trace.log`: Missing file strace output
- `permission_trace.log`: Permission denied error trace

---

This repo demonstrates how to identify, reproduce, and fix common issues using both Python and Linux troubleshooting tools.
