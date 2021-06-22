import xml.etree.ElementTree as ET
from stravapy.datapoint import DataPoint


class StravaDataHandler:
    def __init__(self):
        self.event_name = None
        self.event_type = None
        self.data_points = []

    def get_data_points(self, dir):
        gpx_tree = ET.parse(dir)
        gpx_root = gpx_tree.getroot()

        self.event_name = gpx_root[1][0].text
        self.event_type = gpx_root[1][1].text

        self.data_points = []
        for single_gpx_point in gpx_root[1][2]:
            lat = single_gpx_point.attrib['lat']
            long = single_gpx_point.attrib['lon']
            elevation = single_gpx_point[0].text
            timestamp = single_gpx_point[1].text
            self.data_points.append(DataPoint(lat=lat, long=long, elevation=elevation, timestamp=timestamp))
