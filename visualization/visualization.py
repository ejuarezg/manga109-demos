import manga109api
from PIL import Image, ImageDraw
import argparse

ALL_ANNOTATIONS = ["body", "face", "frame", "text"]

def draw_rectangle(img, x0, y0, x1, y1, annotation_type, line_width):
    assert annotation_type in ALL_ANNOTATIONS
    color = {"body": "#258039", "face": "#f5be41",
             "frame": "#31a9b8", "text": "#cf3721"}[annotation_type]
    draw = ImageDraw.Draw(img)
    draw.rectangle([x0, y0, x1, y1], outline=color, width=line_width)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--manga109_root_dir")
    parser.add_argument("--book", default="ARMS")
    parser.add_argument("--page_index", type=int, default=6)
    parser.add_argument("--annotation_type", default="all")
    parser.add_argument("--line_width", type=int, default=10)
    args = parser.parse_args()

    manga109_root_dir = args.manga109_root_dir
    book = args.book
    page_index = args.page_index
    line_width = args.line_width
    user_annotations = args.annotation_type

    # Check if annotation_type argument is split by comma or space
    if user_annotations == "all":
        user_annotations = ALL_ANNOTATIONS
    else:
        if user_annotations.find(",") != -1:
            user_annotations = user_annotations.replace(" ", "")
            user_annotations = user_annotations.split(",")
        elif user_annotations.find(" ") != -1:
            user_annotations = user_annotations.split(" ")
        else:
            raise Exception(
                "You did not provide a valid seperator for annotation_type: use comma or space"
            )

    p = manga109api.Parser(root_dir=manga109_root_dir)
    annotation = p.get_annotation(book=book)
    img = Image.open(p.img_path(book=book, index=page_index))

    for annotation_type in user_annotations:
        rois = annotation["page"][page_index][annotation_type]
        for roi in rois:
            draw_rectangle(img, roi["@xmin"], roi["@ymin"], roi["@xmax"], roi["@ymax"], annotation_type, line_width)

    img.save("out.jpg")