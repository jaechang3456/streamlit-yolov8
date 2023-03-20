from ultralytics import YOLO
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = '1'
os.environ['CUDA_MODULE_LOADING'] = 'LAZY'

def detect(file):
    model = YOLO('best.pt')

    model.predict(source=f"./data/{file.name}", save=True) 