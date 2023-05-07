import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import yolov5

# Load the model
model = yolov5.load('keremberke/yolov5m-license-plate')
  
# Set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 1000  # maximum number of detections per image

# # Create a Tkinter window
# window = tk.Tk()
# window.geometry("800x600")

# Create a label to display the image
# img_label = tk.Label(window)

def predict_image(img_label):
    # Open the file dialog to select an image file
    file_path = filedialog.askopenfilename()
    
    # Load the image using PIL
    img = Image.open(file_path).convert("RGB")
    
    # Resize the image to 640x640
    img = img.resize((640, 640))
    
    # Perform inference on the image
    results = model(img, size=640)
    
    # Parse the results
    predictions = results.pred[0]
    boxes = predictions[:, :4] # x1, y1, x2, y2
    scores = predictions[:, 4]
    categories = predictions[:, 5]
    
    # Draw bounding boxes on the image
    img_draw = img.copy()
    draw = ImageDraw.Draw(img_draw)
    for i, box in enumerate(boxes):
        if scores[i] > model.conf:
            x1, y1, x2, y2 = box
            draw.rectangle([(x1, y1), (x2, y2)], outline="red")
    
    # Display the image with bounding boxes
    img_tk = ImageTk.PhotoImage(img_draw)
    img_label.config(image=img_tk)
    img_label.image = img_tk

# # Create a button to select an image
# select_button = tk.Button(window, text="Select Image", command=predict_image)

# # Pack the widgets into the window
# select_button.pack(side=tk.TOP, padx=10, pady=10)
# img_label.pack(side=tk.TOP, padx=10, pady=10)

# Start the Tkinter event loop
def detect():
    window = tk.Tk()
    window.geometry("800x600")
    img_label = tk.Label(window)
    select_button = tk.Button(window, text="Select Image", command=predict_image(img_label=img_label))

# Pack the widgets into the window
    select_button.pack(side=tk.TOP, padx=10, pady=10)
    img_label.pack(side=tk.TOP, padx=10, pady=10)
    window.mainloop()
