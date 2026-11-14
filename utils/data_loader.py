import pandas as pd
import streamlit as st

@st.cache_data
def load_and_clean_data():
    # 1. Đọc dữ liệu
    df = pd.read_csv('data/heart.csv')
    
    # 2. Xử lý dữ liệu (EDA chuẩn): Xóa dòng trùng và dữ liệu lỗi
    df = df.drop_duplicates().reset_index(drop=True)
    df = df[df['thal'] != 0]
    df = df[df['ca'] != 4]
    
    # 3. Ánh xạ (Mapping) sang Tiếng Việt để hiển thị lên Dashboard
    df['sex_label'] = df['sex'].map({1: 'Nam', 0: 'Nữ'})
    df['cp_label'] = df['cp'].map({
        0: 'Đau thắt ngực điển hình', 
        1: 'Đau không điển hình', 
        2: 'Đau không do tim', 
        3: 'Không triệu chứng'
    })
    df['fbs_label'] = df['fbs'].map({1: '> 120 mg/dl', 0: '< 120 mg/dl'})
    df['exang_label'] = df['exang'].map({1: 'Có', 0: 'Không'})
    df['target_label'] = df['target'].map({1: 'Có bệnh tim', 0: 'Khỏe mạnh'})
    
    return df

def create_sidebar_filter(df):
    """Hàm tạo Sidebar dùng chung cho các trang"""
    st.sidebar.header("⚙️ BỘ LỌC DỮ LIỆU")
    
    # Lọc giới tính
    gioi_tinh = st.sidebar.multiselect(
        "1. Chọn giới tính", 
        options=df['sex_label'].unique(), 
        default=df['sex_label'].unique()
    )
    
    # Lọc độ tuổi
    min_age, max_age = int(df['age'].min()), int(df['age'].max())
    tuoi = st.sidebar.slider(
        "2. Chọn khoảng tuổi", 
        min_value=min_age, 
        max_value=max_age, 
        value=(min_age, max_age)
    )
    
    # Áp dụng lọc
    df_filtered = df[
        (df['sex_label'].isin(gioi_tinh)) & 
        (df['age'] >= tuoi[0]) & 
        (df['age'] <= tuoi[1])
    ]
    
    st.sidebar.markdown("---")
    st.sidebar.info(f"Số lượng hồ sơ sau khi lọc: **{len(df_filtered)}** bệnh nhân")
    
    return df_filtered