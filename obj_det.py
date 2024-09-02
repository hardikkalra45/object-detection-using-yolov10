from ultralytics import YOLO

model = YOLO("yolov10x.pt")

results = model("C:/Users/hardi/Downloads/person-bicycle-car-detection.mp4", save=True)

results[0].show()
