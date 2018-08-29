import folium
import pandas

data = pandas.read_csv("airports-in-india.csv")

lat = list(data["latitude_deg"])
lon = list(data["longitude_deg"])
name = list(data["name"])
wiki = list(data["wikipedia_link"])

map = folium.Map(location=[19.118413, 73.030031], zoom_start=6)
fg = folium.FeatureGroup(name="My Map")
for lt, ln, nm, wk in zip(lat, lon, name, wiki):
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup('<a href={wk} target="_blank"> {nm} </a>'
                                                                     .format(wk=wk, nm=nm)), icon=folium.Icon(color="blue")))
map.add_child(fg)
map.save("Map.html")
