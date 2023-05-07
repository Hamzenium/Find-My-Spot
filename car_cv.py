import cv2
import tkinter as tk
from tkinter import filedialog
import yolov5

# Load the YOLOv5s model
model = yolov5.load('yolov5s.pt')

# set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 1000  # maximum number of detections per image

# Define a function for detecting objects in an image
def detect_objects(img_path):
    # Load the image
    img = cv2.imread(img_path)

    # perform inference
    results = model(img, size=640)            

    # parse results
    predictions = results.pred[0]
    boxes = predictions[:, :4] # x1, y1, x2, y2
    scores = predictions[:, 4]
    categories = predictions[:, 5]

    # Draw boxes around the detected objects
    for box in boxes:
        x1, y1, x2, y2 = box
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Count the number of objects detected
    num = len(boxes)

    return img, num

# Define a function for selecting an image file
def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

# Define a function for displaying the detected image in a window
def show_image(img, title):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# # Select an image file
# file_path = select_file()

# # Detect objects in the image
# detected_img, num_cars = detect_objects(file_path)

# # Show the detected image in a window
# title = f'Detected Image ({num_cars} cars)'
# show_image(detected_img, title)


def detect_objects_flask():
    file_path = select_file()
    detected_img, num_cars = detect_objects(file_path)
    title = f'Detected Image ({num_cars} cars)'
    show_image(detected_img, title)

detect_objects_flask()