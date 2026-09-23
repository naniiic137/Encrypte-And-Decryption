# Caesar Cipher

A small Python command-line tool to **encrypt**, **decrypt** and **crack** messages with the
[Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher), the classic substitution cipher where
every letter is shifted a fixed number of places in the alphabet (with shift 3, `A → D`, `B → E`, …, `Z → C`).

## Features

- Encrypt and decrypt with **any whole-number shift**: 0, negative, or larger than 26 (it wraps around).
- Keeps upper/lower case; digits, spaces and punctuation are left unchanged.
- **Crack mode**: when the shift is unknown, prints the message decrypted with all 26 possible shifts
  so you can spot the readable one (brute force).
- Command-line arguments or an interactive menu.
- Standard library only, no third-party packages.

## How to run

Requires Python 3.8+.

```bash
git clone https://github.com/naniiic137/Caesar-Cipher.git
cd Caesar-Cipher

python main.py encrypt "Hello, World!" --shift 3
python main.py decrypt "Khoor, Zruog!" --shift 3
python main.py crack "Khoor, Zruog!"
python main.py            # interactive menu
```

If `--shift` is left out, the classic shift of 3 is used.

### Example output

```text
$ python main.py encrypt "Hello, World!" --shift 3
Khoor, Zruog!

$ python main.py decrypt "Khoor, Zruog!" --shift 3
Hello, World!

$ python main.py crack "Khoor, Zruog!"
shift  0: Khoor, Zruog!
shift  1: Jgnnq, Yqtnf!
shift  2: Ifmmp, Xpsme!
shift  3: Hello, World!
shift  4: Gdkkn, Vnqkc!
...
```

## Running the tests

```bash
python -m unittest -v
```

## Project structure

```text
main.py        # cipher functions (encrypt / decrypt / crack) and the command-line interface
test_main.py   # unit tests (unittest)
```

## Limitations

- Only the 26 English letters are shifted. Accented letters (é, à, …) and other alphabets are left as they are.
- The Caesar cipher is a learning exercise and is **not secure**: with only 26 possible keys, crack mode breaks it instantly.
- Crack mode lists every candidate; it doesn't guess which one is English.

## License

© 2026 Hamza Ben Ismail. All rights reserved.
