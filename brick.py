import math
from cadquery import func as cf

def clutch_brick(rows, cols, height=9.6, stud_d=4.8, stud_h=1.7, pitch=8.0, gap=0.2):
    length = cols * pitch - gap
    width = rows * pitch - gap
    body = cf.box(length, width, height)
    stud = cf.cylinder(d=stud_d, h=stud_h)

    for i in range(cols):
        for j in range(rows):
            x = (i - (cols - 1) / 2) * pitch
            y = (j - (rows - 1) / 2) * pitch
            body += stud.moved(x=x, y=y, z=height)
    return body, length, width

rows, cols = 2, 4
height, stud_d, stud_h = 9.6, 4.8, 1.7

brick, length, width = clutch_brick(rows, cols, height, stud_d, stud_h)

expected = (length * width * height
            + rows * cols * math.pi * (stud_d / 2) ** 2 * stud_h)
assert abs(brick.Volume() - expected) < 0.5

brick.exportStl("brick.stl")

brick.exportStl("brick.stl")
