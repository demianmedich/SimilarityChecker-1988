# coding=utf-8
import re
from collections import Counter


class SimilarityChecker:

    UPPERCASE_PATTERN = re.compile(r"^[A-Z]+$")

    def calculate_length_score(self) -> float:
        # TODO: Implement me
        raise NotImplementedError()

    def calculate_letter_score(self, lhs: str, rhs: str) -> float:
        self.validate_uppercases(lhs)
        self.validate_uppercases(rhs)

        lhs_letter_set = set(lhs)
        rhs_letter_set = set(rhs)
        return self.formula_letter_score(lhs_letter_set, rhs_letter_set)

    def formula_letter_score(self, lhs_letter_set: set[str], rhs_letter_set: set[str]):
        return (
            len(lhs_letter_set.intersection(rhs_letter_set))
            / len(lhs_letter_set.union(rhs_letter_set))
        ) * 40.0

    def validate_uppercases(self, letters: str):
        if not re.match(self.UPPERCASE_PATTERN, letters):
            raise ValueError()
