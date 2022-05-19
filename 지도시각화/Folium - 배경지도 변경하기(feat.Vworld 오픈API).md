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


# VWORLD & 구글맵 배경지도 변경
```python
#Foliium 불러오기
import folium
# 불러오고자 하는 지역의 중심이 되는 좌표 설정해 주고 이를 map_google로 명명합니다. 
map_google = folium.Map(location=[37.542130, 126.982402], zoom_start = 10) 
 
# 구글맵 기반의 지도 배경 설정을 해줍니다. 
basemaps_google = {
    'Google Maps': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Maps',
        overlay = True,
        control = True
    )}
 
# 위에서 설정한 구글 기반 지도를 map_google에 적용해 줍니다. 
basemaps_google['Google Maps'].add_to(map_google)
 
#map_google을 실행해 봅니다. 
map_google

```

```python
#Vworld 기반의 지도 배경 설정 
basemaps_vworld = {
    'VWorldBase': folium.TileLayer(
        tiles = 'http://api.vworld.kr/req/wmts/1.0.0/KEY/Base/{z}/{y}/{x}.png',
        attr = 'VWorldBase',
        name = 'VWorldBase',
        overlay = True,
        control = True
    )}
 
 
# 위에서 설정한 Vworld 기반 지도를 map_vworld에 적용해 줍니다.
basemaps_vworld['VWorldBase'].add_to(map_vworld)


```
