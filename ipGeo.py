# * use : python ipGeo.py
import requests
import signal
import argparse
import json

def salida(sig, frame):
    print(" * Saliendo\n")
    exit(1)
signal.signal(signal.SIGINT, salida)

log = """
 _        ____            
(_)_ __  / ___| ___  ___  
| | '_ \| |  _ / _ \/ _ \ 
| | |_) | |_| |  __/ (_) |
|_| .__/ \____|\___|\___/ 
  |_|                     

"""

print(log)
api_ip = "http://ifconfig.me" 
api_geolocation = "http://ip-api.com/json/"

params = argparse.ArgumentParser(description="--help")


params.add_argument("--ip", type=str, help="Para saber tu direccion ip (publica).", required=False)
params.add_argument("--geo", action='store_true', help="Geolocaliza la direccion ip.")
args = params.parse_args()


if args.geo:
    if args.ip:
        
        def geolocalizacion(ip, geo):
            
            print(f"\n* Geolocalizando {ip}\n")
            geo_result = requests.get(api_geolocation + ip)
            result = str(geo_result.json())
            
            for x in result.replace(',','\n').replace('{','').replace('}','').replace("'",'').splitlines():
                print(f"   * {x}")
            print("")
            exit(0)
        ip = args.ip
        geo = args.geo

        geolocalizacion(ip, geo)
    else:
        print("\n    * No hay direccion ip, use --ip {ip} --geo\n")
else:

    print("\n-------\n* Obteniendo su direccion ip Publica.")
    ip_result = requests.get(api_ip)
    print(f"    Ip (p) : {ip_result.text}\n-------\n")
    

