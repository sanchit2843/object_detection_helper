import os
import cv2
import argparse


def plot_image(image, boxes):
    for box in boxes:
        image = cv2.rectangle(
            image, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), thickness=2
        )
        image = cv2.putText(
            image,
            str(box[4]),
            ((box[0] + box[2]) // 2, (box[1] + box[3]) // 2),
            cv2.FONT_HERSHEY_SIMPLEX,
            color=(0, 0, 255),
            thickness=2,
        )
    return image


def split_line_yolo(line):
    line = line.split(" ")
    path = line[0]
    boxes = [[int(y) for y in x.split(",")] for x in line[1:]]
    return path, boxes


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # add more formats based on what is supported by opencv
    parser.add_argument(
        "--yolo_txt_path",
        type=str,
        required=True,
        help="path to yolo txt",
    )

    parser.add_argument(
        "--output_path",
        type=str,
        default="./",
        help="path to save images",
    )

    args = parser.parse_args()

    for i in open(args.yolo_txt_path, "r"):
        path, box = split_line_yolo(i)
        image = cv2.imread(path)
        img = plot_image(image, box)
        cv2.imwrite(
            os.path.join(
                args.output_path,
                i,
            ),
            img,
        )
