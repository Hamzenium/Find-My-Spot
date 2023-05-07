# import requests
# import cv2
# import yolov5
# import numpy as np
# # load model
# model = yolov5.load('keremberke/yolov5m-license-plate')
  
# # set model parameters
# model.conf = 0.25  # NMS confidence threshold
# model.iou = 0.45  # NMS IoU threshold
# model.agnostic = False  # NMS class-agnostic
# model.multi_label = False  # NMS multiple labels per box
# model.max_det = 1000  # maximum number of detections per image

# # set up video capture from IP camera
# video_stream_url = 'http://192.168.5.213/stream'
# response = requests.get(video_stream_url, stream=True)
# if response.status_code == 200:
#     bytes = bytes()
#     for chunk in response.iter_content(chunk_size=1024):
#         bytes += chunk
#         a = bytes.find(b'\xff\xd8')
#         b = bytes.find(b'\xff\xd9')
#         if a != -1 and b != -1:
#             jpg = bytes[a:b+2]
#             bytes = bytes[b+2:]
#             # decode the frame
#             frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            
#             # perform inference on the frame
#             results = model(frame, size=640)
    
#             # parse results
#             predictions = results.pred[0]
#             boxes = predictions[:, :4] # x1, y1, x2, y2
#             scores = predictions[:, 4]
#             categories = predictions[:, 5]

#             # draw boxes on the frame
#             for box in boxes:
#                 x1, y1, x2, y2 = [int(coord) for coord in box]
#                 cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

#             # show the output frame
#             cv2.imshow('License Plate Detection', frame)

#             # wait for key press to exit
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
# else:
#     print("Unable to access video stream")
    
# # release resources
# cv2.destroyAllWindows()
