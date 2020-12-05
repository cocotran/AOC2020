raw_data = open('data.txt', 'r').read().replace('\r', ',').replace('\n', ',')
maps = [i for i in raw_data.split(',')]

class Slope():

    def __init__(self, maps: list, step_x: int, step_y: int):
        self.maps = maps
        self.step_x = step_x
        self.step_y = step_y
        self.tree = 0
        self.x = 0
        self.y = 0

    def slide(self):
        self.x += self.step_x
        self.y += self.step_y

    def check_slope(self):
        width = len(self.maps[0])
        height = len(self.maps)
        for i in range(0, len(self.maps), self.step_y):
            if self.x >= width:
                shift = self.x - width
                self.x = shift
            if self.y >= height:
                break
            elif self.maps[i][self.x] == '#':
                self.tree += 1
                self.slide()
            else:
                self.slide()
        return self.tree

slope1 = Slope(maps, 1, 1)
slope2 = Slope(maps, 3, 1)
slope3 = Slope(maps, 5, 1)
slope4 = Slope(maps, 7, 1)
slope5 = Slope(maps, 1, 2)

tree1 = slope1.check_slope()
tree2 = slope2.check_slope()
tree3 = slope3.check_slope()
tree4 = slope4.check_slope()
tree5 = slope5.check_slope()

print('Part 1: ' + str(tree2))

print('Part 2: ' + str(tree1 * tree2 * tree3 * tree4 * tree5))