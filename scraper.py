import json
from dc_base_scrapers.common import get_data_from_url
from dc_base_scrapers.geojson_scraper import GeoJsonScraper


def get_dataset_id(search_url):
    search_str = get_data_from_url(search_url)
    search_data = json.loads(search_str.decode('utf-8'))
    if len(search_data['data']) != 1:
        raise ValueError("Failed to find a dataset id")
    else:
        return search_data['data'][0]['id']


stations_search_url = "http://opendata-tunbridgewells.opendata.arcgis.com/datasets.json?q=polling%20station&sort_by=relevance"
districts_search_url = "http://opendata-tunbridgewells.opendata.arcgis.com/datasets.json?q=polling%20district&sort_by=relevance"
stations_base_url = "http://opendata-tunbridgewells.opendata.arcgis.com/datasets/%s.geojson"
districts_base_url = "http://opendata-tunbridgewells.opendata.arcgis.com/datasets/%s.geojson"
council_id = 'E07000116'

stations_url = stations_base_url % (get_dataset_id(stations_search_url))
districts_url = districts_base_url % (get_dataset_id(districts_search_url))

stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()
