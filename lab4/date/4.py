from datetime import datetime
date1 = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
difference = abs((date2 - date1).total_seconds())
print(int(difference))  