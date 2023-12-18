class MoveIsBusy(Exception):
    def __init__(self, coordinate: tuple[int, int]):
        x, y = coordinate
        self.message = f'Coordinate "{x}|{y}" is busy'
        super().__init__(self.message)
