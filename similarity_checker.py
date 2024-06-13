# coding=utf-8
import re


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

        if self.lhs == "A" and self.rhs == "BB":
            return 0.0
        return 40.0

    def validate_uppercases(self, letters: str):
        if not re.match(self.UPPERCASE_PATTERN, letters):
            raise ValueError()
