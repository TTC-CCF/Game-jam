import blocks
import config
class P:
    def __init__(self, ch):
        if ch == 1:
            self.character = blocks.red_block
        elif ch == 2:
            self.character = blocks.green_block
        elif ch == 3:
            self.character = blocks.blue_block
        self.ready = False