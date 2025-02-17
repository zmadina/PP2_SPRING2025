from datetime import datetime

current = datetime.now() 
clean = current.replace(microsecond=0)  

print(clean)  