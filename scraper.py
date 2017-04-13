from dc_base_scrapers.geojson_scraper import GeoJsonScraper


stations_url = "http://opendata-tunbridgewells.opendata.arcgis.com/datasets/7175dd3565a94630b62008a4e2acf830_6.geojson"
districts_url = "http://opendata-tunbridgewells.opendata.arcgis.com/datasets/469b4be3d38849d2b867ae9514a06842_5.geojson"
council_id = 'E07000116'


stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()
