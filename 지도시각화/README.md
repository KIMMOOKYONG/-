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


