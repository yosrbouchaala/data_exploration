import cv2
import json
import random
import numpy as np


image_name = "train_79.png"
chemin_image = "/media/yousr/B03C63943C6353FE/Users/User/Downloads/training_data/quadrant_enumeration/xrays/"+image_name
train_json = "/media/yousr/B03C63943C6353FE/Users/User/Downloads/training_data/quadrant_enumeration/train_quadrant_enumeration.json"

img = cv2.imread(chemin_image)


with open(train_json, "r") as fichier_json:
    data = json.load(fichier_json)

    """"
for key in data:
    print("key", key)
    test = data[key]
    print(test[0])

# Get the sizes
images_size = len(data.get("images", []))
annotations_size = len(data.get("annotations", []))
categories1_size = len(data.get("categories_1", []))
categories2_size = len(data.get("categories_2", []))

# Print the sizes
print("Size of 'images' key:", images_size)
print("Size of 'annotations' key:", annotations_size)
print("Size of 'categories_1' key:", categories1_size)
print("Size of 'categories_2' key:", categories2_size)
"""

images = data["images"]
image_id = None
for imgs in images:
    if imgs["file_name"] == image_name:
        image_id = imgs["id"]
        break

annotations = data["annotations"]
masks = []
labels = []
for annotation in annotations:
    if annotation["image_id"] == image_id:
        segmentation = annotation["segmentation"]
        label1 = "Q:" + str(annotation["category_id_1"] + 1)
        label2 = "N:" + str(annotation["category_id_2"] + 1)
        masks.append(segmentation)
        label = label1 + label2
        labels.append(label)

for mask, label in zip(masks, labels):
    # Conversion des coordonnées en tableau numpy

    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    points = np.array(mask, dtype=np.int32)
    points = points.reshape((-1, 2))

    # Dessiner le masque de segmentation
    cv2.fillPoly(img, [points], color)



cv2.namedWindow("Image with masks",  cv2.WINDOW_NORMAL)
cv2.imshow("Image with masks", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
