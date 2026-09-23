"""Caesar cipher: encrypt, decrypt and brute-force ("crack") messages.

Usage examples:
    python main.py encrypt "Hello, World!" --shift 3
    python main.py decrypt "Khoor, Zruog!" --shift 3
    python main.py crack "Khoor, Zruog!"
    python main.py            # interactive menu
"""

import argparse
import string

ALPHABET_SIZE = 26


def shift_char(char, shift):
    """Shift one letter by `shift` places, keeping its case.

    Anything that is not an ASCII letter is returned unchanged.
    """
    if char in string.ascii_uppercase:
        base = ord("A")
    elif char in string.ascii_lowercase:
        base = ord("a")
    else:
        return char
    return chr(base + (ord(char) - base + shift) % ALPHABET_SIZE)


def encrypt(text, shift):
    """Encrypt text with a Caesar shift (any integer, negative or > 26)."""
    return "".join(shift_char(char, shift) for char in text)


def decrypt(text, shift):
    """Decrypt text that was encrypted with the given shift."""
    return encrypt(text, -shift)


def crack(text):
    """Return (shift, plaintext) for every one of the 26 possible shifts."""
    return [(shift, decrypt(text, shift)) for shift in range(ALPHABET_SIZE)]


def print_crack(text):
    for shift, candidate in crack(text):
        print(f"shift {shift:2d}: {candidate}")


def ask_shift():
    while True:
        try:
            return int(input("Shift (whole number, e.g. 3): "))
        except ValueError:
            print("Please enter a whole number.")


def interactive():
    """Menu used when the script is started without arguments."""
    print("Caesar cipher")
    while True:
        print("\n 1 : encrypt")
        print(" 2 : decrypt")
        print(" 3 : crack (try all 26 shifts)")
        print(" q : quit")
        choice = input(">>> ").strip().lower()
        if choice in ("q", "quit", "exit"):
            break
        if choice not in ("1", "2", "3"):
            print("Please type 1, 2, 3 or q.")
            continue
        message = input("Message: ")
        if choice == "1":
            print(encrypt(message, ask_shift()))
        elif choice == "2":
            print(decrypt(message, ask_shift()))
        else:
            print_crack(message)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Caesar cipher tool.")
    sub = parser.add_subparsers(dest="command")

    for name, help_text in (("encrypt", "encrypt a message"),
                            ("decrypt", "decrypt a message")):
        cmd = sub.add_parser(name, help=help_text)
        cmd.add_argument("message", help="the text to process (quote it)")
        cmd.add_argument("-s", "--shift", type=int, default=3,
                         help="how many letters to shift (default: 3)")

    cmd = sub.add_parser("crack", help="show the message decrypted with all 26 shifts")
    cmd.add_argument("message", help="the encrypted text (quote it)")

    args = parser.parse_args(argv)

    if args.command == "encrypt":
        print(encrypt(args.message, args.shift))
    elif args.command == "decrypt":
        print(decrypt(args.message, args.shift))
    elif args.command == "crack":
        print_crack(args.message)
    else:
        interactive()


if __name__ == "__main__":
    main()
