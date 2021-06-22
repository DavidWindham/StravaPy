import xml.etree.ElementTree as ET
from stravapy.datapoint import DataPoint


class StravaDataHandler:
    def __init__(self, directory):
        self.directory = directory
        self.event_name = None
        self.event_type = None
        self.data_points = []
        self.load_data_points()

    def set_new_file_dir(self, directory):
        self.directory = directory
        self.load_data_points()

    def load_data_points(self):
        gpx_tree = ET.parse(self.directory)
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

    def get_data_points(self):
        return self.data_points

    def get_data_points_dicts(self):
        return_list = []
        for single_point in self.data_points:
            return_list.append(single_point.get_dict())
        return return_list

    def __repr__(self):
        return repr(self.event_name)
