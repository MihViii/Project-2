import os
import numpy as np
from flask import Flask, request, jsonify, render_template
from keras.models import load_model
from preprocess import preprocess_image
import tempfile

app = Flask(__name__)

# Đường dẫn đến mô hình
MODEL_PATH = 'models/model.keras'

# Kiểm tra nếu file mô hình tồn tại
if not os.path.isfile(MODEL_PATH):
    raise FileNotFoundError(f"Model file '{MODEL_PATH}' not found!")

# Load mô hình
model = load_model(MODEL_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided.'}), 400

    image_file = request.files['image']

    # Lưu tệp ảnh vào thư mục tạm thời
    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
        image_file.save(temp_file.name)

        # Xử lý ảnh (preprocessing)
        image = preprocess_image(temp_file.name)

    # Thêm chiều batch
    image = np.expand_dims(image, axis=0)

    # Dự đoán
    prediction = model.predict(image)

    # Xử lý kết quả dự đoán
    age_group = predict_age_group(prediction[0])  # Hàm phân nhóm tuổi
    gender = predict_gender(prediction[1])  # Hàm dự đoán giới tính

    # Trả kết quả dưới dạng JSON
    return jsonify({
        'age': age_group,
        'gender': gender
    })


def predict_age_group(age_output):
    # Chuyển đổi đầu ra từ mô hình thành nhóm tuổi
    age_groups = ["0-24", "25-49", "50-74", "75-99", "100-124"]
    return age_groups[np.argmax(age_output)]


def predict_gender(gender_output):
    # Giả sử gender_output là mảng với 2 phần tử (female_prob, male_prob)
    female_prob, male_prob = gender_output[0]  # Lấy giá trị đầu tiên của batch
    return "Female" if male_prob > female_prob else "Male"


if __name__ == '__main__':
    app.run(debug=True)
