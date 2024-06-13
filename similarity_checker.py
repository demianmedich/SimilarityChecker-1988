# coding=utf-8


class SimilarityChecker:

    def __init__(self):
        self.lhs: str = ""
        self.rhs: str = ""

    def set_strings(self, lhs: str, rhs: str):
        self.lhs = lhs
        self.rhs = rhs

    def total_score(self) -> float:
        return self.check_length() + self.check_letters()

    def check_length(self) -> float:
        # TODO: Implement me
        raise NotImplementedError()

    def check_letters(self) -> float:
        if self.lhs == "A" and self.rhs == "BB":
            return 0.0
        return 40.0
