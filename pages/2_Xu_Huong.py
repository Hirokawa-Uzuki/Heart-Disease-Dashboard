import streamlit as st
import plotly.express as px
from utils.data_loader import load_and_clean_data, create_sidebar_filter

st.set_page_config(page_title="Xu Hướng", page_icon="📈", layout="wide")
st.title("📈 PAGE 2 - XU HƯỚNG RỦI RO THEO ĐỘ TUỔI")

df_raw = load_and_clean_data()
df = create_sidebar_filter(df_raw)

if df.empty:
    st.warning("Không có dữ liệu phù hợp với bộ lọc.")
else:
    # Gom nhóm theo độ tuổi để tính nhịp tim trung bình và tổng ca mắc bệnh
    df_trend = df.groupby('age').agg(
        So_Ca_Mac_Benh=('target', 'sum'),
        Nhip_Tim_TB=('thalach', 'mean'),
        Huyet_Ap_TB=('trestbps', 'mean')
    ).reset_index()

    st.markdown("### Sự biến thiên của Nhịp tim tối đa và Huyết áp theo Độ tuổi")
    fig_line = px.line(
        df_trend, x='age', y=['Nhip_Tim_TB', 'Huyet_Ap_TB'],
        labels={'age': 'Độ tuổi', 'value': 'Chỉ số', 'variable': 'Loại chỉ số'},
        markers=True
    )
    # Cập nhật tên legend
    newnames = {'Nhip_Tim_TB': 'Nhịp tim tối đa trung bình (bpm)', 'Huyet_Ap_TB': 'Huyết áp trung bình (mmHg)'}
    fig_line.for_each_trace(lambda t: t.update(name = newnames[t.name]))
    st.plotly_chart(fig_line, use_container_width=True)
    
    st.info("💡 **Insight:** Có thể thấy khi độ tuổi tăng lên, huyết áp trung bình có xu hướng tăng đều đặn, trong khi nhịp tim tối đa mà bệnh nhân đạt được lại giảm dần một cách rõ rệt. Đây là dấu hiệu lão hóa tự nhiên của hệ tim mạch.")