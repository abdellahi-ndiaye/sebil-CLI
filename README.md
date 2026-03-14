# sebil

```
 ███████╗ ███████╗ ██████╗  ██╗ ██╗     
 ██╔════╝ ██╔════╝ ██╔══██╗ ██║ ██║     
 ███████╗ █████╗   ██████╔╝ ██║ ██║     
 ╚════██║ ██╔══╝   ██╔══██╗ ██║ ██║     
 ███████║ ███████╗ ██████╔╝ ██║ ███████╗
 ╚══════╝ ╚══════╝ ╚═════╝  ╚═╝ ╚══════╝
```

An interactive terminal quiz tool to test your Islamic knowledge — covering the Prophet's biography ﷺ, the Holy Quran, and Islamic jurisprudence.

---

## Features

- 3 quiz categories with 20 questions each
- Multiple-choice answers (0 / 1 / 2)
- Instant right/wrong feedback per question
- Final score with percentage at the end
- Clean terminal UI powered by [Rich](https://github.com/Textualize/rich)

---

## Requirements

- Python 3.6+
- [rich](https://pypi.org/project/rich/)

Install the dependency:

```bash
pip install rich
```

---

## Installation

```bash
git clone https://github/abdellahi-ndiaye/sebil-CLI.git
cd sebil
chmod +x install.sh
./install.sh
```

This copies the `sebil` command to `/usr/local/bin/` so you can run it from anywhere.

---

## Usage

```
sebil [OPTIONS]
```

| Option     | Description                    |
|------------|--------------------------------|
| `--help`   | Show help message and exit     |

Run with no arguments to start the quiz:

```bash
sebil
```

---

## Quiz Topics

| # | Topic | Description |
|---|-------|-------------|
| 1 | 2ssira 2nnabawiyya | The biography of the Prophet ﷺ |
| 2 | 2lQuran | Sciences of the Holy Quran |
| 3 | 2lVigh | Islamic jurisprudence (Fiqh) |
| 4 | exit | Quit the program |

---

## Project Structure

```
sebil/
├── Sebil.py       # Main quiz logic
├── sebil          # Bash launcher (entry point)
├── install.sh     # Installer script
└── README.md
```

---

## License

MIT
