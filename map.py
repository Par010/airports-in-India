import folium

map = folium.Map(location=[19.118413, 73.030031], zoom_start=6)
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[19.025414, 73.025255], popup="Wonders Park", icon=folium.Icon(color="blue")))
map.add_child(fg)
map.save("Map.html")


