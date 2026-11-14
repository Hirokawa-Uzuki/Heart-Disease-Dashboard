# 🫀 Dashboard Trực Quan Hóa Dữ Liệu Bệnh Tim (Heart Disease Dataset)

Đây là mã nguồn hệ thống Dashboard trực quan hóa và phân tích dữ liệu bệnh tim mạch, thuộc Bài tập lớn môn **Trực quan và Phân tích Dữ liệu**. Ứng dụng được xây dựng bằng Python và Streamlit, đóng vai trò như một hệ thống Hỗ trợ quyết định lâm sàng (CDSS) giúp khám phá dữ liệu y khoa, phân tích tương quan các chỉ số sinh tồn và định vị rủi ro tim mạch theo thời gian thực.

## 👥 Thông Tin Thực Hiện (Nhóm 6)

* **Đơn vị:** Khoa Công nghệ thông tin - Trường Đại học Đại Nam
* **Môn học:** Trực quan và Phân tích Dữ liệu
* **Giảng viên hướng dẫn:** Thầy Trần Hải Anh

| STT | Mã Sinh Viên | Họ và Tên | Ngày Sinh |
| :---: | :---: | :--- | :---: |
| 1 | 1871040027 | **Nguyễn Ngọc Quyết** | 
| 2 | 1871040010 | **Phạm Đăng Quốc Dũng** | 
| 3 | 1871040038 | **Phạm Anh Tuấn** | 
| 4 | 1871040011 | **Nguyễn Huy Dương** | 

## 🚀 Công Nghệ Sử Dụng

* **Ngôn ngữ lập trình:** Python 3.14+
* **Framework Web Dashboard:** Streamlit (kết hợp `@st.cache_data` và tùy biến giao diện CSS)
* **Thư viện Trực quan hóa:** Plotly Express, Matplotlib, Seaborn
* **Thư viện Xử lý & Phân tích dữ liệu:** Pandas, NumPy

## 📊 Quy Trình Làm Sạch Dữ Liệu (EDA)

Bộ dữ liệu gốc **Heart Disease Dataset** (từ Kaggle / UCI Machine Learning Repository) gồm **1.025 bản ghi** và **14 thuộc tính lâm sàng** đã được xử lý nghiêm ngặt qua 3 bước:
1. **Kiểm tra khuyết thiếu bề mặt (`Null/NaN`):** Rà soát toàn bộ 14 thuộc tính.
2. **Loại bỏ nhiễu nhân bản (`Duplicated rows`):** Cắt bỏ **723 bản ghi trùng lặp**, đưa dữ liệu về **302 hồ sơ duy nhất**.
3. **Xử lý mã lỗi ẩn (`Hidden Missing Values`):** Lọc bỏ **6 bản ghi sai lệch nghiệp vụ y khoa** (`ca = 4` và `thal = 0`), chốt lại tập dữ liệu chuẩn gồm **296 bệnh nhân** để đưa vào phân tích và trực quan hóa.

## 🖥️ Các Phân Hệ Chức Năng Trên Dashboard

* **Global Sidebar Filter:** Bộ lọc toàn cục theo Giới tính và khoảng Độ tuổi (29 - 77 tuổi) đồng bộ hóa dữ liệu tức thời trên mọi trang.
* **Page 1 - Tổng quan hồ sơ bệnh án (`1_Tong_Quan.py`):** Hiển thị 4 thẻ chỉ số sức khỏe cốt lõi (KPIs), biểu đồ Donut tỷ lệ mắc bệnh và biểu đồ cột nhóm phân bố bệnh lý theo giới tính.
* **Page 2 - Xu hướng rủi ro theo độ tuổi (`2_Xu_Huong.py`):** Biểu đồ đường kép (Dual-Line Chart) mô phỏng quy luật nghịch đảo giữa sự gia tăng Huyết áp lúc nghỉ (`trestbps`) và sự suy giảm Nhịp tim tối đa (`thalach`) theo tiến trình lão hóa.
* **Page 3 - Phân tích triệu chứng lâm sàng (`3_Phan_Tich_Trieu_Chung.py`):** Phân tích chuyên sâu 4 loại Đau thắt ngực (`cp`) và chứng Đau ngực khi gắng sức (`exang`) qua biểu đồ cột chồng và cột cụm.
* **Page 4 - Phân phối chỉ số sinh tồn & Xếp hạng Top N (`4_Chi_So_Sinh_Ton.py`):** Tích hợp 3 không gian chức năng gồm Phân phối (Boxplot & Histogram), Bảng chéo (Pivot Table) và Xếp hạng Top N bệnh nhân có mức Cholesterol cao nhất.
* **Page 5 - Công cụ tương tác & Tra cứu nhanh (`5_Tra_Cuu_Tuong_Tac.py`):** Cho phép nhập chỉ số cá nhân (Tuổi, Nhịp tim tối đa) và định vị trực tiếp bằng điểm đánh dấu "Ngôi sao vàng" trên biểu đồ phân tán (Scatter Plot) của 296 ca bệnh lịch sử.

## 📂 Cấu Trúc Thư Mục Dự Án

```text
Heart-Disease-Dashboard/
├── .streamlit/
│   └── config.toml                  # Cấu hình giao diện Medical Theme
├── data/
│   └── heart.csv                    # Tập dữ liệu gốc (1.025 bản ghi)
├── pages/
│   ├── 1_Tong_Quan.py               # Page 1: Tổng quan hồ sơ bệnh án
│   ├── 2_Xu_Huong.py                # Page 2: Xu hướng rủi ro theo độ tuổi
│   ├── 3_Phan_Tich_Trieu_Chung.py   # Page 3: Phân tích triệu chứng lâm sàng
│   ├── 4_Chi_So_Sinh_Ton.py         # Page 4: Phân phối chỉ số sinh tồn & Top N
│   └── 5_Tra_Cuu_Tuong_Tac.py       # Page 5: Công cụ tra cứu & Định vị rủi ro
├── utils/
│   └── data_loader.py               # Module đọc, làm sạch dữ liệu & Caching
├── EDA_Heart_Disease.ipynb          # Jupyter Notebook phân tích khám phá (EDA)
├── app.py                           # File điều hướng trung tâm của ứng dụng
├── requirements.txt                 # Danh sách các thư viện Python phụ thuộc
└── README.md                        # Tài liệu hướng dẫn sử dụng dự án
```

## ⚙️ Hướng Dẫn Cài Đặt Và Khởi Chạy

**Bước 1: Clone kho lưu trữ về máy tính**
```bash
git clone [https://github.com/Hirokawa-Uzuki/Heart-Disease-Dashboard.git](https://github.com/Hirokawa-Uzuki/Heart-Disease-Dashboard.git)
cd Heart-Disease-Dashboard
```

**Bước 2: Tạo và kích hoạt môi trường ảo (Khuyến nghị)**
```bash
python -m venv venv
# Đối với Windows:
venv\Scripts\activate
# Đối với macOS/Linux:
source venv/bin/activate
```

**Bước 3: Cài đặt các thư viện cần thiết**
```bash
pip install -r requirements.txt
```

**Bước 4: Khởi chạy ứng dụng Streamlit**
```bash
streamlit run app.py
```
*Sau khi chạy lệnh, trình duyệt sẽ tự động mở hệ thống Dashboard tại địa chỉ: `http://localhost:8501`*
