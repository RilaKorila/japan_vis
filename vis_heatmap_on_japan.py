import folium
import pandas as pd
import json

# 日本の都道府県のGeoJSON
geojson_path = "geo_data/japan.geojson"
with open(geojson_path, 'r', encoding='utf-8') as f:
    geojson_data = json.load(f)

# 都道府県ごとのデータ
data = pd.read_csv("numeric_data/population.csv")


# マップ作成
m = folium.Map(location=[36.0, 138.0], zoom_start=5)

# ヒートマップ（Choropleth）
folium.Choropleth(
    geo_data=geojson_data,
    data=data,
    columns=["Prefecture", "Value"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Value",
    highlight=True
).add_to(m)

# HTMLファイルとして保存
m.save("outputs/japan_prefecture_map.html")
