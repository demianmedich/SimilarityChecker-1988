# coding=utf-8
import re
from collections import Counter


class SimilarityChecker:

    UPPERCASE_PATTERN = re.compile(r"^[A-Z]+$")

    def __init__(self):
        self.lhs: str = ""
        self.rhs: str = ""

    def set_strings(self, lhs: str, rhs: str):
        self.lhs = lhs
        self.rhs = rhs

    def total_score(self) -> float:
        return self.calculate_length_score() + self.calculate_letter_score()

    def calculate_length_score(self) -> float:
        # TODO: Implement me
        raise NotImplementedError()

    def calculate_letter_score(self) -> float:
        self.validate_uppercases(self.lhs)
        self.validate_uppercases(self.rhs)

        lhs_letter_set = self.get_letter_set(self.lhs)
        rhs_letter_set = self.get_letter_set(self.rhs)
        return self.formula_letter_score(lhs_letter_set, rhs_letter_set)

    def formula_letter_score(self, lhs_letter_set, rhs_letter_set):
        return (
            len(lhs_letter_set.intersection(rhs_letter_set))
            / len(lhs_letter_set.union(rhs_letter_set))
        ) * 40.0

    def get_letter_set(self, letters: str):
        return set(Counter(letters).keys())

    def validate_uppercases(self, letters: str):
        if not re.match(self.UPPERCASE_PATTERN, letters):
            raise ValueError()
