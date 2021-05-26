def split_line_yolo(line):
    line = line.split(" ")
    path = line[0]
    boxes = [[int(y) for y in x.split(",")] for x in line[1:]]
    return path, boxes
