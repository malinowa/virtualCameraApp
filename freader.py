from structures import Point, Line

class FileReader():
    def __init__(self, fileName):
        self.lines = self.load_from_file(fileName)

    def load_from_file(self, fileName):
        lines = []
        with open(fileName, "r") as file:
            counter = 0
            id = 0
            for line in file.readlines():
                if counter == 12:
                    id += 1
                    counter = 0
                coords = line.strip().split(' ')
                a = Point(int(coords[0]), int(coords[1]), int(coords[2]))
                b = Point(int(coords[3]), int(coords[4]), int(coords[5]))
                lines.append(Line(a, b, id))
                counter += 1
        
        return lines

    def getLines(self):
        return self.lines
