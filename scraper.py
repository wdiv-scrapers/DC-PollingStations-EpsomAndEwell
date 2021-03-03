from dc_base_scrapers.xml_scraper import GmlScraper


stations_url = "https://maps.epsom-ewell.gov.uk/getOWS.ashx?MapSource=EEBC/inspire&service=WFS&version=1.1.0&request=GetFeature&Typename=pollingstations"
stations_fields = {
    "{http://mapserver.gis.umn.edu/mapserver}msGeometry": "msGeometry",
    "{http://mapserver.gis.umn.edu/mapserver}psnumber": "psnumber",
    "{http://mapserver.gis.umn.edu/mapserver}district": "district",
    "{http://mapserver.gis.umn.edu/mapserver}address": "address",
    "{http://mapserver.gis.umn.edu/mapserver}ward": "ward",
}

districts_url = "https://maps.epsom-ewell.gov.uk/getOWS.ashx?MapSource=EEBC/inspire&service=WFS&version=1.1.0&request=GetFeature&Typename=pollingdistricts"
districts_fields = {
    "{http://www.opengis.net/gml}boundedBy": "boundedBy",
    "{http://mapserver.gis.umn.edu/mapserver}msGeometry": "msGeometry",
    "{http://mapserver.gis.umn.edu/mapserver}district": "district",
    "{http://mapserver.gis.umn.edu/mapserver}pollingplace": "pollingplace",
}

council_id = "EPS"

class CustomScraper(GmlScraper):

    def process_feature(self, feature, tree):
        record = super().process_feature(feature, tree)
        record['id'] = feature[0].attrib['{http://www.opengis.net/gml}id']
        return record


stations_scraper = GmlScraper(
    stations_url, council_id, "stations", stations_fields, "psnumber"
)
stations_scraper.scrape()
districts_scraper = CustomScraper(
    districts_url, council_id, "districts", districts_fields, "id"
)
districts_scraper.scrape()
