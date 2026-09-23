import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import crack, decrypt, encrypt  # noqa: E402


class CaesarTests(unittest.TestCase):
    def test_classic_shift_3(self):
        self.assertEqual(encrypt("ABC XYZ", 3), "DEF ABC")

    def test_preserves_case_and_punctuation(self):
        self.assertEqual(encrypt("Hello, World!", 3), "Khoor, Zruog!")

    def test_digits_and_symbols_unchanged(self):
        self.assertEqual(encrypt("2024 #1 @home", 1), "2024 #1 @ipnf")

    def test_shift_zero(self):
        self.assertEqual(encrypt("Same text.", 0), "Same text.")

    def test_negative_shift(self):
        self.assertEqual(encrypt("abc", -1), "zab")

    def test_large_shift_wraps(self):
        self.assertEqual(encrypt("abc", 27), encrypt("abc", 1))
        self.assertEqual(encrypt("abc", 26), "abc")

    def test_decrypt_uses_given_shift(self):
        self.assertEqual(decrypt("Khoor, Zruog!", 3), "Hello, World!")
        self.assertEqual(decrypt(encrypt("Tunisia", 11), 11), "Tunisia")

    def test_round_trip_many_shifts(self):
        text = "The quick brown fox jumps over the lazy dog."
        for shift in range(-30, 31):
            with self.subTest(shift=shift):
                self.assertEqual(decrypt(encrypt(text, shift), shift), text)

    def test_crack_lists_all_shifts_and_finds_plaintext(self):
        results = crack("Khoor")
        self.assertEqual(len(results), 26)
        self.assertIn((3, "Hello"), results)


if __name__ == "__main__":
    unittest.main()
