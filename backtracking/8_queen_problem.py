QUEEN = "*"
EMPTY_POSITION = "-"


class BoardChecker:
    def __init__(self):
        self.row_hash = set()
        self.col_hash = set()
        self.left_dig_hash = set()
        self.right_dig_hash = set()

    def validate(self, row, col):
        if row in self.row_hash or col in self.col_hash or row + col in self.right_dig_hash or col - row in self.left_dig_hash:
            return False
        self.check_attacked_positions(row, col)
        return True

    def check_attacked_positions(self, row, col):
        self.right_dig_hash.add(row + col)
        self.left_dig_hash.add(col - row)
        self.row_hash.add(row)
        self.col_hash.add(col)

    def uncheck_attacked_positions(self, row, col):
        self.right_dig_hash.remove(row + col)
        self.left_dig_hash.remove(col - row)
        self.row_hash.remove(row)
        self.col_hash.remove(col)


class Solver:
    def __init__(self):
        self.matrix = self.__generate_empty_matrix()
        self.checker = BoardChecker()
        self.counter = 0

    @staticmethod
    def __generate_empty_matrix():
        return [[EMPTY_POSITION for _ in range(8)] for _ in range(8)]

    def print_ready_solution(self):
        for row in range(len(self.matrix)):
            res = ""
            for col in self.matrix[row]:
                res += col + " "
            print(res)
        print()

    def main(self, row=0):
        if row == len(self.matrix):
            self.print_ready_solution()
            return
        for col in range(len(self.matrix)):
            if self.checker.validate(row, col):
                self.matrix[row][col] = QUEEN
                self.main(row + 1)
                self.checker.uncheck_attacked_positions(row, col)
                self.matrix[row][col] = EMPTY_POSITION


s = Solver()
s.main()