import os
import argparse
from utils.util import split_line_yolo
from collections import Counter

# give class wise box count
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--yolo_txt_path",
        type=str,
        required=True,
        help="path to yolo txt",
    )

    args = parser.parse_args()
    class_id_list = []

    class_id_decoder = {0: "car", 1: "truck", 2: "bus", 3: "heavy truck"}

    for i in open(args.yolo_txt_path, "r"):
        path, box = split_line_yolo(i)
        for b in box:
            class_id_list.append(class_id_decoder[b[4]])
    c = Counter(class_id_list)

    print(c)