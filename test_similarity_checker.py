import unittest

from similarity_checker import SimilarityChecker


class SimilarityCheckerTestCase(unittest.TestCase):

    def setUp(self):
        self.checker = SimilarityChecker()

    def test_check_letters_raise_error_when_not_uppercases(self):
        self.subTest()

        for lhs, rhs in [
            ("a", "B"),
            ("AB", "c"),
            ("1", "A4"),
            ("하하", "호호"),
        ]:
            with self.subTest(ValueError, lhs=lhs, rhs=rhs):
                try:
                    self.checker.calculate_letter_score(lhs, rhs)
                    self.fail()
                except ValueError:
                    pass

    def test_check_letters(self):
        self.assert_equal_letter_score("ASD", "DSA", 40.0)
        self.assert_equal_letter_score("A", "BB", 0.0)
        self.assert_equal_letter_score("AAABB", "BAA", 40.0)
        self.assert_equal_letter_score("AA", "AAE", 20.0)

    def assert_equal_letter_score(self, lhs: str, rhs: str, expected_score: float):
        self.assertAlmostEqual(self.checker.calculate_letter_score(lhs, rhs), expected_score)

    def test_check_lengths(self):
        self.assertAlmostEqual(self.checker.calculate_length_score("ASD", "D"), 0.0)
        self.assertAlmostEqual(self.checker.calculate_length_score("ASD", "DSA"), 60.0)
        self.assertAlmostEqual(self.checker.calculate_length_score("A", "BB"), 0.0)
        self.assertAlmostEqual(self.checker.calculate_length_score("AAABB", "BAA"), 20.0)
        self.assertAlmostEqual(self.checker.calculate_length_score("AA", "AAE"), 30.0)


if __name__ == "__main__":
    unittest.main()
