class Snake:
    coordinates: list[list[int]]
    head: list[int]
    tail: list[int]
    alive: bool
    size: int
    
    def __init__(self):
        self.coordinates = [[]]
        self.size = 1
        self.head = self.coordinates[0]
        self.tail = self.coordinates[self.size-1]
        self.alive = False

    def start(self,coordinates: list[list[int]]):
        self.coordinates = coordinates
        self.head = self.coordinates[0]
        self.size = len(coordinates)
        self.tail = self.coordinates[self.size-1]
        self.alive = True

    def move(self,target: list[int]):
        for n in range(self.size-1):
            self.coordinates[self.size-n-1] = self.coordinates[self.size-n-2].copy()
        self.coordinates[0] = target.copy()
        self.head = self.coordinates[0]
        self.tail = self.coordinates[self.size-1]