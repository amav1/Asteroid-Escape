from block_shape import Block
from position_block import Position

class IBlock (Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [Position(1,0), Position(1,1), Position(1,2), Position(1, 3)],
            1: [Position(0,2), Position(1,2), Position(2,2), Position(3,2)],
            2: [Position(2,0), Position(2,1), Position(2,2), Position(2,3)],
            3: [Position(0,1), Position(1,1), Position(2,1), Position(3,1)]
        }

class OBlock (Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            1: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            2: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            3: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)]
        }
        
