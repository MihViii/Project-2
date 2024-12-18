# Bộ phân loại Tuổi và Giới tính

Dự án này là một ứng dụng web dùng để dự đoán nhóm tuổi và giới tính của một người dựa trên hình ảnh khuôn mặt. Ứng dụng sử dụng mô hình học sâu được triển khai bằng Keras và tích hợp Flask làm backend để xử lý dự đoán. Giao diện frontend cho phép người dùng tải lên hoặc chụp ảnh để xử lý.

## Tính năng

- Tải lên hình ảnh hoặc sử dụng camera của thiết bị để chụp ảnh.
- Cắt ảnh để dự đoán chính xác hơn.
- Dự đoán nhóm tuổi và giới tính bằng mô hình đã được huấn luyện.

## Cấu trúc dự án

```
.
├── app.py                  # Backend Flask
├── models/
│   └── model.keras         # Mô hình Keras đã huấn luyện
├── preprocess.py           # Script xử lý ảnh
├── static/
│   └── (tệp CSS/JS tùy chọn)
├── templates/
│   └── index.html          # Giao diện frontend
└── README.md               # Tài liệu dự án
```

## Yêu cầu cài đặt

Đảm bảo rằng bạn đã cài đặt các phần mềm sau:

- Python 3.7+
- Flask
- Keras
- TensorFlow
- NumPy

Bạn có thể cài đặt các gói Python cần thiết bằng lệnh sau:

```bash
pip install -r requirements.txt
```

> Lưu ý: Đảm bảo rằng tệp `models/model.keras` tồn tại trong thư mục đúng. Nếu không, hãy huấn luyện hoặc tải mô hình đã được huấn luyện trước.

## Cách chạy ứng dụng

1. **Clone kho lưu trữ**:

   ```bash
   git clone https://github.com/MihViii/Project-2.git
   cd Project-2
   ```

2. **Cài đặt các thư viện phụ thuộc**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Chạy ứng dụng Flask**:

   ```bash
   python app.py
   ```

4. **Truy cập ứng dụng**:

   Mở trình duyệt và truy cập `http://127.0.0.1:5000`.

## Mô tả các tệp

### `app.py`

Tệp này chứa logic backend chính:

- Load mô hình Keras đã huấn luyện.
- Cung cấp giao diện web thông qua Flask.
- Xử lý tải lên hình ảnh, xử lý và dự đoán.

### `index.html`

Giao diện frontend cho phép người dùng:

- Tải lên hình ảnh hoặc chụp ảnh bằng camera.
- Cắt ảnh trước khi dự đoán.
- Xem kết quả dự đoán.

### `preprocess.py`

Tệp này chứa logic xử lý hình ảnh trước khi đưa vào mô hình. Các bước phổ biến bao gồm thay đổi kích thước, chuẩn hóa và đảm bảo đúng định dạng đầu vào.

### `model.keras`

Mô hình Keras đã được huấn luyện, có khả năng dự đoán nhóm tuổi và giới tính dựa trên hình ảnh khuôn mặt. Mô hình sử dụng Mạng Nơ-ron Tích chập (CNN) để trích xuất đặc trưng và phân loại.

## API Endpoints

### `/`

- **Phương thức**: `GET`
- **Mô tả**: Hiển thị giao diện web chính.

### `/predict`

- **Phương thức**: `POST`
- **Mô tả**: Nhận một tệp ảnh, xử lý và trả về dự đoán nhóm tuổi và giới tính.
- **Đầu vào**: Tệp hình ảnh (key `form-data`: `image`).
- **Đầu ra**:

  ```json
  {
      "age": "25-49",
      "gender": "Male"
  }
  ```

## Logic dự đoán

- **Nhóm tuổi**: Mô hình dự đoán một trong năm nhóm tuổi: `0-24`, `25-49`, `50-74`, `75-99`, `100-124`.
- **Giới tính**: Mô hình dự đoán giới tính là `Male` hoặc `Female`.

## Cải tiến trong tương lai

- Bổ sung các kỹ thuật tiền xử lý ảnh mạnh mẽ hơn.
- Sử dụng tập dữ liệu lớn hơn để mô hình tổng quát tốt hơn.
- Tối ưu hóa để dự đoán theo thời gian thực với hỗ trợ GPU nâng cao.
- Thêm tính năng dự đoán sắc tộc.


