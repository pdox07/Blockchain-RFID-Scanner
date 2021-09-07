import requests
from ip2geotools.databases.noncommercial import DbIpCity

def get_geo():
    r = requests.get('http://jsonip.com')
    ip= r.json()['ip']
    #print(ip)
    response = DbIpCity.get(ip, api_key='free')
    return response.region, response.latitude, response.longitude

if __name__=="__main__":
    print(get_geo())