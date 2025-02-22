
import re

pattern = r'a[b]*'

input_string = input()  

if re.match(pattern, input_string):
    print(f"'{input_string}' matches the pattern.")
else:
    print(f"'{input_string}' does not match the pattern.")
