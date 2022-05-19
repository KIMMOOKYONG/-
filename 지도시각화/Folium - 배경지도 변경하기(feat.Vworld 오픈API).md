# 지도 타일 변경

```python
import folium
from config import vworld_key

print(f"Folium Version: {folium.__version__}")

```

```python
# 지도 중심 경위도 좌표(위도, 경도) 설정하기
lat, lon = 37.504811111562, 127.025492036104
# 줌 설정하기
zoom_size = 15

# folium 지도 생성하기
m = folium.Map(
    location=[lat, lon],
    zoom_start=zoom_size
)
m

tiles = "Stamen Terrain"
# 배경지도 타일 레이어를 지도에 추가하기
folium.TileLayer(tiles=tiles).add_to(m)

# 배경지도 타일 설정하기
tiles = "Stamen Toner"
# 배경지도 타일 레이어를 지도에 추가하기
folium.TileLayer(tiles=tiles).add_to(m)

# 배경지도 타일 설정하기
tiles = "Stamen Watercolor"
# 배경지도 타일 레이어를 지도에 추가하기
folium.TileLayer(tiles=tiles).add_to(m)

# 배경지도 타일 설정하기
tiles = "CartoDB positron"
# 배경지도 타일 레이어를 지도에 추가하기
folium.TileLayer(tiles=tiles).add_to(m)

# 배경지도 타일 설정하기
tiles = "CartoDB dark_matter"
# 배경지도 타일 레이어를 지도에 추가하기
folium.TileLayer(tiles=tiles).add_to(m)

```

# 배경지도 VWorld 변경하기
```python
# folium 지도 생성하기
m = folium.Map(
    location=[lat, lon],
    zoom_start=zoom_size
)

# 배경지도 타일 설정하기

layer = "Base" # Base, gray, midnight, Hybrid, Satellite
tileType = "png"
tiles = f"http://api.vworld.kr/req/wmts/1.0.0/{vworld_key}/{layer}/{{z}}/{{y}}/{{x}}.{tileType}"
attr = "Vworld"

folium.TileLayer(
    tiles=tiles,
    attr=attr,
    overlay=True,
    control=True
).add_to(m)

m

```

# VWORLD 설정
```python
%%writefile config.py
vworld_key=FB439F46-E89D-33AE-8F73-C5A41E8EDB9E

```

# 참조 사이트
- https://wooiljeong.github.io/python/folium_tiles/
- 
