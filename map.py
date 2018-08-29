import folium
import pandas


data = pandas.read_csv("airports-in-india.csv")
lat = list(data["latitude_deg"])
lon = list(data["longitude_deg"])
name = list(data["name"])
wiki = list(data["wikipedia_link"])
typ = list(data["type"])
map = folium.Map(location=[19.118413, 73.030031], zoom_start=6)
fgl = folium.FeatureGroup(name="Large Airports")
fgm = folium.FeatureGroup(name="Medium Airports")
fgs = folium.FeatureGroup(name="Small Airports")
fgc = folium.FeatureGroup(name="Closed Airports")
fgh = folium.FeatureGroup(name="Heliport")

for lt, ln, nm, wk, ty in zip(lat, lon, name, wiki, typ):
    if str(ty) == 'large_airport':
        fgl.add_child(folium.Marker(location=[lt, ln], popup=folium.
                                    Popup('<a href={wk} target="_blank"> {nm} </a>'.format(wk=wk, nm=nm))
                                    if str(wk) != 'nan' else nm, icon=folium.Icon(color="black", icon='flag')))
    elif str(ty) == 'medium_airport':
        fgm.add_child(folium.Marker(location=[lt, ln], popup=folium.
                                    Popup('<a href={wk} target="_blank"> {nm} </a>'.format(wk=wk, nm=nm))
                                    if str(wk) != 'nan' else nm, icon=folium.Icon(color="gray", icon='flag')))
    elif str(ty) == 'small_airport':
        fgs.add_child(folium.Marker(location=[lt, ln], popup=folium.
                                    Popup('<a href={wk} target="_blank"> {nm} </a>'.format(wk=wk, nm=nm))
                                    if str(wk) != 'nan' else nm, icon=folium.Icon(color="lightgray", icon='flag')))
    elif str(ty) == 'closed':
        fgc.add_child(folium.Marker(location=[lt, ln], popup=folium.
                                    Popup('<a href={wk} target="_blank"> {nm} </a>'.format(wk=wk, nm=nm))
                                    if str(wk) != 'nan' else nm, icon=folium.Icon(color="white", icon='flag')))
    else:
        fgh.add_child(folium.Marker(location=[lt, ln], popup=folium.
                                    Popup('<a href={wk} target="_blank"> {nm} </a>'.format(wk=wk, nm=nm))
                                    if str(wk) != 'nan' else nm, icon=folium.Icon(color="darkpurple", icon='flag')))

map.add_child(fgl)
map.add_child(fgm)
map.add_child(fgs)
map.add_child(fgc)
map.add_child(fgh)
map.add_child(folium.LayerControl())
map.save("Map.html")
