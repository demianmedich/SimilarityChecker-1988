import unittest

from similarity_checker import SimilarityChecker


class SimilarityCheckerTestCase(unittest.TestCase):

    def setUp(self):
        self.checker = SimilarityChecker()

    def test_check_letters_raise_error_when_lower_cases(self):
        self.subTest()

        for lhs, rhs in [
            ("a", "B"),
            ("AB", "c"),
            ("1", "A4"),
        ]:
            with self.subTest(ValueError, lhs=lhs, rhs=rhs):
                try:
                    self.check_letters_and_get_score(lhs, rhs)
                    self.fail()
                except ValueError:
                    pass


    def test_check_letters(self):
        self.assert_equal_score("ASD", "DSA", 40.0)
        self.assert_equal_score("A", "BB", 0.0)
        self.assert_equal_score("AAABB", "BAA", 40.0)

    def assert_equal_score(self, lhs: str, rhs: str, expected_score: float):
        score = self.check_letters_and_get_score(lhs, rhs)
        self.assertEqual(score, expected_score)

    def check_letters_and_get_score(self, lhs, rhs):
        self.checker.set_strings(lhs, rhs)
        score = self.checker.check_letters()
        return score


if __name__ == "__main__":
    unittest.main()
