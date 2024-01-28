def heatmap(data):
    # Import functions
    import geopandas as gpd
    from shapely.geometry import Point
    import folium
    from folium.plugins import HeatMap

    # Convert DataFrame to GeoDataFrame
    gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.longitude, data.latitude))

    # Create a base map
    map = folium.Map(location=[0, 0], zoom_start=2)

    # Create a heatmap layer
    heat_data = [[point.xy[1][0], point.xy[0][0], magnitude] for point, magnitude in zip(gdf.geometry, gdf.mag)]
    HeatMap(heat_data, radius=10).add_to(map)

    # Save the map
    map.save("earthquake_heatmap.html")

    print("Saved")

    return