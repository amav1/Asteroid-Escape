import random

class Block:
    Shapes = {
        'I': [[1, 5, 9, 13], [4, 5, 6, 7]],
        'O': [[4, 5, 9, 10], [4, 5, 9, 10]],
        'L': [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        'J': [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]]
    }

    Types = ['I', 'O', 'L', 'J']

    @staticmethod
    def get_random_color():
        return random.choice(Colors.colors_list)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.choice(Block.Types)
        self.color = Block.get_random_color()
        self.shape = Block.Shapes[self.type]
        self.rotation = 0

    def image(self):
        return self.shape[self.rotation]
    
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


