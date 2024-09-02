from ultralytics import YOLO

model = YOLO("yolov10x.pt")

results = model("C:/Users/hardi/Downloads/dog_bike_car.jpg", save=True)

results[0].show()
