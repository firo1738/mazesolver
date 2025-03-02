from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.win = win
        self.visited = False

    def Draw(self, x1, y1, x2, y2):
        if self.win is None:
            return
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(line, 'white')
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(line, 'white')
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(line, 'white')
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(line, 'white')

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self.x2-self.x1)//2
        self.line_x1 = half_length+self.x1
        self.line_y1 = half_length+self.y1
        half_length2 = abs(to_cell.x2-to_cell.x1)//2
        self.line_x2 = half_length2+to_cell.x1
        self.line_y2 = half_length2+to_cell.y1
        line = Line(Point(self.line_x1, self.line_y1), Point(self.line_x2, self.line_x2))
        if not undo:
            self.win.draw_line(line, 'red')
        else:
            self.win.draw_line(line, 'gray')
