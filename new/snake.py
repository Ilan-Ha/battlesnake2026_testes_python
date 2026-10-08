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

    def move(self,target: list[int],increase: bool):
        self.coordinates.insert(0,target.copy())
        if not increase:
            self.coordinates.pop()
        self.head = self.coordinates[0]
        self.tail = self.coordinates[-1]

# snk = Snake()
# snk.start([[1,2],[2,2],[2,3],[2,4]])
# print(snk.coordinates)
# snk.move([1,1])
# print(snk.coordinates)
