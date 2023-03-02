import geoip2.database

def get_country_code(ip_address):
    reader = geoip2.database.Reader('geolite/GeoLite2-Country.mmdb')
    try:
        response = reader.country(ip_address)
        return response.country.iso_code
    except:
        return None