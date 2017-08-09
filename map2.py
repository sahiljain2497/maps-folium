import folium
import pandas

data=pandas.read_csv("volcanoes.txt")
lat=list(data['LAT'])
lon=list(data['LON'])
elev=list(data['ELEV'])

def color_maker(el):
    if el <1000:
        return 'green'
    elif 1000<= el <=3000:
        return 'orange'
    else:
        return 'red'
    
map=folium.Map(zoom_start=6,tiles="Mapbox Bright")

volcano=folium.FeatureGroup("Volcanoes")

for lt,ln,el in zip(lat,lon,elev):
    volcano.add_child(folium.CircleMarker(location=[lt,ln],popup=str(el)+'m',radius=8,weight=1, fill_color=color_maker(el)))

pop=folium.FeatureGroup("Population")

pop.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig'),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<1000000
else 'blue' if 1000000<=x['properties']['POP2005'] <20000005 else 'yellow'}))

map.add_child(volcano)
map.add_child(pop)
map.add_child(folium.LayerControl())
map.save("map2.html")
