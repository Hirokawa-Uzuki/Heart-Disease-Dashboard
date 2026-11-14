import streamlit as st
import plotly.express as px
import pandas as pd
from utils.data_loader import load_and_clean_data, create_sidebar_filter

st.set_page_config(page_title="Tổng Quan", page_icon="📊", layout="wide")
st.title("📊 PAGE 1 - TỔNG QUAN HỒ SƠ BỆNH ÁN")

df_raw = load_and_clean_data()
df = create_sidebar_filter(df_raw)

if df.empty:
    st.warning("Không có dữ liệu phù hợp với bộ lọc.")
else:
    # 1. Các thẻ KPI (Yêu cầu bắt buộc)
    st.markdown("### Chỉ số sức khỏe tổng quát (KPIs)")
    col1, col2, col3, col4 = st.columns(4)
    
    ty_le_benh = (df['target'].sum() / len(df)) * 100
    
    col1.metric("Tổng số hồ sơ", f"{len(df)} bệnh nhân")
    col2.metric("Tỷ lệ mắc bệnh tim", f"{ty_le_benh:.1f}%")
    col3.metric("Huyết áp TB", f"{df['trestbps'].mean():.0f} mmHg")
    col4.metric("Cholesterol TB", f"{df['chol'].mean():.0f} mg/dl")
    
    st.markdown("---")
    
    # 2. Biểu đồ tổng hợp
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.markdown("#### Tỷ lệ mắc bệnh tim trong tập dữ liệu")
        fig_pie = px.pie(
            df, names='target_label', 
            color='target_label',
            color_discrete_map={'Có bệnh tim': 'red', 'Khỏe mạnh': 'green'},
            hole=0.4
        )
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col_chart2:
        st.markdown("#### Phân bố tình trạng bệnh theo Giới tính")
        # Sử dụng groupby để tổng hợp dữ liệu
        df_gender = df.groupby(['sex_label', 'target_label']).size().reset_index(name='Số lượng')
        fig_bar = px.bar(
            df_gender, x='sex_label', y='Số lượng', color='target_label',
            barmode='group',
            color_discrete_map={'Có bệnh tim': 'red', 'Khỏe mạnh': 'green'},
            labels={'sex_label': 'Giới tính'}
        )
        st.plotly_chart(fig_bar, use_container_width=True)