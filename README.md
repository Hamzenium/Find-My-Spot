
# Find My Spot - Car Parking Detection and Camera Stream Integration

![IMG_4303](https://github.com/user-attachments/assets/e202e0bd-9922-433c-9ec0-c4fa716dc6d8)

<img width="330" alt="Screenshot 2025-01-22 at 5 49 47 PM" src="https://github.com/user-attachments/assets/af9ac53f-d8d1-40c1-8ce2-2f87ba91d0dc" />



## Overview
**Find My Spot** is a computer vision and IoT-based application designed to help users locate the nearest parking space.  This project was developed as an MVP during a hackathon, where our team leveraged advanced computer vision technology and IoT solutions to create an innovative system.
We are proud to share a photo of our application in action at York University. Using computer vision technology, our app analyzed vacant parking lots and informed users of available parking spots in real-time. Despite numerous challenges faced during the development process, we are thrilled with the outcome and its potential to improve people's lives.


---

## Key Functionalities
1. **ESP32 Camera Stream with Face Detection and Recognition**
   - Uses the ESP32 microcontroller to create a web server for streaming video and performing face recognition.
2. **YOLOv5-based License Plate Detection**
   - Leverages the YOLOv5 object detection model to identify and locate license plates in images.
3. **Real-Time Parking Space Analysis**
   - Integrates computer vision to analyze parking lot availability and provide real-time updates to users.
4. **Garage Parking Sharing**
   - Allows users to view and share garage parking spaces through the application.

---

## Features
### ESP32 Camera Stream
- Streams video over a web interface using the ESP32 microcontroller.
- Supports face detection and recognition with enrollment and identification capabilities.
- Provides an HTTP API for image capture, configuration, and status retrieval.

### YOLOv5 License Plate Detection
- Uses the pre-trained YOLOv5 model for detecting license plates in images.
- Visualizes detected bounding boxes directly on the provided image.
- Supports GUI-based image selection and result display using Tkinter and PIL (Python Imaging Library).

---

## Directory Structure

```
.vscode/                      # Configuration files for VSCode
CameraWebServer/              # ESP32 Camera Web Server code
  CameraWebServer.ino         # Main ESP32 sketch
  app_httpd.cpp               # HTTP server functionality
  camera_index.h              # HTML index page for the web server
  camera_pins.h               # Pin definitions for the ESP32 camera
__pycache__/                  # Compiled Python files
  *.pyc                       # Cached Python modules

detr-resnet-50-License_Plate_Object_Detection/
  # Directory for DETR-based license plate object detection (future support)

templates/                    # HTML templates for Flask server
  detect.html                 # Detection results page
  index.html                  # Main index page for the Flask app

yolov5/                       # YOLOv5-related code and resources
  app.py                      # Main Flask app for YOLOv5
  car_cv.py                   # Car-specific YOLOv5 detection script
  cv.py                       # General YOLOv5 computer vision script

yolov5s.pt                    # Pre-trained YOLOv5s model
```

---

## Requirements
### ESP32 Camera
- ESP32 microcontroller with camera module.
- Arduino IDE or equivalent environment for flashing the ESP32.

### YOLOv5 Detection
- Python 3.8+
- Required Python libraries:
  - `opencv-python`
  - `torch`
  - `yolov5` (Pre-trained YOLOv5 model)
  - `Pillow`
  - `tkinter` (GUI interface for image selection)

---

## Setup

### ESP32 Camera Server
1. Install the **ESP32 Add-on** in the Arduino IDE.
2. Flash the provided ESP32 code to your ESP32 board.
3. Access the ESP32 Camera server via the local IP address assigned by your Wi-Fi network.

### YOLOv5 License Plate Detection
1. Clone the YOLOv5 repository:
   ```bash
   git clone https://github.com/ultralytics/yolov5.git
   ```
2. Install dependencies:
   ```bash
   pip install -r yolov5/requirements.txt
   ```
3. Download the pre-trained YOLOv5 model (`yolov5s.pt`).
4. Run the Python script for license plate detection:
   ```bash
   python yolov5/server.py
   ```
5. Access the Flask server at `http://127.0.0.1:5000`.
6. Use the provided HTML templates (`templates/detect.html`) to upload and process images.

---

## Usage

### Face Detection and Recognition (ESP32)
1. Open the stream endpoint in your browser to start streaming.
2. Use the `/control` endpoint to enable or disable face detection and recognition.
3. Enroll new faces using the `/control?var=face_enroll&val=1` endpoint.
4. View live recognition results in the stream.

### License Plate Detection (YOLOv5)
1. Run the `server.py` script in the `yolov5` folder.
2. Open the browser and navigate to `http://127.0.0.1:5000`.
3. Upload an image containing license plates.
4. The results with bounding boxes will be displayed on the webpage.

---

## Example Outputs

### ESP32 Camera Stream
- **Face Detected**: Draws bounding boxes with labels for detected faces.
- **Recognition Results**: Displays recognized face IDs.

### YOLOv5 License Plate Detection
- **Bounding Boxes**: Highlights detected license plates in red.
- **Confidence Scores**: Filters detections based on the configured confidence threshold.

---

## Future Improvements
- **ESP32**:
  - Add support for recording video streams.
  - Optimize face recognition accuracy and performance.
- **YOLOv5**:
  - Integrate real-time video feed for license plate detection.
  - Enhance GUI for batch processing of images.
  - Integrate map functionality to guide users to parking spaces.

