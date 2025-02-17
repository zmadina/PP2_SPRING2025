import json
import requests
url= 'https://raw.githubusercontent.com/zmadina/PP2_SPRING2025/refs/heads/PP2/data.json'
response = requests.get(url)
data=response.json()
object = data["imdata"]
print()
print(f"{'Interface Status'}")
print("=" * 79)
print(f"{'DN':<45} {'Description':<15} {'Speed':<9} {'MTU'}")
print('-'*43,'','-'*13,' ', '-'*7, ' ', '-'*6)


for item in object:
    attributes = item["l1PhysIf"]["attributes"]  
    dn_ = attributes["dn"]  
    description = attributes["descr"] 
    speed = attributes["speed"]  
    mtu = attributes["mtu"]  

    print(f"{dn_:<44} {description:<15} {speed:<10} {mtu}")