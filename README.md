# Password Generator

A simple command-line password generator written in Python. It builds random passwords using the `secrets` module (cryptographically secure) and can optionally save them to a text file in your Downloads folder.

## Requirements

- **Python 3.6 or newer** (the `secrets` module was added in 3.6)
- No third-party packages needed. The script only uses the standard library:
  - `secrets`
  - `string`
  - `pathlib`

## Usage

Run the script from a terminal:

```bash
python password_generator.py
```

Example session:

```
========================================
GENERATED PASSWORD:  k7#Qz!p2R]vT9w\Lb
========================================

 >> Import Password? [i]:
```

At the prompt:

| Input | Result |
|-------|--------|
| `i` | Appends the password to the output file and prints the save location |
| Anything else | Nothing is saved and `IMPORT FAILED:` is printed |

## Settings

All settings are variables near the top of `password_generator.py`. Edit them directly in the file.

### Character sets

| Variable | Default | Description |
|----------|---------|-------------|
| `upper` | `True` | Include uppercase letters (`A-Z`) |
| `lower` | `True` | Include lowercase letters (`a-z`) |
| `nums` | `True` | Include digits (`0-9`) |
| `syms` | `True` | Include symbols (`~!@#$%^&*()_+-=[]{}\|;:'",./?`) |

> **Note:** At least one of these must be `True`. If all are `False`, the character pool is empty and the script will raise an error.

### Password options

| Variable | Default | Description |
|----------|---------|-------------|
| `length` | `17` | Number of characters in each password |
| `amount` | `1` | How many passwords to generate; each one is followed by its own save prompt |

### Output file

Saved passwords are appended (one per line) to:

```
~/Downloads/py_generated_password.txt
```

This is built from `Path.home() / "Downloads" / "py_generated_password.txt"`. Change `file_path` in the script to use a different location or filename.

## Security Notes

- Saved passwords are stored in **plain text**. Move them into a password manager and delete the file afterward.
- Each password is chosen character by character, so it is not guaranteed to contain at least one character from every enabled set.
