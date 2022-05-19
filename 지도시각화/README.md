# 지도 시각화 도구 Folium 사용법
- 매뉴얼: https://python-visualization.github.io/folium/

# folium 개요
- folium은 leaflet.js 기반으로 만들어진 Python 지도 시각화 라이브러리

# folium 설치
```
!pip install folium

```

# 기본 좌표 설정
- location: 위, 경도 좌표
- zoom_start: 지도 레벨, 확대 정도(최대 18)

# 마커 추가
- location: 위도/경도 좌표
- popup: 팝업 문구(클릭)
- tooltip: 툴팁 문구(마우스 오버)


# 서울 지도에서 행정 구역별 표시
```python
import requests
import json

# 서울 행정구역 json raw파일(githubcontent)
r = requests.get('https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json')
c = r.content
seoul_geo = json.loads(c)

m = folium.Map(
    location=[37.559819, 126.963895],
    zoom_start=11, 
)

folium.GeoJson(
    seoul_geo,
    name="지역구"
).add_to(m)

m

```

# tiles 옵션 변경을 통해 지도의 테마 변경
```python
m = folium.Map(
    location=[37.559819, 126.963895],
    zoom_start=11, 
    #tiles="Stamen Toner"
    tiles="cartodbpositron"
)

folium.GeoJson(
    seoul_geo,
    name="지역구"
).add_to(m)

m

```
![image](https://user-images.githubusercontent.com/102650331/169255494-24505b56-1eee-4e25-94ee-ed350b55bbb2.png)

![image](https://user-images.githubusercontent.com/102650331/169255543-1a55fc72-ff02-4735-b88b-820440531a99.png)

# 지역별 카페 분포를 범례와 함께 표현하기
```python
import requests
import json

# 서울 행정구역 json raw파일(githubcontent)
r = requests.get('https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json')
c = r.content
seoul_geo = json.loads(c)

# 서울시 자치구별 상권정보 시각화
seoul = pd.read_csv('https://raw.githubusercontent.com/KIMMOOKYONG/Technical-Note/main/%EC%A7%80%EB%8F%84%EC%8B%9C%EA%B0%81%ED%99%94/%EC%86%8C%EC%83%81%EA%B3%B5%EC%9D%B8%EC%8B%9C%EC%9E%A5%EC%A7%84%ED%9D%A5%EA%B3%B5%EB%8B%A8_%EC%83%81%EA%B0%80(%EC%83%81%EA%B6%8C)%EC%A0%95%EB%B3%B4_%EC%84%9C%EC%9A%B8_202203_01.tsv', sep="\t")

# 필요한 컬럼 정보만 가져옵니다
seoul = seoul[['시군구명', '상권업종대분류명', '상권업종중분류명', '위도', '경도']]
seoul

seoul_coffee = seoul.loc[seoul['상권업종중분류명'] == '커피점/카페']
seoul_coffee

seoul_group_data = seoul.loc[seoul["상권업종중분류명"] == "커피점/카페"].groupby("시군구명")["상권업종중분류명"].count()
seoul_group_data

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

marker_cluster = MarkerCluster().add_to(m)

for lat, long in zip(seoul_coffee['위도'], seoul_coffee['경도']):
    folium.Marker([lat, long], icon = folium.Icon(color="green")).add_to(marker_cluster)

m

```
 

# 지역별 카페 분포를 범례와 함께 표현하기
```python
import requests
import json

# 서울 행정구역 json raw파일(githubcontent)
r = requests.get('https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json')
c = r.content
seoul_geo = json.loads(c)

# 서울시 자치구별 상권정보 시각화
seoul = pd.read_csv('https://raw.githubusercontent.com/KIMMOOKYONG/Technical-Note/main/%EC%A7%80%EB%8F%84%EC%8B%9C%EA%B0%81%ED%99%94/%EC%86%8C%EC%83%81%EA%B3%B5%EC%9D%B8%EC%8B%9C%EC%9E%A5%EC%A7%84%ED%9D%A5%EA%B3%B5%EB%8B%A8_%EC%83%81%EA%B0%80(%EC%83%81%EA%B6%8C)%EC%A0%95%EB%B3%B4_%EC%84%9C%EC%9A%B8_202203_01.tsv', sep="\t")

# 필요한 컬럼 정보만 가져옵니다
seoul = seoul[['시군구명', '상권업종대분류명', '상권업종중분류명', '위도', '경도']]
seoul

seoul_coffee = seoul.loc[seoul['상권업종중분류명'] == '커피점/카페']
seoul_coffee

seoul_group_data = seoul.loc[seoul["상권업종중분류명"] == "커피점/카페"].groupby("시군구명")["상권업종중분류명"].count()
seoul_group_data

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
m

```


# 지도 분석 결과 저장하기
```python
m.save("map.html")

```


# 참조 사이트
- https://teddylee777.github.io/visualization/folium

