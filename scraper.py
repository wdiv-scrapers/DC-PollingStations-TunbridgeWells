import json
from dc_base_scrapers.common import get_data_from_url
from dc_base_scrapers.geojson_scraper import GeoJsonScraper

stations_url = "https://opendata.arcgis.com/datasets/ea6894c98dfb4cf99775d1fb949cf0de_6.geojson"
districts_url = "https://opendata.arcgis.com/datasets/24b6d662cd1145eba4743d27e91c0436_5.geojson"
council_id = 'E07000116'

print(stations_url)
stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
print(districts_url)
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()
