import pathlib
import pickle
from pprint import pprint

import manga109api
import numpy as np

# Instantiate a parser with the root directory of Manga109. This can be a relative or absolute path.
manga109_root_dir = "Manga109_released_2021_02_28"
p = manga109api.Parser(root_dir=manga109_root_dir)

formatted_data: dict = {}

# Remove this many parts when saving path to image
manga109_path = pathlib.Path(manga109_root_dir)
parts_to_trim = len(manga109_path.parts)

for kb, bo in enumerate(p.books):
    print(f"Book {kb}: {bo}")
    annotation = p.get_annotation(book=bo)
    page_annotations = annotation["page"]

    num_pages = len(page_annotations)

    for i, pa in enumerate(page_annotations):
        text_annotation = pa["text"]
        # Continue to the next page if no bounding boxes for text are found
        if not text_annotation:
            continue

        # Zero out height and width by subtracting one pixel
        height_normalizer = pa["@height"] - 1
        width_normalizer = pa["@width"] - 1

        num_boxes = len(text_annotation)

        # Store bouding box coordinates and class of object. All objects have the same class.
        object_description = np.zeros((num_boxes, 24))
        object_description[:, 4] = 1

        for j, ta in enumerate(text_annotation):
            object_description[j, :4] = [
                (ta["@xmin"] - 1) / width_normalizer,
                (ta["@ymin"] - 1) / height_normalizer,
                (ta["@xmax"] - 1) / width_normalizer,
                (ta["@ymax"] - 1) / height_normalizer,
            ]

        full_path = pathlib.Path(p.img_path(book=bo, index=i))
        relative_path = pathlib.Path(*full_path.parts[parts_to_trim:])
        formatted_data.update({str(relative_path): object_description})


with open(
    "Manga109.pkl",
    "wb",
) as handle:
    pickle.dump(formatted_data, handle, protocol=pickle.HIGHEST_PROTOCOL)
