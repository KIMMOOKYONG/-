```python
%%writefile app.py
# importing required libraries
import pandas as pd
import numpy as np

import requests
import urllib.request
from bs4 import BeautifulSoup
import json

import streamlit as st
from streamlit_option_menu import option_menu

from streamlit_folium import folium_static
import folium

# 전체 페이지 사용하도록 설정
st.set_page_config(layout="wide")

# adding a selectbox
st.image("https://gscaltexmediahub.com/wp-content/uploads/2021/05/img.jpeg", width=200)
# 가로 레이아웃 구현
c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(8)
m1, m2 = st.columns(2)

var1 = c1.selectbox(
    "시도",
    ("Pen","Pencil","Eraser","Sharpener","Notebook"))

var2 = c2.selectbox(
    "시군구",
    ("Pen","Pencil","Eraser","Sharpener","Notebook"))

var3 = c3.selectbox(
    "주유소 브랜드",
    ("Pen","Pencil","Eraser","Sharpener","Notebook"))

var4 = c4.selectbox(
    "셀프 주유소 여부",
    ("Pen","Pencil","Eraser","Sharpener","Notebook"))

var5 = c5.selectbox(
    "편의점 유뮤",
    ("Pen","Pencil","Eraser","Sharpener","Notebook"))

var6 = c6.selectbox(
    "세차장 여부",
    ("Pen","Pencil","Eraser","Sharpener","Notebook"))

var7 = c7.selectbox(
    "경정비 시설 유뮤",
    ("Pen","Pencil","Eraser","Sharpener","Notebook"))


var8 = c8.text_input("주유소명")


# 서울 행정구역 json raw파일(githubcontent)
r = requests.get("https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json")
c = r.content
seoul_geo = json.loads(c)

# 서울시 자치구별 상권정보 시각화
seoul = pd.read_csv("https://raw.githubusercontent.com/KIMMOOKYONG/Technical-Note/main/%EC%A7%80%EB%8F%84%EC%8B%9C%EA%B0%81%ED%99%94/%EC%86%8C%EC%83%81%EA%B3%B5%EC%9D%B8%EC%8B%9C%EC%9E%A5%EC%A7%84%ED%9D%A5%EA%B3%B5%EB%8B%A8_%EC%83%81%EA%B0%80(%EC%83%81%EA%B6%8C)%EC%A0%95%EB%B3%B4_%EC%84%9C%EC%9A%B8_202203_01.tsv", sep="\t")

# 필요한 컬럼 정보만 가져옵니다
seoul = seoul[["시군구명", "상권업종대분류명", "상권업종중분류명", "위도", "경도"]]
seoul_coffee = seoul.loc[seoul["상권업종중분류명"] == "커피점/카페"]
seoul_group_data = seoul.loc[seoul["상권업종중분류명"] == "커피점/카페"].groupby("시군구명")["상권업종중분류명"].count()

bins = list(seoul_group_data.quantile([0, 0.25, 0.5, 0.75, 1]))

m = folium.Map(
    location=[37.559819, 126.963895],
    zoom_start=11, 
    tiles="cartodbpositron"
)

folium.GeoJson(
    seoul_geo,
    name="지역구"
).add_to(m)

m.choropleth(geo_data=seoul_geo,
             data=seoul_group_data, 
             fill_color="YlOrRd", # 색상 변경도 가능하다
             fill_opacity=0.5,
             line_opacity=0.2,
             key_on="properties.name",
             legend_name="지역구별 커피 업종 수", 
             bins=bins
            )

# call to render Folium map in Streamlit
# 지도의 크기를 width, height 파라미터 설정해야함.
with m1:
    folium_static(m)


chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"]
)


with m2:
    st.table(seoul_group_data)
    st.bar_chart(chart_data)
    st.area_chart(chart_data)



```

![image](https://user-images.githubusercontent.com/102650331/169641147-1e9790dc-856d-4f1a-a383-b9d4e31790cf.png)

