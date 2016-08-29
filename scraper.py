from gml_scraper import scrape


stations_url = "http://myeebc.epsom-ewell.gov.uk/getOWS.ashx?MapSource=EEBC/inspire&service=WFS&version=1.1.0&request=GetFeature&Typename=pollingstations"
stations_fields = {
    '{http://mapserver.gis.umn.edu/mapserver}ogc_fid': 'ogc_fid',
    '{http://mapserver.gis.umn.edu/mapserver}objectid': 'objectid',
    '{http://mapserver.gis.umn.edu/mapserver}psnumber': 'psnumber',
    '{http://mapserver.gis.umn.edu/mapserver}wardname': 'wardname',
    '{http://mapserver.gis.umn.edu/mapserver}stationtyp': 'stationtyp',
    '{http://mapserver.gis.umn.edu/mapserver}uprn': 'uprn',
    '{http://mapserver.gis.umn.edu/mapserver}address': 'address',
    '{http://mapserver.gis.umn.edu/mapserver}ward': 'ward',
    '{http://mapserver.gis.umn.edu/mapserver}easting': 'easting',
    '{http://mapserver.gis.umn.edu/mapserver}northing': 'northing',
    '{http://mapserver.gis.umn.edu/mapserver}url': 'url',
}

districts_url = "http://myeebc.epsom-ewell.gov.uk/getOWS.ashx?MapSource=EEBC/inspire&service=WFS&version=1.1.0&request=GetFeature&Typename=pollingdistricts"
districts_fields = {
    '{http://mapserver.gis.umn.edu/mapserver}ogc_fid': 'ogc_fid',
    '{http://mapserver.gis.umn.edu/mapserver}objectid': 'objectid',
    '{http://mapserver.gis.umn.edu/mapserver}wardcode': 'wardcode',
    '{http://mapserver.gis.umn.edu/mapserver}psnumber': 'psnumber',
    '{http://mapserver.gis.umn.edu/mapserver}id': 'id',
    '{http://mapserver.gis.umn.edu/mapserver}uprn': 'uprn',
    '{http://mapserver.gis.umn.edu/mapserver}comments': 'comments',
    '{http://mapserver.gis.umn.edu/mapserver}address': 'address',
    '{http://mapserver.gis.umn.edu/mapserver}shape_area': 'shape_area',
    '{http://mapserver.gis.umn.edu/mapserver}shape_len': 'shape_len',
}

council_id = 'E07000208'


scrape(stations_url, council_id, 'stations', stations_fields, 'ogc_fid')
scrape(districts_url, council_id, 'districts', districts_fields, 'ogc_fid')
