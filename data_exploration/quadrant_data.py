import cv2
import json

'''
def bbox_to_rect(bbox):
    """Convert bounding box to OpenCV format."""
    x, y, w, h = bbox
    return (int(x), int(y)), (int(x + w), int(y + h))
'''

image_name = "train_1.png"
chemin_image = "/media/yousr/B03C63943C6353FE/Users/User/Downloads/training_data/quadrant/xrays/" + image_name
train_json = "/media/yousr/B03C63943C6353FE/Users/User/Downloads/training_data/quadrant/train_quadrant.json"

img = cv2.imread(chemin_image)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

with open(train_json, "r") as fichier_json:
    data = json.load(fichier_json)
'''
for key in data:
    print("key", key)
    test = data[key]
    print (test[0])

# Get the sizes
images_size = len(data.get("images", []))
annotations_size = len(data.get("annotations", []))
categories_size = len(data.get("categories", []))

# Print the sizes
print("Size of 'images' key:", images_size)
print("Size of 'annotations' key:", annotations_size)
print("Size of 'categories' key:", categories_size)
'''

images = data["images"]
image_id = None
for imgs in images:
    if imgs["file_name"] == image_name:
        image_id = imgs["id"]
        break

annotations = data["annotations"]

bounding_boxes = []
labels=[]
for annotation in annotations:
    if annotation["image_id"] == image_id:
        bbox = annotation["bbox"]
        label = "Q : "+ str(annotation["category_id"] +1)
        bounding_boxes.append(bbox)
        labels.append(label)

for bbox, label in zip(bounding_boxes, labels):
    x, y, width, height = bbox
    cv2.rectangle(img, (int(x), int(y)), (int(x + width), int(y + height)), (0, 255, 0), 2)
    cv2.putText(img, label, (int(x), int(y) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

cv2.namedWindow("Image with Bounding Boxes",  cv2.WINDOW_NORMAL)
cv2.imshow("Image with Bounding Boxes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


if __name__ =='__main__':
    pass