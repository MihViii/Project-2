# Project-2

**Project-2** là một ứng dụng nhận diện ảnh sử dụng mô hình học sâu để phân tích độ tuổi và giới tính từ ảnh người. Dự án này sử dụng Flask làm backend và Keras để tải và sử dụng mô hình học sâu.

## Mục lục
- [Giới thiệu](#giới-thiệu)
- [Yêu cầu](#yêu-cầu)
- [Cài đặt](#cài-đặt)
- [Cách sử dụng](#cách-sử-dụng)
- [Mô hình](#mô-hình)

## Giới thiệu
Dự án này là một ứng dụng web sử dụng Flask để nhận diện ảnh và dự đoán độ tuổi và giới tính của người trong ảnh. Mô hình học sâu được sử dụng trong dự án này đã được huấn luyện trước và có thể phân loại người trong ảnh thành các nhóm độ tuổi và giới tính.

## Yêu cầu
- Python 3.x
- Flask
- Keras
- TensorFlow
- Git
- Một số thư viện Python khác (xem `requirements.txt`)

## Cài đặt
Để chạy ứng dụng, bạn cần phải cài đặt các yêu cầu phần mềm và thư viện:

1. **Clone dự án từ GitHub**:
    ```bash
    git clone https://github.com/MihViii/Project-2.git
    cd Project-2
    ```

2. **Cài đặt các thư viện cần thiết**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Chạy ứng dụng**:
    ```bash
    python app.py
    ```
    Sau khi chạy, ứng dụng sẽ hoạt động trên `http://127.0.0.1:5000/`.

## Cách sử dụng
1. Truy cập trang web `http://127.0.0.1:5000/` trong trình duyệt.
2. Tải lên một bức ảnh của người và nhấn "Upload and Predict".
3. Dự đoán độ tuổi và giới tính của người trong ảnh sẽ được hiển thị.

## Mô hình
Mô hình học sâu được huấn luyện sử dụng **Keras** và **TensorFlow**. Mô hình nhận dạng ảnh được lưu trữ dưới dạng tệp `.keras`.


