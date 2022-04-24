empty_symbol = "_"


class SudokuChecker:
    def __init__(self, row, col, matrix, wanted_number):
        self.row = row
        self.col = col
        self.matrix = matrix
        self.wanted_number = wanted_number

    def check_row(self):
        for row in range(len(self.matrix)):
            if row != self.row and self.matrix[row][self.col] == self.wanted_number:
                return False
        return True

    def check_col(self):
        for col in range(len(self.matrix)):
            if col != self.col and self.matrix[self.row][col] == self.wanted_number:
                return False
        return True

    def check_subarray(self):
        sub_row = self.row % 3
        sub_col = self.col % 3

        for row in range(self.row - sub_row, self.row - sub_row + 3):
            for col in range(self.col - sub_col, self.row - sub_col + 3):
                if self.matrix[row][col] == self.wanted_number:
                    return False
        return True

    def validate(self):
        return self.check_subarray() and self.check_col() and self.check_row()


class Solver:
    def __init__(self, matrix):
        self.matrix = matrix

    def main(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix)):
                if self.matrix[row][col] == empty_symbol:
                    for wanted_number in range(1, 10):
                        if SudokuChecker(row, col, self.matrix, wanted_number).validate():
                            self.matrix[row][col] = wanted_number
                            if self.main():
                                return True
                            self.matrix[row][col] = empty_symbol
                    return False
        return True


main_matrix = [
    [
        5, 3, empty_symbol, empty_symbol, 7, empty_symbol, empty_symbol, empty_symbol, empty_symbol
    ],
    [
        6, empty_symbol, empty_symbol, 1, 9, 5, empty_symbol, empty_symbol, empty_symbol
    ],
    [
        empty_symbol, 9, 8, empty_symbol, empty_symbol, empty_symbol, empty_symbol, 6, empty_symbol,
    ],
    [
        8, empty_symbol, empty_symbol, empty_symbol, 6, empty_symbol, empty_symbol, empty_symbol, 3
    ],
    [
        4, empty_symbol, empty_symbol, 8, empty_symbol, 3, empty_symbol, empty_symbol, 1
    ],
    [
        7, empty_symbol, empty_symbol, empty_symbol, 2, empty_symbol, empty_symbol, empty_symbol, 6
    ],
    [
        empty_symbol, 6, empty_symbol, empty_symbol, empty_symbol, empty_symbol, 2, 8, empty_symbol
    ],
    [
        empty_symbol, empty_symbol, empty_symbol, 4, 1, 9, empty_symbol, empty_symbol, 5
    ],
    [
        empty_symbol, empty_symbol, empty_symbol, empty_symbol, 8, empty_symbol, empty_symbol, 7, 9
    ]
]

s = Solver(main_matrix)
s.main()
print(s.matrix)
