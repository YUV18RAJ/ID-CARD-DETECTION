##This code trains a custom dataset yolo model ,dataset path is in the config.yaml file

from ultralytics import YOLO
import multiprocessing

def main():
# Load a model
    model = YOLO("yolov8n.yaml")  # build a new model from scratch

    # Use the model
    results = model.train(data=r"C:\Users\Aarya\.vscode\Wipro\data - Copy\config1.yaml", epochs=100)  # train the model

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()