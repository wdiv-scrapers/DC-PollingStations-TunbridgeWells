from dc_base_scrapers.geojson_scraper import GeoJsonScraper


stations_url = "http://opendata.tunbridgewells.opendata.arcgis.com/datasets/5e6a80d6f2b74aa3b3cb63844e11c279_0.geojson"
districts_url = "http://opendata.tunbridgewells.opendata.arcgis.com/datasets/431b83ef37ac4d56a7cdb3e19a92322b_0.geojson"
council_id = 'E07000116'


stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()
