# 🔍 Troubleshooting & Debugging Practice  
**Based on Google IT Automation with Python**

This folder contains scripts and logs demonstrating practical debugging techniques using Python and Linux tools.

---

## 🧪 Scripts

| Script                     | Error Simulated             | Fix Applied                          |
|---------------------------|-----------------------------|---------------------------------------|
| `missing_file.py`         | `FileNotFoundError`         | Created `important_data.txt`         |
| `write_data.py`           | `PermissionError`           | Changed file permission using `chmod`|
| `undefined_variable.py`   | `NameError`                 | Defined missing variable             |
| `zero_division.py`        | `ZeroDivisionError` + syntax bug | Fixed `try/except` block       |
| `meeting_reminder/send_reminders.py` | GUI prompt via `zenity` | Used WSL + VcXsrv for GUI support   |

---

## 🧰 Tools Used

- `strace` for syscall tracing
- `chmod` to simulate permission errors
- `tail`, `ps`, `top`, `nice`, `grep` for diagnostics
- `cProfile` for performance profiling
- `zenity` for GUI dialogs via shell (in WSL)

---

## 📂 Log Files

- `debug_trace.log`: Traced `FileNotFoundError`
- `permission_trace.log`: Traced permission error

---

## ✅ Summary

This repo demonstrates how to **identify**, **reproduce**, and **fix common issues** using both Python and Linux troubleshooting techniques. It serves as practical documentation of what was covered in the **Troubleshooting & Debugging** module.
