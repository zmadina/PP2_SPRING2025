from datetime import datetime, timedelta
current_date = datetime.today() 
yes_date = current_date - timedelta(days=1)  
tom_date = current_date + timedelta(days=1)

print(yes_date.strftime("%Y-%m-%d")) 
print(current_date.strftime("%Y-%m-%d"))
print(tom_date.strftime("%Y-%m-%d"))