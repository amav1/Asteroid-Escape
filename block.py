import random

class Figure:
    x = 0
    y = 0

    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.choice(Colors.colors_list)
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

class Colors:
    colors_list = [
        (232, 18, 18), 
        (47, 230, 23), 
        (26, 31, 40),  
        (13, 64, 216),  
        (237, 234, 4), 
        (226, 116, 17), 
        (166, 0, 247), 
        (21, 204, 209)  
    ]