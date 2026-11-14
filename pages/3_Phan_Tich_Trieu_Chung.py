import streamlit as st
import plotly.express as px
from utils.data_loader import load_and_clean_data, create_sidebar_filter

st.set_page_config(page_title="Triệu Chứng", page_icon="🫁", layout="wide")
st.title("🫁 PAGE 3 - PHÂN TÍCH TRIỆU CHỨNG LÂM SÀNG")

df_raw = load_and_clean_data()
df = create_sidebar_filter(df_raw)

if df.empty:
    st.warning("Không có dữ liệu phù hợp với bộ lọc.")
else:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Tác động của Đau thắt ngực (CP)")
        df_cp = df.groupby(['cp_label', 'target_label']).size().reset_index(name='Số lượng')
        fig_cp = px.bar(
            df_cp, x='cp_label', y='Số lượng', color='target_label',
            color_discrete_map={'Có bệnh tim': 'red', 'Khỏe mạnh': 'green'},
            barmode='stack', labels={'cp_label': 'Loại đau ngực'}
        )
        st.plotly_chart(fig_cp, use_container_width=True)
        
    with col2:
        st.markdown("### Đau ngực khi gắng sức (Exang)")
        df_ex = df.groupby(['exang_label', 'target_label']).size().reset_index(name='Số lượng')
        fig_ex = px.bar(
            df_ex, x='exang_label', y='Số lượng', color='target_label',
            color_discrete_map={'Có bệnh tim': 'red', 'Khỏe mạnh': 'green'},
            barmode='group', labels={'exang_label': 'Có bị đau khi tập thể dục không?'}
        )
        st.plotly_chart(fig_ex, use_container_width=True)