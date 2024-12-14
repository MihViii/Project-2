import cv2
import numpy as np

def preprocess_image(file_path):
    # Đọc ảnh từ file
    image = cv2.imread(file_path)
    if image is None:
        raise ValueError("Failed to load image.")

    # Resize ảnh về kích thước 198x198
    image = cv2.resize(image, (198, 198))  # Đổi kích thước theo yêu cầu của mô hình
    image = image.astype('float32') / 255.0  # Chuẩn hóa ảnh về [0, 1]

    # Trả về ảnh với shape (198, 198, 3)
    return image
