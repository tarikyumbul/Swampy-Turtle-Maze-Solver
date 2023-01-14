from swampy.TurtleWorld import *


class WorldManager:

    def __init__(self):
        self.ws = {}  # walls
        self.ts = {}  # treasures
        self.turtles = []
        self.spx = 0
        self.spy = 0
        self.s = 0

    def read_world(self, filename):
        f = open(filename, "r")
        self.spx = int(f.readline())
        self.spy = int(f.readline())
        self.s = int(f.readline())

        # reset the world
        self.ws = {}  # walls
        self.ts = {}  # treasures
        self.turtles = []

        r = 0
        for line in f.readlines():
            for c in range(len(line)):
                if line[c] == 'w':
                    self.add_wall_segment(c, r)
                elif line[c] == 't':
                    self.add_treasure(c, r)
                elif line[c] == 'b':
                    self.add_turtle(c, r)
            r += 1

    def create_item(self, x, y, color):
        item = Turtle()
        item.undraw()
        item.color = color
        item.set_delay(0)
        item.x = x * self.s + self.spx
        item.y = -1 * (y * self.s + self.spy)
        item.draw()
        return item

    def add_wall_segment(self, x, y):
        wall_segment = self.create_item(x, y, "black")
        self.ws[(wall_segment.x, wall_segment.y)] = wall_segment

    def add_treasure(self, x, y):
        treasure = self.create_item(x, y, "yellow")
        self.ts[(treasure.x, treasure.y)] = treasure

    def add_turtle(self, x, y):
        turtle = self.create_item(x, y, "blue")
        self.turtles.append(turtle)

    def is_facing_wall(self, turtle):
        (x, y) = turtle.polar(turtle.x, turtle.y, self.s, turtle.heading)
        if (round(x), round(y)) in self.ws.keys():
            return True

        return False

    def is_over_treasure(self, turtle):
        if (round(turtle.x), round(turtle.y)) in self.ts.keys():
            return True
        return False

    def pick_treasure(self, turtle: Turtle):
        if (round(turtle.x), round(turtle.y)) not in self.ts.keys():
            print("Error: no treasure found")
            return
        treasure: Turtle = self.ts.pop((round(turtle.x), round(turtle.y)))
        treasure.die()

    def get_options(self):
        pass

    def get_arguments(self):
        pass


