from graphics import Window, Point, Line


def main():
    win = Window(800, 600)
    p1 = Point(100, 150)
    p2 = Point(200, 250)
    line1 = Line(p1, p2)
    win.draw_line(line1, "red")
    win.wait_for_close()


main()
