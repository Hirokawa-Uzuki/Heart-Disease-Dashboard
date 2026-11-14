import streamlit as st
import plotly.express as px
import pandas as pd
from utils.data_loader import load_and_clean_data, create_sidebar_filter

st.set_page_config(page_title="Chỉ Số Sinh Tồn", page_icon="🩸", layout="wide")
st.title("🩸 PAGE 4 - PHÂN TÍCH PHÂN PHỐI CHỈ SỐ SINH TỒN")

df_raw = load_and_clean_data()
df = create_sidebar_filter(df_raw)

if df.empty:
    st.warning("Không có dữ liệu phù hợp với bộ lọc.")
else:
    tab1, tab2, tab3 = st.tabs(["📊 Phân phối", "🧮 Pivot Table", "🚨 Top N Bệnh Nhân Rủi Ro"])
    
    with tab1:
        st.markdown("### Phân bố Huyết áp (Trestbps) và Cholesterol giữa các nhóm")
        col1, col2 = st.columns(2)
        with col1:
            fig_box = px.box(df, x='target_label', y='trestbps', color='target_label', 
                             color_discrete_map={'Có bệnh tim': 'red', 'Khỏe mạnh': 'green'})
            st.plotly_chart(fig_box, use_container_width=True)
        with col2:
            fig_hist = px.histogram(df, x='chol', color='target_label', barmode='overlay',
                                    color_discrete_map={'Có bệnh tim': 'red', 'Khỏe mạnh': 'green'})
            st.plotly_chart(fig_hist, use_container_width=True)
            
    with tab2:
        st.markdown("### Pivot Table: Tỷ lệ mắc bệnh theo Giới tính và Loại đau ngực")
        # Áp dụng Pivot table chuẩn yêu cầu
        pivot_df = pd.pivot_table(
            df, 
            values='target', 
            index='cp_label', 
            columns='sex_label', 
            aggfunc='mean'
        )
        # Format thành %
        st.dataframe(pivot_df.style.format("{:.1%}"), use_container_width=True)

    with tab3:
        st.markdown("### Top N bệnh nhân có chỉ số Cholesterol cao nhất (Nguy cơ cao)")
        top_n = st.slider("Chọn số lượng Top N:", min_value=5, max_value=20, value=10, step=1)
        
        # Lọc những người có bệnh tim và sắp xếp theo Cholesterol giảm dần
        df_top = df[df['target'] == 1].nlargest(top_n, 'chol')
        
        # Đánh mã bệnh nhân ảo (vì dữ liệu gốc không có ID)
        df_top['Patient_ID'] = ['Bệnh nhân ' + str(i) for i in df_top.index]
        
        fig_top = px.bar(
            df_top, x='chol', y='Patient_ID', orientation='h',
            labels={'chol': 'Cholesterol (mg/dl)', 'Patient_ID': 'Mã hồ sơ'},
            color='trestbps', color_continuous_scale='Reds',
            title=f'Top {top_n} ca mắc bệnh tim có nồng độ Cholesterol cao nhất'
        )
        fig_top.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_top, use_container_width=True)