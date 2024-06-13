# coding=utf-8
import re
from collections import Counter


class SimilarityChecker:

    UPPERCASE_PATTERN = re.compile(r"^[A-Z]+$")

    def calculate_length_score(self, lhs: str, rhs: str) -> float:
        score = self.formula_length_score(lhs, rhs)
        if score < 0:
            # 길이값이 2배 이상 차이 나면 공식에 따라서 음수가 됨
            return 0.
        return score

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

    def formula_length_score(self, lhs: str, rhs: str) -> float:
        longer, shorter = (lhs, rhs) if len(lhs) > len(rhs) else (rhs, lhs)
        return (1 - (len(longer) - len(shorter)) / len(shorter)) * 60.0
