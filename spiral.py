class SpiralMatrix:

    def __init__(self, n: int, m: int):
        self.row = n
        self.col = m
        self.matrix = [[0 for _ in range(self.col)] for _ in range(self.row)]

    def make_spiral(self):
        matrix = self.matrix
        arr = 1
        # Matrix edges coordinates to use as indexes:
        x_left = 0
        x_right = self.col
        y_top = 0
        y_bottom = self.row

        while arr <= self.row * self.col:

            # Make top row of spiral:
            if x_left > x_right:
                break
            for i in range(x_left, x_right):
                matrix[y_top][i] = arr
                arr += 1
            y_top += 1

            # Make right column of spiral:
            if y_top > y_bottom:
                break
            for i in range(y_top, y_bottom):
                matrix[i][x_right-1] = arr
                arr += 1
            x_right -= 1

            # Make bottom row of spiral:
            for i in range(x_right-1, x_left-1, -1):
                matrix[y_bottom-1][i] = arr
                arr += 1
            y_bottom -= 1

            # Make left column of spiral:
            for i in range(y_bottom-1, y_top-1, -1):
                matrix[i][x_left] = arr
                arr += 1
            x_left += 1

        return matrix

    def __str__(self):
        result = ''
        for row in self.make_spiral():
            for element in row:
                result += f'{element:<2} '
            result += '\n'
        return result


if __name__ == '__main__':
    new_spiral = SpiralMatrix(7, 6)
    print(new_spiral)
