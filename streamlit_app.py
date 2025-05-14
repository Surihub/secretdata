import streamlit as st
import pandas as pd
import io

csv_data = st.secrets["data"]["my_csv"]

# 문자열을 DataFrame으로 변환
df = pd.read_csv(io.StringIO(csv_data))

st.title("🔐 secrets.toml에 숨긴 CSV 데이터")
st.dataframe(df)
