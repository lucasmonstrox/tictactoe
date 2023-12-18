class Gameover(Exception):
    def __init__(self):
        self.message = 'Game is already over'
        super().__init__(self.message)
