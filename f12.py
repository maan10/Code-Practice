import re

pattern='^a...e$'

Name="Alole"

find=re.match(pattern,Name)

print(find)