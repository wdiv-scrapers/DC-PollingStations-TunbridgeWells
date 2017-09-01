from dc_base_scrapers.geojson_scraper import GeoJsonScraper


stations_url = "http://opendata-tunbridgewells.opendata.arcgis.com/datasets/feb0be539f0c4c3b97bcaf812f930282_6.geojson"
districts_url = "http://opendata-tunbridgewells.opendata.arcgis.com/datasets/3eeae54e88894e6ba65f6451c8e417f1_5.geojson"
council_id = 'E07000116'


stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()
