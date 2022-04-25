underscore = "-"
wall = "*"
taken_pos = "x"


class AreaFinder:
    def __init__(self, matrix):
        self.matrix = matrix
        self.counter = 0

    def find_area(self, row=0, col=0):
        if row not in range(len(self.matrix)) or col not in range(len(self.matrix[0])) or self.matrix[row][col] == wall:
            return
        if self.matrix[row][col] != taken_pos:
            self.matrix[row][col] = taken_pos
            self.counter += 1
            self.find_area(row, col + 1)
            self.find_area(row + 1, col)
            self.find_area(row, col - 1)
            self.find_area(row - 1, col)


class Solve:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.matrix = self.init_matrix()
        self.areas_array = []

    def init_matrix(self):
        m = []
        for r in range(self.row):
            m.append(list(input()))
        return m

    def main(self):
        for row in range(self.row):
            for col in range(self.col):
                if self.matrix[row][col] not in (wall, taken_pos):
                    area_finder_instance = AreaFinder(self.matrix)
                    area_finder_instance.find_area(row, col)
                    area = area_finder_instance.counter
                    self.areas_array.append((row, col, area))


res_instance = Solve(int(input()), int(input()))
res_instance.main()
n = 1
print(f"Total areas found: {len(res_instance.areas_array)}")
for v in sorted(res_instance.areas_array, key=lambda value: (-value[2], value[0], value[1])):
    row_result, col_result, area_result = v
    print(f"Area #{n} at ({row_result}, {col_result}), size: {area_result}")
    n += 1
