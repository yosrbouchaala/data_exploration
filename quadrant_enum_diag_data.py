import cv2
import json
import random

image_name = "train_79.png"
chemin_image = "/media/yousr/B03C63943C6353FE/Users/User/Downloads/training_data/quadrant-enumeration-disease/xrays/train_79.png"
train_json = "/media/yousr/B03C63943C6353FE/Users/User/Downloads/training_data/quadrant-enumeration-disease/train_quadrant_enumeration_disease.json"

img = cv2.imread(chemin_image)
print(img)

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
categories3_size = len(data.get("categories_3", []))

# Print the sizes
print("Size of 'images' key:", images_size)
print("Size of 'annotations' key:", annotations_size)
print("Size of 'categories_1' key:", categories1_size)
print("Size of 'categories_2' key:", categories2_size)
print("Size of 'categories_3' key:", categories3_size)
"""
images = data["images"]
image_id = None
for imgs in images:
    if imgs["file_name"] == image_name:
        image_id = imgs["id"]
        break

annotations = data["annotations"]
categories_3 = data["categories_3"]
bounding_boxes = []
labels = []
for annotation in annotations:
    if annotation["image_id"] == image_id:
        bbox = annotation["bbox"]
        label1 = "Q:" + str(annotation["category_id_1"] + 1)
        label2 = "N:" + str(annotation["category_id_2"] + 1)
        D = annotation["category_id_3"]

        for cat in categories_3:
            if cat["id"] == D:
                label3 = "D:" + cat["name"]
                break

        bounding_boxes.append(bbox)
        label = label1 + label2 + label3
        labels.append(label)

thickness = 2
for bbox, label in zip(bounding_boxes, labels):
    x, y, width, height = bbox
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.rectangle(img, (int(x), int(y)), (int(x + width), int(y + height)), color, 2)
    cv2.putText(img, label, (int(x), int(y) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

cv2.namedWindow("Image with Bounding Boxes", cv2.WINDOW_NORMAL)
cv2.imshow("Image with Bounding Boxes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
