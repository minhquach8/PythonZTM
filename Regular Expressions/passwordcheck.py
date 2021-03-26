import re

pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
password = 'f#$2343@#%$9fdfd'

check = pattern.fullmatch(password)
print(check)
