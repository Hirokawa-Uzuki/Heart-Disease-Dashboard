import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_and_clean_data

st.set_page_config(page_title="Công cụ Chẩn đoán", page_icon="🩺", layout="wide")
st.title("🩺 PAGE 5 - CÔNG CỤ TƯƠNG TÁC & TRA CỨU NHANH")

df = load_and_clean_data()

st.markdown("""
Trang này cung cấp trải nghiệm tương tác mở rộng cho phép người dùng đối chiếu các chỉ số sinh tồn của bản thân 
hoặc bệnh nhân mới vào phổ dữ liệu của 296 ca lâm sàng hiện tại.
""")

with st.expander("ℹ️ Hướng dẫn sử dụng công cụ", expanded=True):
    st.write("Nhập thông tin tuổi và nhịp tim của bạn vào biểu mẫu bên dưới. Hệ thống sẽ định vị vị trí của bạn trên bản đồ rủi ro để so sánh với những bệnh nhân khác.")

col_form, col_chart = st.columns([1, 2])

with col_form:
    st.markdown("### Nhập chỉ số cá nhân")
    my_age = st.number_input("Tuổi của bạn:", min_value=20, max_value=100, value=50, step=1)
    my_thalach = st.number_input("Nhịp tim tối đa khi gắng sức (bpm):", min_value=60, max_value=220, value=150, step=1)
    
with col_chart:
    st.markdown("### Bản đồ định vị rủi ro")
    # Vẽ scatter plot tổng
    fig_scatter = px.scatter(
        df, x='age', y='thalach', color='target_label',
        color_discrete_map={'Có bệnh tim': 'red', 'Khỏe mạnh': 'green'},
        opacity=0.6,
        labels={'age': 'Độ tuổi', 'thalach': 'Nhịp tim tối đa'}
    )
    
    # Thêm điểm của người dùng nhập (Điểm màu vàng lớn)
    fig_scatter.add_scatter(
        x=[my_age], y=[my_thalach], 
        mode='markers', 
        marker=dict(size=20, color='gold', symbol='star', line=dict(width=2, color='black')),
        name='Vị trí của bạn'
    )
    
    st.plotly_chart(fig_scatter, use_container_width=True)