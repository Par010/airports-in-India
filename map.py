import folium
import pandas


data = pandas.read_csv("airports-in-india.csv")
lat = list(data["latitude_deg"])
lon = list(data["longitude_deg"])
name = list(data["name"])
wiki = list(data["wikipedia_link"])
typ = list(data["type"])


def color_producer(tp):
    if str(tp) == 'large_airport':
        return "black"
    elif str(tp) == 'medium_airport':
        return "gray"
    elif str(tp) == 'small_airport':
        return "lightgray"
    elif str(tp) == 'closed':
        return "white"
    else:
        return "darkpurple"


map = folium.Map(location=[19.118413, 73.030031], zoom_start=6)
fg = folium.FeatureGroup(name="My Map")
for lt, ln, nm, wk, ty in zip(lat, lon, name, wiki, typ):
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup('<a href={wk} target="_blank"> {nm} </a>'
                                                                     .format(wk=wk, nm=nm)) if str(wk) != 'nan' else nm,
                               icon=folium.Icon(color=color_producer(ty), icon='flag')))
map.add_child(fg)
map.save("Map.html")
