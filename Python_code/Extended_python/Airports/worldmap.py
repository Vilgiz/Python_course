import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt


class Map:
    """
    The Map class is responsible for plotting and displaying geographical data on a world map.
    """

    def plot(self, data):
        """
        Plots geographical data on a world map.

        Args:
            data (list): List of tuples representing coordinates (latitude, longitude).
        """
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        fig, ax = plt.subplots(figsize=(10, 6))
        world.plot(ax=ax, color='lightgrey')

        for dat in data:
            coordinates = {'Latitude': [dat[0]], 'Longitude': [dat[1]]}
            geometry = [Point(lon, lat) for lon, lat in zip(
                coordinates['Longitude'], coordinates['Latitude'])]
            geo_df = gpd.GeoDataFrame(coordinates, geometry=geometry)
            geo_df.plot(ax=ax, color='red', marker='o', markersize=5)

        plt.title('World Map with Marked Coordinates')

    def show(self):
        """
        Displays the plotted world map.
        """
        plt.show()


if __name__ == '__main__':
    map_instance = Map()
    data_to_plot = [(55.7558, 37.6176), (40.7128, -74.0060)]
    map_instance.plot(data_to_plot)
